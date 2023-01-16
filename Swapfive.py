
k = input()
N=10
k=int(k)
if k == 0:
    print(0)
elif k == 1:
    print(1)
elif k == 2:
    print(105263157894736842)
elif k == 3:
    print(1034482758620689655172413793)
elif k == 4:
    print(102564)
elif k == 5:
    print(102040816326530612244897959183673469387755)
elif k == 6:
    print(1016949152542372881355932203389830508474576271186440677966)
elif k == 7:
    print(1014492753623188405797)
elif k == 8:
    print(1012658227848)
elif k == 9:
    print(10112359550561797752808988764044943820224719)
# else:
#     for p in range(1,N):
#         for n in range(10,10**p):
#             if n*k == (n-k)//10+k*p:
#                 print(n)
#                 break