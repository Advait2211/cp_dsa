import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = input().strip()

    """
    this question has a beautiful observation

    you would need 52 characters per alphabet
    ie aa ab ac ad ae af.... and so on.. 

    52 chars * 26 alphabets =  1352 > 1000

    WHICH WAS BEAUTIFUL, till it was wrong
    since we are considering lexicographical, we only need to consider string starting with a.
    should not really care about strings starting with others characters.
    
    okay. 
    so now that we know that
    can we just have a 3x for loop
    this is just 26
    """

    seta = set()
    import string

    chars = list(string.ascii_lowercase)

    # print(chars)

    for char in a:
        seta.add(char)

    for i in range(n-1):
        seta.add(f"{a[i]}{a[i+1]}")

    for i in range(n-2):
        seta.add(f"{a[i]}{a[i+1]}{a[i+2]}")

    # print(seta)


    for c in chars:
        if c not in seta:
            return c

    for i in chars:
        for j in chars:
            temp = f"{i}{j}"
            if temp not in seta:
                return temp
    
    for i in chars:
        for j in chars:
            temp = f"a{i}{j}"
            if temp not in seta:
                return temp
            
    

    


t = int(input())
for _ in range(t):
    print(solve()) 