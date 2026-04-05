# 6.2.py
def safe_divide_100(divisor):
    try:
        return 100 / divisor
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"
    except TypeError:
        return "Ошибка: неверный тип данных!"

try:
    user_input = input("Введите число, на которое разделить 100: ")
    num = float(user_input)
    result = safe_divide_100(num)
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: необходимо ввести число!")
