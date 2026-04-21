
more = [x+1 for x in [1,2,3,4]] #list, in order, the values that x takes at each step
print()  #what is the values of more at this point? 1+1=2, 2+2=3, 3+1=4, 4+1=5 SO more=[2,3,4,5]

def square(n:int) -> int:
    return n * n    # Record, in order of the calls, each value of n and the corresponding return value.
                    # values of n: 1,2,3,4
                    # return: [1,4,9,16] b/c 1(1*1), 4 (2*2), 9 (3*3), 16(4*4)

def check(n:int) -> bool:
    return n > 2    # Record, in order of the calls, each value of n and the corresponding return value.
                    # values of n: 0, 1,2,3,4 b/c of range(5)
                    # returns: False, False, False, True, True
answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print()

def inc(m:int) -> int:
    return m + 1       # Record, in order of the calls, each value of m and the corresponding return value.
                       # values of m: 3,4
                       # return: 4,5 b/c 3+1=4 4+1=5

def check(n:int) -> bool:
    return n > 2         # Record, in order of the calls, each value of n and the corresponding return value.
                         # values of n: 0, 1,2,3,4
                        #returns: False, False, False, True, True
answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5] b/c inc(3)=4, inc(4)=5
print()