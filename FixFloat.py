# from sys import stdin


def fix(n):
    def wrapped(func):
        def inner(*args, **kwargs):

            args = list(args)
            for i, v in enumerate(args):
                if isinstance(v, float):
                    args[i] = round(v, n)

            for k, v in kwargs.items():
                if isinstance(v, float):
                    kwargs[k] = round(v, n)

            res = func(*args, **kwargs)
            if isinstance(res, float):
                res = round(res, n)
            return res

        return inner

    return wrapped


# if __name__ == '__main__':
#     exec(stdin.read())

# @fix(4)
# def aver(*args, sign=1):
#     return sum(args)*sign

# print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))
