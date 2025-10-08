import sys

p = int(input())

if p >= 18:
    t = int(input())
    if p+t >= 60:
        print("Passed")
    else:
        print("Failed")
else:
    print("Failed")