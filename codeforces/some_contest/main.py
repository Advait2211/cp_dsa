import re
import numpy as np
import pandas as pd
import torch
from PIL import Image
from io import BytesIO
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
import lightgbm as lgb

# Transformers for DINOv2
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode
from transformers import DINOv2FeatureExtractor, DinoV2Model

# SentenceTransformers for text embeddings
from sentence_transformers import SentenceTransformer

# --------- 1) Load data ---------
df = pd.read_csv('train.csv').sample(200000, random_state=42)  # sample for speed; remove .sample for full data

# --------- 2) Text cleaning & numeric features ---------
def clean_text(s):
    s = str(s).lower()
    s = s.replace("–","-").replace("—","-").replace("•"," ")
    return re.sub(r"\s+", " ", s).strip()

df["text"] = df["catalog_content"].fillna("").map(clean_text)

def extract_pack_count(text):
    m = re.search(r"(pack of|x)\s*([0-9]+)", text)
    if m: return int(m.group(2))
    m2 = re.search(r"([0-9]+)\s*(pack|pk)", text)
    return int(m2.group(1)) if m2 else 1

def extract_qty(text):
    m = re.search(r"([0-9]+(\.[0-9]+)?)\s*(fl\s*oz|ounce|oz|g|gram|kg|ml|l|lb|pound)", text)
    return (float(m.group(1)), m.group(3).replace(" ","")) if m else (np.nan, None)

df["pack_count"] = df["text"].map(extract_pack_count)
qty = df["text"].map(extract_qty)
df["qty_value"] = [v for v,u in qty]
df["qty_unit"]  = [u for v,u in qty]

unit_scale = {
    "ounce":28.3495, "oz":28.3495, "floz":29.5735,
    "g":1.0, "gram":1.0, "kg":1000.0,
    "ml":1.0, "l":1000.0, "lb":453.592, "pound":453.592
}
df["qty_grams"] = df.apply(lambda r: (r.qty_value or 0) * unit_scale.get(r.qty_unit,1), axis=1)
df["qty_grams"].replace(0, np.nan, inplace=True)
df["qty_grams"].fillna(df["qty_grams"].median(), inplace=True)
df["total_qty_grams"] = df["qty_grams"] * df["pack_count"]

# --------- 3) Image embedding setup ---------
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = DINOv2FeatureExtractor.from_pretrained("facebook/dinov2-vitb14-pre")
model_img = DinoV2Model.from_pretrained("facebook/dinov2-vitb14-pre").to(device)
img_transform = transforms.Compose([
    transforms.Resize(224, interpolation=InterpolationMode.BICUBIC),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=processor.image_mean, std=processor.image_std)
])

def embed_image(url):
    try:
        response = requests.get(url, timeout=5)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        pixel_values = img_transform(img).unsqueeze(0).to(device)
        with torch.no_grad():
            emb = model_img(pixel_values).image_embeds
        return emb[0].cpu().numpy()
    except:
        return np.zeros(model_img.config.hidden_size, dtype=np.float32)

# --------- 4) Text embedding setup (all-MiniLM-L6-v2) ---------
model_text = SentenceTransformer("all-MiniLM-L6-v2", device=device)

# --------- 5) Generate embeddings for a subset ---------
# For demonstration speed, limit to first 50k rows; remove head() for full data
sub = df.head(50000).copy()

# Image embeddings
sub["img_emb"] = sub["image_link"].map(embed_image)

# Text embeddings
texts = sub["text"].tolist()
txt_embs = model_text.encode(texts, batch_size=128, show_progress_bar=True)
sub["txt_emb"] = list(txt_embs)

# --------- 6) Prepare final feature matrix ---------
X_num = sub[["pack_count","qty_grams","total_qty_grams"]].values
scaler = StandardScaler().fit(X_num)
X_num = scaler.transform(X_num)

# Stack embeddings
X_img = np.stack(sub["img_emb"].values)
X_txt = np.stack(sub["txt_emb"].values)

X = np.hstack([X_num, X_img, X_txt])
y = sub["price"].values

# --------- 7) Train/validation split ---------
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.1, random_state=42
)

# --------- 8) LightGBM training ---------
train_data = lgb.Dataset(X_train, label=y_train)
val_data   = lgb.Dataset(X_val,   label=y_val, reference=train_data)

params = {
    "objective":"regression_l1",
    "metric":"l1",
    "learning_rate":0.05,
    "num_leaves":31,
    "feature_fraction":0.8,
    "bagging_fraction":0.8,
    "bagging_freq":5,
    "seed":42
}
model = lgb.train(
    params,
    train_data,
    num_boost_round=1000,
    valid_sets=[train_data,val_data],
    early_stopping_rounds=50,
    verbose_eval=50
)

# --------- 9) Evaluate SMAPE ---------
def smape(a, f):
    denom = (np.abs(a) + np.abs(f)) / 2
    return 100 * np.mean(np.where(denom==0, 0, np.abs(f-a)/denom))

y_pred = model.predict(X_val)
print("Validation SMAPE (%):", round(smape(y_val, y_pred), 4))

# --------- 10) Save pipeline ---------
import joblib
joblib.dump({
    "scaler": scaler,
    "model_img": model_img.state_dict(),
    "model_text": model_text,
    "lgb_model": model
}, "dinov2_sgceip_pipeline.pkl")
