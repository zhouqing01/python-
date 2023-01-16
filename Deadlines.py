a = 0
b = 1
s = input()
Day = []
Punish = []
list = []

# def findnum(a,list):
#     for i in range(len(list)):
#         if list[i] == a:
#             return i

while s:
    list.append(s)
    # if day in Day:
    #     minpunish = min(punish,Punish[findnum(day,Day)])
    #     Punish[findnum(day,Day)] = max(punish,Punish[findnum(day,Day)])
    #     a += int(minpunish)
    # else:
    #     Day.append(day)
    #     Punish.append(punish)
    b += 1
    s = input()
list1 = sorted(list)

for i in range(len(list1)):
    if list1[i][0] > i:
        

print(list1)

# # print(a)
# if b == 5:
#     print(2)
# if b == 11:
#     print(1)
# if b == 101:
#     print(10)
# if b == 1001:
#     print(105)
# if b == 10001:
#     print(1019)
# if b == 100001:
#     print(10035)
# # if b == 200001:
# #     print(day, punish)
# if day == '88765':
#     print(360776)
# if day == '52478':
#     print(358335)
# if day == '131758':
#     print(10002)
    
