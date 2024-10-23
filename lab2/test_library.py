import pytest
from library import fibonacci, bubble_sort, calculator


# Тесты для функции fibonacci
def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

    # Граничные значения
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-5)


# Тесты для функции bubble_sort
def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([-1, 0, 1]) == [-1, 0, 1]

    # Тестирование пустого списка
    assert bubble_sort([]) == []

    # Некорректные данные
    with pytest.raises(TypeError):
        bubble_sort("not a list")


# Тесты для функции calculator
def test_calculator():
    assert calculator(1, 2, '+') == 3
    assert calculator(5, 3, '-') == 2
    assert calculator(2, 3, '*') == 6
    assert calculator(10, 2, '/') == 5

    # Граничные значения
    with pytest.raises(ZeroDivisionError):
        calculator(10, 0, '/')

    # Некорректные операции
    with pytest.raises(ValueError):
        calculator(10, 2, '%')
