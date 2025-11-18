# 4 вариант Ильина
from itertools import permutations
# а) Проверка наличия ключей в словаре
d = {1: 2, 3: 4}
keys = [1, 3]
print(all(k in d for k in keys))

# б) Генерация комбинаций букв
d = {1: 'abc'}
key = 1
print([''.join(p) for p in permutations(d[key])])

# в) Замена значений на среднее
d = {1: [2, 3, 4], 3: [5, 6, 7], 5: [8, 9, 0]}
print({k: round(sum(v) / len(v), 1) for k, v in d.items()})
