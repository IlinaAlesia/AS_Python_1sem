def find_sum_of_min_max(filename='f'):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                for token in line.split():
                    try:
                        num = float(token)
                        numbers.append(num)
                    except ValueError:
                        continue
            
            if not numbers:
                return None
            
            min_val = min(numbers)
            max_val = max(numbers)
            return min_val + max_val
            
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return None
