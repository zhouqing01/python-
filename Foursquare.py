# import math

# res = set()

# n = int(input())
# b = math.ceil(n ** 0.5)
# for s in range(int(b/2),b + 1):
#     s_2 = s**2
#     for i in range(int(b/2)+1):
#         i_2 = i ** 2
#         for j in range(i, b + 1):
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

from math import sqrt

x = int(input())


ans = []
t = int(sqrt(x))
for i in range(t + 1):
    b = i * i
    for j in range(i, int(sqrt(x - b)) + 1):
        for k in range(j, int(sqrt(x - b - j * j)) + 1):
            for n in range(int(sqrt(x - b - j * j - k * k)), k - 1, -1):
                s = b + j * j + k * k + n * n
                if x == s:
                    if not sorted([i, j, k, n], key=lambda q: -q) in ans:
                        ans.append(sorted([i, j, k, n], key=lambda q: -q))
                    break
                elif s < x:
                    break
for arr in sorted(ans):
    print(*arr)




