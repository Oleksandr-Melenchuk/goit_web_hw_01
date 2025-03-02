#Приймає вхідні данні та передає 1 аргумент як команду 2 та 3 як параметри
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Перевірка на валідність номеру
def correct_number(number):
    return number.lstrip('+').isdigit()