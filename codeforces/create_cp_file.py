#!/usr/bin/env python3
import os
import argparse

# Base path for your Codeforces problems
BASE_DIR = "/Users/advaitdesai/Programming/CpDsa/codeforces"

TEMPLATE = '''# problem_link

"""
logic:

"""


def solve():
    n = int(input())
    a = list(map(int, input().split()))



t = int(input())

for _ in range(t):
    print(solve())
'''

def main():
    parser = argparse.ArgumentParser(description="Create Codeforces CP template file")
    parser.add_argument("rel_path", help="Relative path inside the base directory (e.g., div3r1055)")
    parser.add_argument("filename", help="Python filename to create (e.g., q1.py)")
    args = parser.parse_args()

    full_dir = os.path.join(BASE_DIR, args.rel_path)
    os.makedirs(full_dir, exist_ok=True)

    full_path = os.path.join(full_dir, args.filename)

    if os.path.exists(full_path):
        print(f"❌ File already exists: {full_path}")
    else:
        with open(full_path, 'w') as f:
            f.write(TEMPLATE)
        print(f"✅ Created file: {full_path}")

if __name__ == "__main__":
    main()
