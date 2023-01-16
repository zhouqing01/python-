# class Pushpull:
#     def __init__(self,i,count = 0):
#         self.i = i
#         self.count = count
#         self.str = '1'

#     def __str__(self):
#         # if self.i < 0:
#         #     return '<' + Pushpull.i + '<'
#         # if self.i > 0:
#         #     return ('>' + self.i + '>')
#         # if self.i == 0:
#         #     return ('<' + self.i + '>')
#         print(1)
#         return self.str
    
#     def push(self,i):
#         print(3)
#         return self.count + i

#     def pull(self, idx):
#         print(4)
#         return self.count - idx

#     def __iter__(self):
#         print(2)
#         return iter(self.str)


class Pushpull:
    count = 0

    def __init__(self, p=0):
        Pushpull.count = p

    def __str__(self):
        if self.count > 0:
            return f">{self.count}>"
        elif self.count < 0:
            return f"<{-self.count}<"
        return f"<{self.count}>"

    @staticmethod
    def push(n=1):
        Pushpull.count += n

    @staticmethod
    def pull(n=1):
        Pushpull.count -= n

    def __iter__(self):
        a = []
        if self.count > 0:
            return iter(list(range(0, self.count)))
        else:
            for i in range(0, -self.count):
                a.append(-i)

            return iter(a)
    

# a = Pushpull(-10)
# print(a)
# b, c = Pushpull(7), Pushpull(5)
# print(b)
# for i in b:
#     c.pull()
# print(a)
# b.push(3)
# t = tuple(c)
# a.pull(7)
# t += tuple(b)
# print(*t)

