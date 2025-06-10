def ask_number(message):
  while True:
    try:
      value = float(input(message))
      if value <= 0:
        print("Por favor, insira um valor positivo.")
        continue
      break
    except ValueError:
      print("Por favor, insira um número válido.")
  return value

weight = ask_number('Digite o seu peso em kg: ')
height = ask_number('Digite a sua altura em metros: ')

bmi = weight / (height ** 2)

print(f"Seu IMC é: {bmi:.2f}")