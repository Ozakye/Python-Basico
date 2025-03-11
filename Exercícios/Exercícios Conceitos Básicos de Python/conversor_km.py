# pip install pint
import pint

ureg = pint.UnitRegistry()

def menu(km_input):
    while True:
        print('Escolha a unidade para converter:')
        print('1. Metros')
        print('2. Centímetros')
        print('3. Milímetros')

        try:
            option = int(input('Digite a opção desejada: '))
            if option == 1:
                km = km_input * ureg.kilometer
                result = km.to(ureg.meter)
                unit = 'metros'
                break
            elif option == 2:
                km = km_input * ureg.kilometer
                result = km.to(ureg.centimeter)
                unit = 'centímetros'
                break
            elif option == 3:
                km = km_input * ureg.kilometer
                result = km.to(ureg.millimeter)
                unit = 'milímetros'
                break
            else:
                print('Erro: Por favor, insira uma opção válida.')
        except ValueError:
            print('Erro: Por favor insira um número das opções.')

    print(f'{km_input} quilômetros são {result} {unit}.')

print('Bem-vindo ao conversor de km.')

try:
    km_input = float(input('Digite a quantidade de quilômetros: '))
except ValueError:
    print('Erro: Por favor, insira um número válido.')
    exit()

menu(km_input)