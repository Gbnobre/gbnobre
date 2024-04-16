import random

numero_aleatorio = random.randint(0,100)
inicio = 0

while inicio < 2:
    numero = int(input('Digite seu palpite: '))
    if numero < numero_aleatorio :
        print('aumente seu palpite')
    elif numero > numero_aleatorio :
        print('abaixe seu palpite')
    else:
        print('Você acertou ')
        break
print('O número mágico é ', numero_aleatorio)
