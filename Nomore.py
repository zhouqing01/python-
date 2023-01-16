# def nomore(a):
#     b = []
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[j] <= a[i]:
#                 b.append(a[j])
                
#     return b

def nomore(a):
    for i in a:
        for j in a:
            if j <= i:
                yield j
                



# print([n % 13 for n in range(5,23,3)])
# print(*nomore([n % 13 for n in range(5,23,3)]))