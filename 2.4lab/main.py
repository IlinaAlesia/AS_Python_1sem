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
def common_keys(**kwargs):  
    # Если нет словарей, возвращаем пустой словарь  
    if not kwargs:  
        return {}  
      
    # Получаем список всех словарей  
    dicts = kwargs.values()  
      
    # Находим общие ключи во всех словарях  
    common = set(dicts.keys())  
    for d in dicts[1:]:  
        common.intersection_update(d.keys())  
      
    # Создаем результирующий словарь с общими ключами и значениями  
    result = {}  
    for key in common:  
        # Проверяем, что значения одинаковы во всех словарях  
        value = dicts[key]  
        if all(d[key] == value for d in dicts[1:]):  
            result[key] = value  
      
    return result
