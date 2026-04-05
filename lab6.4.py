# 6.4.py
def is_lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    length = len(ticket_str)
    
    if length % 2 != 0:
        return False
    
    half = length // 2
    first_half = sum(int(digit) for digit in ticket_str[:half])
    second_half = sum(int(digit) for digit in ticket_str[half:])
    
    return first_half == second_half

ticket = input("Введите номер билета: ")
if is_lucky_ticket(ticket):
    print("Билет счастливый!")
else:
    print("Билет несчастливый.")
