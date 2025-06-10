def intro():
    print('Olá, esta é uma calculadora simples. Para começar digite dois números: ')

def numberA():
    while True:
        try:
            a = float(input('Digite o primeiro número (a): '))
            return a
        except ValueError:
            print('O valor inserido não é um número. Digite um número.')

def numberB():
    while True:
        try:
            b = float(input('Digite o segundo número (b): '))
            return b
        except ValueError:
            print('O valor inserido não é um número. Digite um número.')

def newNumbers():
    while True:
        try:
            a = float(input('Digite um novo número para (a): '))
            break
        except ValueError:
            print('O valor inserido não é um número. Digite um número.')
    
    while True:
        try:
            b = float(input('Digite um novo número para (b): '))
            break
        except ValueError:
            print('O valor inserido não é um número. Digite um número.')

    print(f'Seus números são: a = {a} e b = {b}')
    return a, b

def continueMath():
    while True:
        try:
            print('Deseja realizar outra operação?')
            continueInput = input('s - Sim / n - Não').lower()
            if continueInput == 's':
                return True
            elif continueInput == 'n':
                print('Saindo...')
                return False
        except ValueError:
            print('O valor inserido não é uma opção. Digite "s" para sim ou "n" para não.')

def menu():
        print('\nEscolha a operação desejada:')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Alterar números')
        print('6 - Sair')

def addition(a, b):
    return (a + b)

def subtraction(a, b):
    return (a - b)

def multiplication(a, b):
    return (a * b)

def division(a, b):
    if b == 0:
        return 'Não é possível dividir por 0'
    return (a / b)

intro();
a = numberA()
b = numberB()
print(f'Seus números são: a = {a} e b = {b}')

while True:
    try:
        menu()
        choice = int(input('Digite o número da sua escolha: '))

        if choice == 6:
            print('Saindo...')
            break
        elif choice == 5:
            a, b = newNumbers()
        elif choice == 4:
            result = division(a, b)
            print(f"O resultado da divisão de {a} / {b} é: {result}")
        elif choice == 3:
            result = multiplication(a, b)
            print(f"O resultado da multiplicação de {a} * {b} é: {result}")
        elif choice == 2:
            result = subtraction(a, b)
            print(f"O resultado da subtração de {a} - {b} é: {result}")
        elif choice == 1:
            result = addition(a, b)
            print(f"O resultado da adição de {a} + {b} é: {result}")
        else:
            print('Opção inválida. Tente novamente.')
            continue
        if not continueMath():
            break
    except ValueError:
        print('O valor inserido não é um número válido. Digite um número entre as opções.')