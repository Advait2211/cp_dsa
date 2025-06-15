t = int(input())

for _ in range(t):
    length = int(input())
    s = input()

    # print(length, s)
    transfer = 0

    for i in range(length-1, -1, -1):
        # print(f's[i]={type(s[i])}')
        temp = int(s[i])
        while temp == 0:
            transfer += 1
            print("in i == 0")
            print(transfer)
            i -= 1
            temp = int(s[i])

        while temp == 1:
            transfer += 1
            print("in i == 1")
            print(transfer)
            i -= 1
            temp = int(s[i])

        print("transfer types")
        # print(s[transfer:])
        print(s[:transfer])

