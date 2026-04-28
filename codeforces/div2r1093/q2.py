import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    """
    what is the case for exit?
    only when he gets caught
    he came move ahead and behind as much as he wants

    we don't need to have a simulation
    we just need to check if the situation where he is caught, can be created or not. 

    we have to check if there can be trapped

    so how do we do that
    the situation of a trap would be like this:

    right at 0
    left at 0
    cur at m-1
    0 4 0, for m = 5

    say you came here from the left. in order to get trapped, you would have to be forced to come here
    4 4 3 4

    or he is at the edge
    4 3 4, and has to move

    wait no i got it wrong
    in this case you would be safe, it take the start of the second

    like trapped position would be like 
    4 4 4 and you are at the middle position

    why would you get forced into a situation like this?

    trust your intuition

    oh oh oh 
    the logic is something like this
    if the consecuetive of ones of some length (possibly k-1 or k) are at a same value
    then it would not work

    dry running

    k = 3
    1 1 1 0 1 0

    2 2 2 1 2 1

    okay but you would get caught only if start was 1
    if it were to be 0

    0 0 0 1 0 1
    1 1 1 2 1 2
    2 2 2 0 2 0
    0 0 0 1 0 1

    1 0 0 0 
    so initially you won't be able to pass the sequence if the k - (len + val) < 0

    and for later cases, it won't work if the value k - len < 0

    but somehow i am not very sure about this
    okay nvm i am sure

    more dry runs before submitting

    our assumption is, after the first instance the value does not matter
    but i think i should write a special case for 2

    0 0 
    you exit - safe
    case of 2
    X 0 1 1

    0 0 1


    what situation would force a trap?
    think about it
    all places around you hit 0
    initially you may be forced to exit
    so we checked that condition

    1 1 1 0 0 1 - 2
    2 2 2 1 1 2 - 3
    0 0 0 2 2 0 - 4
    1 1 1 0 0 1 - 3
    2 2 2 1 1 2 - 4
    0 0 0 2 2 0 - 5
    1 1 1 0 0 1 - 6

    okay we don't change TC1 and TC2. 

    make new test cases
    either there is a specific case of 2
    if case of 2, no two elements can be same
    also for starting
    you have to start at 0

    
    when do you get trapped?
    you cannot stay where you are
    your immediate right is cooked
    your immediate left is cooked

    okay
    so nothing i am thinking up is working
    what if we have a sliding window of size 3
    and check if you are getting cooked at any point in time

    um
    how would i check if i am enforced to reach this
    no i cannot run a simulation looking at the constraints

    um wait
    i think i can run a simulation
    why tf not


    """

    cont = 1
    
    if k == 2:
        for i in range(1, n):
            if a[i] == a[i-1]:
                return "NO"
        return "YES"

    for i in range(1, n):
        if a[i] == a[i-1]:
            cont += 1
            if cont >= k:
                return "NO"
        else:
            cont = 1
            
    return "YES"
            

    # i = 0
    # pos = 0

    # touch = [0] * n

    # # so check if you can start safe

    # if a[0] == 0 and a[1] == 0:
    #     return "NO"
    

    # while pos < n-1:
    #     touch[pos] += 1

    #     if touch[pos] > n:
    #         return "NO"
    #     if (a[pos+1] + i) % k != 0:
    #         pos += 1
    #     elif (a[pos] + i) % k != 0:
    #         pass
    #     elif i >= 0 and (a[pos-1] + i) % k != 0:
    #         pos -= 1
    #     else:
    #         return "NO"
        
    #     # print(pos)

    #     i += 1


    
            
        # print(f"{start=}")
        # print(cont)
            
    return 'YES'
    

    


t = int(input())
for _ in range(t):
    print(solve()) 