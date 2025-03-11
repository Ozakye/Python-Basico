def ask_for_number(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Por favor, insira um valor positivo.")
                continue
            return value
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

hours_per_week = ask_for_number("Digite o número de horas de exercício por semana: ")

minutes_per_week = hours_per_week * 60
calories_per_week = minutes_per_week * 5
calories_per_month = calories_per_week * 4

print(f"O total de calorias queimadas em um mês é: {calories_per_month:.0f} calorias.")