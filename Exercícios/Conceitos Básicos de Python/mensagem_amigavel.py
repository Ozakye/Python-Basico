def ask_for_input(message):
    return input(message)

name = ask_for_input("Qual é o seu nome? ")
age = ask_for_input("Quantos anos você tem? ")
city = ask_for_input("De onde você é? ")
profession = ask_for_input("Qual é a sua profissão? ")

print(f"Olá {name}, prazer em te conhecer! Você tem {age} anos e é de {city}.")
print(f"Eu também sou {profession} e estou muito feliz por nossa troca de ideias!")