# def seesaw(a):
#     jishu=[]
#     oushu = []
#     b = []
#     for i in a:
#         if i%2 == 1:
#             jishu.append(i)
#         if i%2 == 0:
#             oushu.append(i)
#     c = []
#     if len(jishu)>len(oushu):
#         c = jishu
#     else:
#         c = oushu
#     lenmin = min(len(jishu),len(oushu))
#     for i in range(lenmin):
#         b.append(oushu[i])
#         b.append(jishu[i])
#     lenmax = max(len(jishu),len(oushu))
#     for j in range(lenmin,lenmax):
#         b.append(c[j])

#     return b

# def seesaw(a):
#     jishu=[]
#     oushu = []
#     while True:
#         yield b

#         for i in a:
#             if i%2 == 1:
#                 jishu.append(i)
#             if i%2 == 0:
#                 oushu.append(i)

def seesaw(a):
    jishu=[]
    oushu = []
    ss = []
    for i in a:
        if i%2 == 1:
            jishu.append(i)
        if i%2 == 0:
            oushu.append(i)
    lenmin = min(len(jishu),len(oushu))

    if lenmin==0:
        if lenmin==len(jishu):
            ss=oushu
        else:
            ss=jishu
    else:
        if lenmin == len(oushu):
            for i in range(len(oushu)):
                ss.append(oushu[i])
                ss.append(jishu[i])
            for j in (jishu[i + 1:]):
                ss.append(j)
        else:
            for i in range(len(jishu)):
                ss.append(oushu[i])
                ss.append(jishu[i])
            for j in (oushu[i + 1:]):
                ss.append(j)

    return ss
        

# print(*seesaw(i//3 for i in range(1, 27, 2)))
# print([i//3 for i in range(1, 27, 2)])