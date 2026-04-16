def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated? first call
    elif len(L) > 1:                                  #   and what are the values being added? 4(length of this)+2(length of is)+3(length of the)=9
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated? third call
    elif len(L) > 0:                                  #   and what are the values being added? 7(length of another)
        result = len(L[0])                            # For which call below is this statement evaluated? second call
    else:                                             # and what are the values being added? 11(length of second call)
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()