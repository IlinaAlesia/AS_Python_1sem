# 4 вариант Ильина
def Transp(A):
    M = len(A)
    return [[A[j][i] for j in range(M)] for i in range(M)]
# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = Transp(matrix)
for row in result:
    print(row)
