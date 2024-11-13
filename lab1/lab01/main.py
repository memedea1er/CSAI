def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(f"НОД для чисел {num1} и {num2} = {euclid_gcd(num1, num2)}")