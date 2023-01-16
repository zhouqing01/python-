s = input()
list = []
iter = 1
while s:
    list.append(s)
    s = input()
    iter += 1

# print(list)
list1 = sorted(list)
# print(list)
# print(list[0][1])
def compare(a,b):
    const = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            const += 1
        else:
            break
    return const

# print(compare(list[0],list[1]))

K = 0
for i in range(0,len(list1),2):
    K = max(compare(list1[i], list1[i+1]), K)

print(K)