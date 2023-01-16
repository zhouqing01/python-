import itertools
import sys

alphabet = "!\"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ".encode("koi8-r")
cd = [
    'cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256',
    'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855',
    'cp864', 'cp866', 'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16',
    'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2'
]
b = sys.stdin.read().rstrip()
# t0 = time()
headtail = b[:4] + b[-4:]
if 'KM' in headtail or '×{´F' in headtail:
    b = b.split('%')
else:
    b = b.split('\n')
# print(b, 'saas')
# b = bytes.fromhex(b).decode().split('%')
# print(b)
# b = list(map(lambda x: x.decode('utf-8'), b))
# print(b)
if headtail == 'ПРОЦКНЦ;':
    print('\n'.join(b))
    sys.exit()

#   Кодировки длины 1
codes = dict()  # Список всех возможных последовательностей перекодировок длины 1
for i, j in itertools.permutations(cd, 2):

    try:
        val = alphabet.decode(i).encode(j)
        key = ((j, i),)
        codes[key] = val
        if headtail.encode(i).decode('koi8-r') == 'ПРОЦКНЦ;':
            for seq in b:
                print(seq.encode(i).decode('koi8-r'))
            sys.exit()
    except UnicodeDecodeError:
        continue
    except UnicodeEncodeError as E:
        continue

codes1 = dict()
for el, value in codes.items():
    for i, j in itertools.permutations(cd, 2):
        if el[0][0] == i:
            continue

        try:
            val = value.decode(i).encode(j)
            key = ((j, i),) + el
            codes1[key] = val
            if headtail.encode(i).decode(el[0][0]).encode(el[0][1]).decode('koi8-r') == 'ПРОЦКНЦ;':
                for seq in b:
                    print(seq.encode(i).decode(el[0][0]).encode(el[0][1]).decode('koi8-r'))
                sys.exit()
        except UnicodeDecodeError:
            continue
        except UnicodeEncodeError:
            continue

for el, value in codes1.items():
    for i, j in itertools.permutations(cd, 2):
        if el[0][0] == i:
            continue

        try:
            val = value.decode(i).encode(j)
            key = el + ((i, j),)
            ((v1, v2), (v3, v4)) = el
            if headtail.encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode('koi8-r') == 'ПРОЦКНЦ;':
                for num in range(len(b)):
                    b[num] = b[num].encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode('koi8-r')
                print('\n'.join(b))
                # print(time() - t0)
                sys.exit()
        except UnicodeDecodeError:
            continue
        except UnicodeEncodeError:
            continue
