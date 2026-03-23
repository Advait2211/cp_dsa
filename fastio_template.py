import sys

def main():
    # 1. Read everything at once and split by whitespace
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 2. Create an iterator to easily grab the next token
    tokens = iter(input_data)
    
    t = int(next(tokens))
    out = []
    
    for _ in range(t):
        n = int(next(tokens))
        
        # Grab the next 'n' tokens for list 'a'
        a = [int(next(tokens)) for _ in range(n)]
        
        x = int(next(tokens))
        y = int(next(tokens))
        z = int(next(tokens))
        
        # --- YOUR LOGIC HERE ---
        # ans = x + y + z + sum(a)
        ans = "Result"
        
        # 3. Store string answers in an array instead of printing immediately
        out.append(str(ans))
        
    # 4. Print all answers at once, joined by newlines
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()