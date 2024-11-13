import unittest
from lib import count_common_elements

# Функция для тестов
def count_common_elements(*lists):
    if not lists:
        return 0

    # Находим пересечение всех списков
    common_elements = set(lists[0])

    for lst in lists[1:]:
        common_elements &= set(lst)

    # Возвращаем количество одинаковых элементов
    return len(common_elements)

# Тесты
class TestCountCommonElements(unittest.TestCase):
    def test_common_elements(self):
        # Тест с несколькими списками
        self.assertEqual(count_common_elements([1, 2, 3], [2, 3, 4], [2, 3, 5]), 2)

    def test_no_common_elements(self):
        # Тест, когда нет общих элементов
        self.assertEqual(count_common_elements([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)

    def test_single_list(self):
        # Тест с одним списком
        self.assertEqual(count_common_elements([1, 2, 3]), 3)

    def test_empty_lists(self):
        # Тест с пустыми списками
        self.assertEqual(count_common_elements([], [], []), 0)

    def test_mixed_empty_and_non_empty(self):
        # Тест со смешанными пустыми и непустыми списками
        self.assertEqual(count_common_elements([1, 2], [], [2]), 0)

    def test_no_arguments(self):
        # Тест без аргументов
        self.assertEqual(count_common_elements(), 0)

    def test_all_identical_elements(self):
        # Тест, где все элементы одинаковы во всех списках
        self.assertEqual(count_common_elements([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()
