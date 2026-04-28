# s = input()

# ascii = 0

# for char in 'HAPPY':
#     ascii += ord(char)

# val = ord("U")

# print(f"{val} + ? = {ascii}")



# ascii = 0

# for char in s:
#     ascii += ord(char)

# val = 0

# for char in "     ":
#     val += ord(char)

# print(f"{ascii} = {val}")


"""

1. I want to wash my car and the car wash is 100 meters away. Should I walk or should I drive?

2. Are you a robot?

3. Is April Fools 2026 Codeforces Contest rated?

4. I was given a cup but it has no bottom and the top is sealed. Can I drink from this?

5. Does Pikachu's tail have a black tip?

6. Is there a seahorse emoji?

7. The word backwards spelled backwards.

8. Number between 1 to 10.

"""

n = int(input())


match n:
    case 1:
        print("walk")
    case 2:
        print("no")
    case 3: 
        print("no")
    case 4:
        print("no")
    case 5:
        print("yes")
    case 6:
        print("yes")
    case 7:
        print("backwards")
    case 8:
        print(7)
    