import sys
import tarfile
from io import BytesIO

s = bytes.fromhex(''.join(sys.stdin.read().replace(' ', '').split('\n')))
bts = BytesIO(s)
file = tarfile.open(fileobj=bts)
list = []
for i in file.getmembers():
    list.append(i)
res = []
for i in range(len(list)):
    if list[i].isfile():
        res.append(list[i])
print(sum(map(lambda x: x.size, res)), len(res))