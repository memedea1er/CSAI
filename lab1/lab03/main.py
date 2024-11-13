def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input("Введите количество чисел: "))

numbers = []
for _ in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

# Запрашиваем направление сортировки
while True:
    sort_order = input("Введите направление сортировки (возрастание/убывание): ").lower()
    if sort_order in ["возрастание", "убывание"]:
        break
    else:
        print("Неверный ввод. Пожалуйста, введите 'возрастание' или 'убывание'.")

ascending = sort_order == "возрастание"

bubble_sort(numbers, ascending)

print("Отсортированные числа:", numbers)
