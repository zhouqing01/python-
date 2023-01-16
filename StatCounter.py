
def statcounter():
    statcounter.a = {}
    func = yield statcounter.a

    while True:
        statcounter.a[func] = 0

        def wrapped(f):
            def inner(*args, **kwargs):
                statcounter.a[f] += 1
                return f(*args, **kwargs)

            return inner

        func = yield wrapped(func)
