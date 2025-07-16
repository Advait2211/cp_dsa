def solve():
    n = int(input())
    a = list(map(int, input().split()))


t = int(input())

for _ in range(t):
    solve()


"""
time complexity is n**2 so plenty of time
space is also not an issue


so what do we do here?

first we sort in invserse order
now, we can convert 0 to 1, till value of our element > 1

when value of our element becomes 1, it is equivalent to add 1, or to make the number before it double, sum += 2 

if we have multiple ones, then it is optimal to take 2 after a certain respectable value has been reached

questions to solve:
when to take that 1? 

what is a respectable value increase that we are looking for? 

see we will go into this situation, only and only if count of 1 is greater than 1. if we have only 1-1 then there is not issue
this leads me to thinking, the count of ones we have, is the only place we should convert 1 to 2
in all other cases, directly taking the value is optimal

of course, we will be making 2's from the start, so that x has reached the maximum value it can reach

so taking the input test case
1 1 1 4

sorted
4 1 1 1


k = 1
4 1 1 1
1
4

k = 2
4 1 1 1
1 1
5

k = 3
4 1 1 1
1 1 1
6
now here, having the subset as 2, 1 and 1 1 1 yeilds the same result. so if it is yeilding the same result, we will take the extra number. ie, if we have the first 1, we will give it value

then any 1 that comes after it, is quite useless. 
k = 4
8
4 1 1 1
2 1 1

i get what i did, but how do i make the algorithm understand? 
essentially, we don't make the last 1 into 2


k = 5
10
4 1 1 1
2 1 1 1


4 2 1 1
1 1 1 1
8

4 2 1 1
1

4 2 1 1
1 1

4 2 1 1
2 1 - 2 + 1 + 4 = 7

4 2 1 1
2 1 1
4 + 2 + 2 + 1 = 9

if length before the number is greater than the number, then taking that number is not worth it
don't convert the last 1 to 2, because that is pointless. 

5 4 3 1 1
2 1 1 - 3 + 4 + 5 + 2 = 14

5 4 3 1 1
2 2 1 - 3 + 4 + 5 + 1 + 2 = 15

5 4 3 1 1
2 1 1 1 - 3 + 4 + 5 + 3 = 15


5 4 3 1 1
2 2 1 1




wait. so even if i have 1, just saying a single 2 is better than having a 2 more often

of course. i had thought of it so long ago

after getting 3rd one, so before marking the third one, 
"""