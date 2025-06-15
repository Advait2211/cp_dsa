from collections import Counter
something = dict((Counter([1, 2, 2, 3, 3, 3])))

print(type(something))

print(something)

for key, value in something.items():
    print(key, value)