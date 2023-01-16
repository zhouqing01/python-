
import math
a,b,c = map(int,input().split(","))
delta = b*b - 4*a*c
if a == 0 | b!=0:
    print(-c//b)
if delta>0:
    x_1=(-b-math.sqrt(delta))/(2*a)
    x_2=(-b+math.sqrt(delta))/(2*a)
    if x_1 > x_2:
        print(x_2,x_1)
    else:
        print(x_1,x_2)
if delta < 0:
    print(0)
if delta == 0:
    print(-1.0)