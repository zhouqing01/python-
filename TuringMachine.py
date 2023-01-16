table = input().split()
c = dict()

while True:
    dot = dict()
    table1 = input().split()
    len_v = len(table1)
    if len_v == 1:
        l = table1[0]
        break
    for i in range(len_v):
        dot[table[i-1]]=table1[i].split(',')
    c[table1[0]]=dot

num='0'
M = 0
operate = 2
for i in range(100000):
    if M>=len(l):
        S=c[num]['_']
        if S[operate-2]:
            l+=S[operate-2]
    elif M<0:
        S=c[num]['_']
        if S[operate-2]:
            l=S[operate-2]+l
    else:
        S=c[num][l[M]]
        if S[operate-2]:
            l=l[:M]+S[operate-2]+l[M+1:]
    if S[operate-1] == 'L':
        M -= 1
    if S[operate-1] == 'R':
        M += 1
    if S[operate] == '!':
        print(l.replace('_',''))
        break
    if S[operate]:
        num=S[operate]

