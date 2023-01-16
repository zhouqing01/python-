from math import factorial
from decimal import Decimal, getcontext

def PiGen():
    getcontext().prec = 10000
    sum_vals = Decimal('0')
    k = 0
    mul_5 = 13591409
    deg_2 = 1
    dec_4 = Decimal(426880)
    dec_1 = Decimal(10005).sqrt()
    while True:
        
        value = Decimal(factorial(6*k)) * mul_5 / (Decimal(factorial(3*k)*(factorial(k)**3))*deg_2)
        sum_vals += value
        k += 1
        mul_5 += 545140134
        deg_2 *= -262537412640768000
        res = (dec_4 * dec_1) / sum_vals
        yield res
        


for i, p in enumerate(PiGen()):
    if i>120:
        break
print(str(p)[1400:1470])
