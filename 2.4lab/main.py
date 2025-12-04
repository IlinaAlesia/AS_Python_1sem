# 4 вариант Ильина
# а)
def calculate(a, b, operation='add'):  
    if operation == 'add':  
        return a + b  
    elif operation == 'subtract':  
        return a - b  
    elif operation == 'multiply':  
        return a * b  
    elif operation == 'divide':  
        if b == 0:  
            raise ValueError("Деление на ноль невозможно")  
        return a / b  
    else:  
        raise ValueError("Неизвестная операция. Допустимые значения: 'add', 'subtract', 'multiply', 'divide'")
# б)
def transform_list(numbers, transform_function=None):  
    # Создаем копию исходного списка  
    result = numbers.copy()  
      
    # Если функция преобразования указана, применяем её к каждому элементу  
    if transform_function is not None:  
        result = [transform_function(x) for x in result]  
    return result  
# в)
def sum_positive_numbers(*args):  
    return sum(num for num in args if num > 0)
# г)
