def calculate_time(distance, speed):
  return distance/speed

popular_places = {
    'São Paulo - Rio de Janeiro': 430,
    'São Paulo - Minas Gerais': 590,
    'São Paulo - Porto Alegre': 1100,
    'São Paulo - Salvador': 1600
}

print('Bem-vindo ao calculador de tempo de viagem! Este programa permite calcular o tempo necessário para percorrer uma distância,')
print('considerando diferentes meios de transporte: avião, carro ou ônibus.')
print('Escolha a distância e o meio de transporte, e descubra quanto tempo você levaria!')
print('Escolha abaixo um local popular ou digite a distância:')
print('1. São Paulo - Rio de Janeiro (430 km)')
print('2. São Paulo - Minas Gerais (590 km)')
print('3. São Paulo - Porto Alegre (1100 km)')
print('4. São Paulo - Salvador (1600 km)')
print('5. Digite manualmente a distância')

while True:
  try:
    option = int(input('Digite a opção desejada: '))
    if option not in [1, 2, 3, 4, 5]:
      print('Opção inválida, escolha uma opção válida.')
      continue
    break
  except ValueError:
    print('Insira um número válido das opções.')

if option == 1:
  distance = popular_places['São Paulo - Rio de Janeiro']
  place = 'São Paulo - Rio de Janeiro'
elif option == 2:
  distance = popular_places['São Paulo - Minas Gerais']
  place = 'São Paulo - Minas Gerais'
elif option == 3:
  distance = popular_places['São Paulo - Porto Alegre']
  place = 'São Paulo - Porto Alegre'
elif option == 4:
  distance = popular_places['São Paulo - Salvador']
  place = 'São Paulo - Salvador'
elif option == 5:
  while True:
    try:
      distance = float(input('Digite a distância da viagem em km: '))
      if distance <= 0:
        print('Por favor, insira uma distância positiva.')
        continue
      break
    except ValueError:
      print('Por favor, insira um número válido.')
  place = f'Distância de {distance} km'

print(f"\nVocê escolheu a distância: {place}")
print("Escolha o meio de transporte para calcular o tempo de viagem:")
print("1. Avião (600 km/h)")
print("2. Carro (100 km/h)")
print("3. Ônibus (80 km/h)")

while True:
  try:
    transport_option = int(input('Digite o número do meio de transporte: '))
    if transport_option not in [1, 2, 3]:
      print('Opção inválida, por favor escolha entre 1, 2 ou 3.')
      continue
    break
  except ValueError:
    print('Por favor, insira um número válido.')

if transport_option == 1:
  speed = 600
  transport = 'Avião'
elif transport_option == 2:
  speed = 100
  transport = 'Carro'
elif transport_option == 3:
  speed = 80
  transport = 'Ônibus'

travel_time = calculate_time(distance, speed)

print(f'O tempo de viagem de {distance} km de {transport} é {travel_time:.2f} horas.')