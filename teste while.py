import random

numero_magico = random.randint(0,5)
tentativa = 0

while tentativa < 3: 
    numero = input('Adivinhe o núemero mágico (0 a 100): ')

    if int(numero) == numero_magico:
       print('Você ganhou o numero mágico é', numero_magico)
       break
    tentativa += 1
else:
    print('Voce errou tente outra vez')