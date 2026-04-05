# 6.1.py
def is_divisible_by_three(num):
    return num % 3 == 0

number = int(input("Введите число: "))
if is_divisible_by_three(number):
    print(f"{number} делится на 3")
else:
    print(f"{number} не делится на 3")
