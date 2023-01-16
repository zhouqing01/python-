import base64, sys


a = sys.stdin.buffer.read().strip()
a = base64.b85decode(a)
head = []
pos = 0
while el := int.from_bytes(a[pos:pos + 1], byteorder='big', signed=True):
    head.append(el)
    pos += 1
res = []
pos += 1
for j in range((len(a) - pos) // sum(map(abs, head))):
    for i in head:
        if i <= 0:
            res.append(int.from_bytes(a[pos: pos + abs(i)], byteorder='big', signed=True))
        else:
            res.append(int.from_bytes(a[pos: pos + abs(i)], byteorder='big', signed=False))
        pos += abs(i)

print(sum(res))