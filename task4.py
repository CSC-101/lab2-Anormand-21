from typing import Optional  #gain access to the Optional[x}type hint

def checked_access (L:list[int], idx:int) -> Optional[int]:
    test = idx >=0 and idx < len(L) #what is the value of test on each call? test=9 on first, test=2 on second
    if test: #what is this check preventing? preventing syntax error
        return L[idx]
    else:
        return None

first = checked_access([1,0,1],9) #what is the values of first? first:None
second = checked_access([1,0,1],2) #what is the values of second? second: 1
print()