# Desafio: Verificador de Elegibilidade para Emprego
# Você deve criar um programa em Python que determine se uma pessoa é elegível para uma vaga de emprego com base na sua idade
# e na quantidade de anos de experiência.


# A elegibilidade é definida pelas seguintes regras:

# A pessoa deve ter pelo menos 18 anos.
# A pessoa deve ser brasileira
# A pessoa deve ter pelo menos 2 anos de experiência de trabalho.


# Objetivos:

# Solicitar ao usuário que insira sua idade.
# Solicitar ao usuário que insira sua nacionalidade.
# Solicitar ao usuário que insira seus anos de experiência.
# Imprimir uma mensagem indicando se a pessoa é elegível ou não.
print()
print(' '*55, 'Bem vindo ao Vaga de Empregos')
print()
nome = input('Digite seu nome para começar.\n')
print()
print(nome, 'agora iremnos coletar alguns dados para ver se seu perfil se encaixa com a vaga\n' )

idade = int(input('Quantos anos você tem?\n'))
print()
nacionalidade = input('Em qual o país  nasceu?\n')
print()
experiencia = int(input('Quantos anos de experiência tem na área?\n'))
print()

if idade > 17:
    if nacionalidade == 'Brasil' or 'BRASIL':
        if experiencia == 2 or experiencia > 2:
            print('Você esta eligivel para a vaga')
else:
    print('Tu nasceu para trabalhar no MC Donalds')