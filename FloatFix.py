import numbers


def de(fun, arg):
    def new_f(*args, **kwargs):
        res = fun(*args, **kwargs)
        return round(res, arg) if isinstance(res, numbers.Real) else res
    return new_f


class fixed(type):
    def __init__(cls, name, parents, ns, **kwds):
        return super().__init__(name, parents, ns)


    @staticmethod
    def __new__(metacls, name, parents, ns, ndigits=3):
        for i, j in ns.items():
            if callable(j):
                ns[i] = de(j, ndigits)
        return super().__new__(metacls, name, parents, ns)

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return super().__prepare__(name, bases)


