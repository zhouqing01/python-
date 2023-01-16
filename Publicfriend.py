from collections import defaultdict

person = defaultdict(set)
s = input()
while s != '0, 0':

    number, name = s.split(', ')
    person[number].add(name)
    name, number = s.split(', ')
    person[number].add(name)
    s = input()

a = len(person)
num1 = []
for number,name in person.items():
    len_num = len(name)
    if len_num == a-1:
        num1.append(int(number))

if num1 != []:
    # for num in sorted(num1):
    #     print(num)
    num1.sort()
    print(*num1,sep=' ')
else:
    print(' ')
