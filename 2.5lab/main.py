call_count = 0

def FibRec(N):
    global call_count
    call_count += 1
    
    if N == 1 or N == 2:
        return 1
    return FibRec(N - 2) + FibRec(N - 1)

# Находим 5 чисел Фибоначчи
numbers = [5, 7, 10, 12, 15]
results = []

for n in numbers:
    call_count = 0
    fib_num = FibRec(n)
    results.append((n, fib_num, call_count))

# Вывод результатов
for n, fib, calls in results:
    print(f"F({n}) = {fib}, рекурсивных вызовов: {calls}")
