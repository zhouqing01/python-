s = input()

a = s.split('+')[0]
b = s.split('+')[1].split('=')[0]
c = s.split('=')[1]

alphabet = ''.join(list(dict.fromkeys(a+b+c)))
digits = '1234567890'


def Replace(a, b):
    maxlen = max(len(a), len(b))
    i = 0
    while i < maxlen:
        if i < len(a) and a[-i-1].isalpha():
            return a[-i-1], i+1
        if i < len(b) and b[-i-1].isalpha():
            return b[-i-1], i+1
        i+=1
    return 'None', -1


def Rebus(a, b, c, letters, digits):
    answer = []
    if not letters:
        if int(a) + int(b) != int(c):
            return []
        return [a + '+' + b + '=' + c]
    new_a, new_b = Replace(a, b)
    if new_a == 'None':
        changedDigit = str((int(a) + int(b)) // 10**(len(c)-1))
        if changedDigit not in digits:
            return []
        if int(a) + int(b) != int(changedDigit + c[1:]):
            return []
        return [a + '+' + b + '=' + changedDigit + c[1:]]

    for j in range(len(digits)):
        aNew = a.replace(new_a, digits[j]) 
        bNew = b.replace(new_a, digits[j])
        cNew = c.replace(new_a, digits[j])
        lettersNew = letters.replace(new_a, '')
        if (new_b <= len(a) and aNew[-new_b].isalpha()) or (new_b <= len(b) and bNew[-new_b].isalpha()):
            answer += Rebus(aNew, bNew, cNew, lettersNew, digits[:j] + digits[j+1:])
            continue
        if '0' in [aNew[0], bNew[0], cNew[0]]:
            continue
        
        if cNew[-new_b].isdigit():
            if (int(aNew[-min(new_b, len(a)):]) + int(bNew[-min(new_b, len(b)):])) % 10**new_b != int(cNew[-min(new_b, len(c)):]):
                continue
            answer += Rebus(aNew, bNew, cNew, lettersNew, digits[:j] + digits[j+1:])
            continue
        changedDigit = str((int(aNew[-min(new_b, len(a)):]) + int(bNew[-min(new_b, len(b)):])) % 10**new_b // 10**(new_b-1))
        if changedDigit not in digits[:j]+digits[j+1:]:
            continue
        aNew = aNew.replace(c[-new_b], changedDigit)
        bNew = bNew.replace(c[-new_b], changedDigit)
        cNew = cNew.replace(c[-new_b], changedDigit)
        lettersNew = lettersNew.replace(c[-new_b], '')
        digitsNew = (digits[:j] + digits[j+1:]).replace(changedDigit, '')
        answer += Rebus(aNew, bNew, cNew, lettersNew, digitsNew)
    return answer

solutions = Rebus(a, b, c, alphabet, digits)
solutions.sort()
for solution in solutions:
    print(solution)
