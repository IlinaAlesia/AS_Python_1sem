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
