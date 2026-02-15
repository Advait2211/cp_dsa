from pynput import keyboard
import time

char_count = 0
active_time = 0.0
last_key_time = None
elapsed_time = 0
start = time.time()

IDLE_THRESHOLD = 0.5  # seconds (adjustable)

def on_press(key):
    global char_count, last_key_time, active_time

    now = time.time()

    if last_key_time is not None:
        delta = now - last_key_time
        if delta <= IDLE_THRESHOLD:
            active_time += delta  # count only active typing time

    last_key_time = now

    try:
        if key.char is not None:
            char_count += 1
    except AttributeError:
        pass  # ignore special keys

def on_release(key):
    if key == keyboard.Key.esc:
        minutes = active_time / 60
        words = char_count / 5
        wpm = words / minutes if minutes > 0 else 0

        print("\n--- Typing Stats (Fair) ---")
        print(f"Characters typed: {char_count}")
        print(f"Active typing time: {active_time:.2f} seconds")
        print(f"Typing speed: {wpm:.2f} WPM")
        end = time.time()
        print(f"elapsed time: {(end - start):.2f}s")
        return False

print("Fair typing tracker started.")
print("Pauses longer than 3 seconds are ignored.")
print("Press ESC to stop.\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
