import datetime

def validate_day(month, day):
    if month == 2:
        year = datetime.datetime.now().year
        if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    return True

print('Olá. Esse programa calcula sua idade atual.')

while True:
    try:
        yearBirth = int(input('Para começar, digite o ano em que nasceu usando 4 digitos: '))
        if len(str(yearBirth)) != 4:
            raise ValueError('O ano deve conter 4 digitos.')
        monthBirth = int(input('Agora, digite o mês de nascimento (1-12): '))
        if monthBirth < 1 or monthBirth > 12:
            raise ValueError('O mês deve ser entre 1 a 12.')
        dayBirth = int(input('Por último, digite o dia do seu nascimento (1-31): '))
        if not validate_day(monthBirth, dayBirth):
            raise ValueError(f'O dia {dayBirth} não é válido para o mês {monthBirth}.')        
        break
    except ValueError as e:
        print(f'Erro: {e}. Insira novamente.')
current_date = datetime.datetime.now()
age = current_date.year - yearBirth
if (current_date.month, current_date.day) < (monthBirth, dayBirth):
    age -= 1

print(f'Sua idade atual é {age} anos.')