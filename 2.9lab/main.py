def read_matrices(filename):
    matrices = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if not lines[i].strip():
                i += 1
                continue
            
            try:
                m, n = map(int, lines[i].split())
            except:
                i += 1
                continue
            
            i += 1
            matrix = []
            for _ in range(m):
                if i >= len(lines):
                    break
                row = list(map(float, lines[i].split()[:n]))
                if len(row) == n:
                    matrix.append(row)
                i += 1
            
            if len(matrix) == m:
                matrices.append(matrix)
    return matrices

def matrices_equal(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if abs(m1[i][j] - m2[i][j]) > 1e-9:
                return False
    return True

def write_matrices(filename, matrices):
    with open(filename, 'w') as f:
        for matrix in matrices:
            m = len(matrix)
            n = len(matrix[0])
            f.write(f"{m} {n}\n")
            for row in matrix:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("\n")

# Основная программа
file1 = input("Введите имя первого файла: ")
file2 = input("Введите имя второго файла: ")

matrices1 = read_matrices(file1)
matrices2 = read_matrices(file2)

# Добавляем уникальные матрицы из первого файла во второй
for mat in matrices1:
    if not any(matrices_equal(mat, m) for m in matrices2):
        matrices2.append(mat)

write_matrices(file2, matrices2)

# Вывод содержимого файлов
print(f"\nСодержимое файла {file1}:")
print("=" * 40)
with open(file1, 'r') as f:
    print(f.read())

print(f"\nСодержимое файла {file2}:")
print("=" * 40)
with open(file2, 'r') as f:
    print(f.read())
