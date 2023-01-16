from itertools import tee, zip_longest


# def nomore(sequence):
#     s=[]
#     for i in sequence:
#         for j in sequence:
#             if j<i or j==i:
#                 s.append(j)
#
#     return s
#
# #print([n % 13 for n in range(5,23,3)])
# #print(*nomore([n % 13 for n in range(5,23,3)]))
#
def seesaw(seq):
    # x1,x2=tee(seq,2)
    # print(x1, x2)
    # x=[[],[]]
    # j=0
    y1=[]
    y2=[]
    # for sem in iterators2:
    #     x[j]=list(sem)
    #     j+=1
    # x = zip_longest(x[0], x[1])
    #print(list(x))
    #print(seq)
    for i in seq:
        if i%2==0:
            y1.append(i)
        else:
            y2.append(i)
    #print(y1,y2)
    s=min(len(y1),len(y2))
    ss=[]
    if s==0:
        if s==len(y1):
            ss=y2
        else:
            ss=y2
    else:
        if s == len(y1):
            for i in range(len(y1)):
                ss.append(y1[i])
                ss.append(y2[i])
            for j in (y2[i + 1:]):
                ss.append(j)
        else:
            for i in range(len(y2)):
                ss.append(y1[i])
                ss.append(y2[i])
            for j in (y1[i + 1:]):
                ss.append(j)


    return ss

#print([i//3 for i in range(1, 27, 2)])
#print(*seesaw(i//3 for i in range(1, 27, 2)))
#print(*seesaw([1] * 20))

# def PiGen():
#
# import math
# import time
import decimal

def PiGen():
    D = decimal.Decimal
    decimal.getcontext().prec = 10000
    L = D(13591409)
    X = D(1)
    M = D(1)
    K = D(6)
    q = D(0)
    sum = D(0)
    while True:
        pi = 426880 * (D(10005).sqrt()) * (sum ** -1)
        yield pi
        sum = sum + M * L / X
        Lq = L + 545140134
        Xq = X * (-262537412640768000)
        Mq = M * ((K ** 3 - 16 * K) / (q + 1) ** 3)
        Kq = K + 12
        q = q + 1
        L = Lq
        X = Xq
        M = Mq
        K = Kq
#print(f'计算完成。时间（秒）：{time_end - time_start}')
# for i, p in enumerate(PiGen()):
#     if i>120:
#         #print(p)
#         break
# print(str(p)[1400:1470])

# print(f'迭代{71}次计算圆周率：\n{str(pi)[1400:1470]}')
# from time import time
# ctime = time()
# for p in PiGen():
#     if time()-ctime > 4:
#         break
# print(str(p)[5000:5070])
# for i, p in enumerate(PiGen()):
#     if i>120:
#         break
# print(str(p)[1400:1470])

#turtle
def turtle(coord,direction):
    #t = yield "x"

    while True:
        t = yield coord

        #print(t)
        #print("-----",direction, t)
        if t=="f":
            if direction==0:
                coord = (coord[0] + 1, coord[1])
                #yield coord  # +(1,0)
            elif direction==1:
                coord = (coord[0], coord[1]+1)
                #yield coord
            elif direction==2:
                coord = (coord[0] - 1, coord[1])
                #yield coord  # +(1,0)
            elif direction==3:
                coord = (coord[0], coord[1]-1)
                #yield coord
        elif t=="l":
            if direction==0:
                direction=1
                #yield coord
            elif direction==1:
                direction=2
                #yield coord
            elif direction==2:
                direction=3
                #yield coord
            else:
                direction=0
                #yield coord
        elif t=="r":
            if direction == 0:
                direction = 3
                #yield coord
            elif direction == 1:
                direction = 0
                #yield coord
            elif direction == 2:
                direction = 1
                #yield coord
            else:
                direction = 2
                #yield coord

    # while t:
    #     if t=="f" and direction=='0':
    #         c=(coord[0]+1,0)
    #         yield c
# robo = turtle((0, 0), 0)
# start = next(robo)
# for c in "flfrffrffr":
#     print(*robo.send(c))