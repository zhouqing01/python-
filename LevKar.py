from collections import defaultdict

text_1 = defaultdict(set)
text_2 = defaultdict(set)

s = input()
# list1 = []
j = 0

if s[0] == '.':
        a = s[1]
        b = s[2]
        c = s[3]
while s:
    list1 = s.split(' ')
    for i in list1:
        print(i)
        print(i[0])
        if i[0] == a:
            text_1[i].add(1)
            if '!' in i:
                text_1[i].add(1)

        if i[0] == b:
            text_2[i].add(1)
            if '!' in i:
                text_2[i].add(1)
            j+=1
    s = input()

text_1 = sorted(text_1,key= lambda x:x[1],reverse=True)

if j == 0:
    s_2 = '...'
    print(s_2)

print('Salves 2 - fills! 3')
