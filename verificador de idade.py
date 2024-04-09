# Minhas variaveis

idade = int(input('Qual sua idade? '))

# Minhas condições

if idade < 13 :
    print('Sua idade é', idade,'então você é "criança"')
elif idade > 12 and idade < 18 :
    print('Sua idade é', idade,'então você é "adolecente"')
elif idade > 17 and idade < 60 :
    print('Sua idade é', idade,'então você é "adulto"')
else:
    print('Sua idade é', idade,'então você é "idoso"')