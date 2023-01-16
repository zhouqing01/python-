#Написать класс NegExt， расширяющий унарный минус по следующей схеме： Производный класс должен конструироваться с помощью class потомок（NegExt， родитель）： Если для родителя можно вызвать унарный минус, -потомок() возвращает то же, что и -родитель() Если для родителя унарный минус не работает, но работает операция секционирования, -потомок() возвращает собственную секцию [1:-1] В противном случае возвращается сам потомок Результат нужно преобразовать к типу потомка

class NegExt:

    def __neg__(self):
        try:
            return self.__class__(super().__neg__())
        except AttributeError:
            try:
                return self.__class__(super().__getitem__(slice(1, -1)))
            except Exception:
                return self.__class__(self)


# if __name__ == '__main__':
#     import sys
#     exec(sys.stdin.read())
class nstr(NegExt, str):
    pass
class nnum(NegExt, int):
    pass
class ndict(NegExt, dict):
    pass
print(-nstr("Python"), -nnum(123), -ndict({1: 2, 3: 4}), --nstr("NegExt"))