# 6.3.py
def is_magic_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        last_two_digits = year % 100
        return day * month == last_two_digits
    except ValueError:
        return False

date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magic_date(date):
    print(f"{date} — магическая дата!")
else:
    print(f"{date} — не магическая дата.")
