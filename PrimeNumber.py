import math
a,b = map(int,input().split())
for i in range(a,b+1):
    flag = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
    if flag == 0:
        # list.append(str(i))
        print(i,end = " ")
