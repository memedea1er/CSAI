def fibonacci(n):
    """
    Возвращает список из n чисел Фибоначчи.
    :param n: Количество чисел в последовательности Фибоначчи
    :return: Список чисел Фибоначчи
    """
    if n <= 0:
        raise ValueError("Количество чисел должно быть положительным")

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


def bubble_sort(arr):
    """
    Возвращает отсортированную копию списка arr методом пузырька.
    :param arr: Список чисел
    :return: Отсортированный список
    """
    if not isinstance(arr, list):
        raise TypeError("Ожидается список чисел")

    n = len(arr)
    sorted_arr = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


def calculator(a, b, operation):
    """
    Выполняет арифметическое действие между двумя числами a и b.
    :param a: Первое число
    :param b: Второе число
    :param operation: Операция (+, -, *, /)
    :return: Результат операции
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b
    else:
        raise ValueError("Неверная операция")
