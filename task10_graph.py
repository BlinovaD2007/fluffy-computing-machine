print('задача 1')
from itertools import permutations
table = '457 567 45 136 123 247 126'.split()
graph = 'EF FA AB BG GE EC CB CD DF DA'.split()
print(*range(1,8))
for p in permutations('ABCDEFG'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print('задача 2')
from itertools import permutations
table = '234 157 147 138 268 58 23 456'.split()
graph = 'DG GF GA AF FH HC CB BD BE EH ED'.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)


print('задача 3')
from itertools import permutations
table = '268 134678 257 27 38 12 234 125'.split()
graph = 'АГ ГБ БД ДИ ИЖ ЖЕ ЕВ ВГ ГД ГИ ГЕ'.split()
print(*range(1,9))
for p in permutations('АБВГДЕЖИ'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
         print(*p)

print('задача 4')
from itertools import permutations
table = '47 345 27 1267 268 458 134 56'.split()
graph = 'АБ БГ ГД ДЖ ДИ ИЖ ЖЕ ЕГ ЕВ ВА АГ'.split()
print(*range(1,9))
for p in permutations('АБВГДЕЖИ'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
          print(*p)

print('задача 5')
from itertools import permutations
table = '23467 1356 12458 13 238 127 16 35'.split()
graph = 'AB BC BD CD DE DG GE GC GF EF GH HC CA'.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
          print(*p)

print('задача 6')
from itertools import permutations
table = '247 148 578 126 38 47 136 235'.split()
graph = 'AH AB BH HF FG FD DC CG CE EG EA '.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
          print(*p)


print('задача 7')
from itertools import permutations
table = '347 3456 1245 1237 236 25 14'.split()
graph = 'AB BC CA AD CD DE DF FG GE EF EC'.split()
print(*range(1,8))
for p in permutations('ABCDEFG'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
          print(*p)


print('задача 8')
from itertools import permutations
table = '279 13789 2578 57 3468 589 1234 2356 126'.split()
graph = 'БА АВ АГ АД ДГ ГВ ДЗ ЗК КЖ ЖБ ЖВ ВЕ ЕГ ЕЖ ЕЗ ЕК'.split()
print(*range(1,10))
for p in permutations('АБВГДЗЕКЖ'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
          print(*p)


print('задача 9')
from itertools import permutations
table = '457 37 267 1678 16 3458 12348 467'.split()
graph = 'АБ БД ДЕ ЕЗ ЗГ ГА АВ ВД ВЖ ЖД ЖГ ГВ ГЕ'.split()
print(*range(1,9))
for p in permutations('АБВГДЖЕЗ'):
    if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
          print(*p)