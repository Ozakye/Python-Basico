def ask_number(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Por favor, insira um valor positivo.")
                continue
            return value
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

hourly_wage = ask_number("Digite quanto você ganha por hora: R$ ")
hours_worked = ask_number("Digite o número de horas trabalhadas no mês: ")

salary = hourly_wage * hours_worked

print(f"Seu salário no mês é: R$ {salary:.2f}")