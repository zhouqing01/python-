a = input()
b = list()
line = a.split(',')

b.append(line)
N = len(line)
c = N-1
while c > 0:
    a = input()
    line = a.split(',')
    b.append(line)
    c-=1
# for i in range(N-1):
#     a = input()
#     line = a.split(',')
#     b.append(line)

for i in range(N):
    for j in range(i + 1):
        print(b[i][j], end='')
        
        if i != j:
            print(',', end='')
            
    for k in range(i, -1, -1):
        if (k != i):
            print(b[k][i], end='')
            
        if i > 0 and k > 0:
            print(',', end='')
        
    print()
    