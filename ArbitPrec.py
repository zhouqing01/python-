from decimal import *

def get_func(func, x):
    res = eval(func)
    return res


func = input()
d = int(input())
getcontext().prec = d + 2

left = Decimal('-1.5')
left_value = get_func(func, left)
# print(left_value)
right = Decimal('1.5')
right_value = get_func(func, left)
# print(right_value)

while right_value != Decimal('0') and (right-left) > 10 ** (-d):
    mid = (right + left) / 2
    mid_value = get_func(func, mid)
    if mid_value > 0 and left_value > 0 or mid_value < 0 and left_value < 0:
        left = mid
        left_value = mid_value
    else:
        right = mid
        right_value = mid_value   
print('{:.{prec}f}'.format(right, prec=d))