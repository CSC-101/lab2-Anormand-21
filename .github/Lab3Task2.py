
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num    # Record each value of total and num at the end of the loop body.
                               # First: value of initial total=0, num=4, total=4 (0+4)
                                #Second: value of initial total= 4, num=9 total =13
                                # Third: value of initial total=13, num=2, total=15
                                #Fourth: value of initial total= 15, num=1, total=16
    return total
result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
                                       #First: idx=0, append nums[0]=4 SO new_list=[4]
                                        # Second: idx=1, append nums[1]=9 SO new_list=[4,9]
                                        # Third: idx=2, append nums[2]=2 SO new_list=[4,9,2]
                                         # Fourth: idx=3, append nums[3]=1 SO new_list=[4,9,2,1]
    return new_list                    # How does this loop differ from that above? the one above computed the sum (one #), rather than creating a combined list (append)
result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
                                       # First: value=4, append 4+1=5, SO new_list=[5]
                                     # Second: value=9, append 9+1=10, SO new_list=[5,10]
                                     # Third: value=2, append 2+1=3, SO new_list=[5,10,3]
                                        # Fourth: value=1, append 1+1=2, SO new_list=[5,10,3,2]
    return new_list
result = increment_all([4, 9, 2, 1])