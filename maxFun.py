from math import *

def maxfun_1(rang, *args):
    result = 0
    maxsum = sum(map(args[0], rang))
    for a,the_value in enumerate(args):
        maxvalue = sum(map(the_value, rang))
        if maxvalue >= maxsum:
            maxsum = maxvalue
            result = the_value
    return result


def maxfun_2(*S):
    p = [sum([k(j) for j in S[0]]) for f,k in enumerate(S[-1:0:-1])]
    return p

print(maxfun_1(range(-2,10), sin, cos, exp)(1))
#print(maxfun_2(range(-2,10), sin, cos, exp)(1))