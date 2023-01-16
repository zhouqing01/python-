# import math

# res = set()

# n = int(input())
# b = math.ceil(n ** 0.5)
# for s in range(int(b/2)+1):
#     s_2 = s**2
#     for i in range(s,int(b/2)+1):
#         i_2 = i ** 2
#         for j in range(i, b+1):
#             j_2 = j ** 2
#             k_2 = n - i_2 - j_2 - s_2
#             if k_2 >= 0:
#                 k = k_2 ** 0.5
#                 if math.floor(k) ** 2 + i_2 + j_2 + s_2 == n:
#                     res.add(tuple(sorted([s, i, j, math.floor(k)], reverse=True)))
#                 elif math.ceil(k) ** 2 + i_2 + j_2 + s_2 == n:
#                     res.add(tuple(sorted([s, i, j, math.ceil(k)], reverse=True)))


                   
# for elem in sorted(res):
#     print(' '.join(map(str, elem)))

from decimal import Decimal, getcontext

a = Decimal('0')
b = Decimal(0)
print(a==b)