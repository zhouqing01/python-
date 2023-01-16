a = input()
b=[]
c = 0
max = 0
lenlist = 0
while a != '0':
    if a == '-0':
        break
    else:
        a=int(a)
        if a>=c:
            b.append(a)
            lenlist += 1
            if lenlist>max:
                max = lenlist
        else:
            b.clear()
            b.append(a)
            lenlist = 1
        c = a

    a = input()

print(max)