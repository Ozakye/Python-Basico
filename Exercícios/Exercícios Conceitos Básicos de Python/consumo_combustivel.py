print('Olá. Este programa calcula o consumo médio de combustível em km/l')

while True:
  try:
    fuel_consumed = float(input('Digite a quantidade de combustível consumido em litros: '))
    if fuel_consumed <= 0:
      print('Insira um número positivo para o combustível.')
      continue
    break
  except ValueError:
    print('Insira um número válido.')

while True:
  try:
    distance_travelled = float(input('Digite a distância percorrida em km: '))
    if distance_travelled <= 0:
      print('Insira um número positivo para a distância.')
      continue
    break
  except ValueError:
    print('Insira um número válido.')

average_consumption = distance_travelled / fuel_consumed

print(f'O consumo médio é de {average_consumption:.2f} km/l')