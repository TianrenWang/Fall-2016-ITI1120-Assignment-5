# Course: ITI 1120
# Assignment # 5 Part 3
# Wang, Tianren
# 6040795

import math

def digit_sum(n):
    '''(int)->int
    Return sum of all digits of n
    Precondition: n is an integer
    '''

    n = int(math.sqrt(n**2))
    
    if n < 10:
        return n
    else:
        return n%10 + digit_sum(n//10)

def digital_root(n):
    '''(int)->int
    Compute the digital root of n
    Precondition: n is an integer
    '''

    n = int(math.sqrt(n**2))
    x = digit_sum(n)
    
    if x < 10:
        return x
    else:
        return digit_sum(x)
