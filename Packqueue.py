pack = []
new_package = eval(input())

for p in new_package:
    if isinstance(p, tuple):
        pack += p
        continue
    if len(pack) < p:
        break
    print(tuple(pack[:p]))
    pack = pack[p:]
