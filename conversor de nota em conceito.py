# Minhas variáveis

nota = float(input('digite sua nota para converte-la: '))

# Minhas condições

if nota > 8 and nota < 11 :
    print('Sua nota é "A"')
elif nota > 7.4 and nota < 9 :
    print('Sua nota é "B"')
elif nota > 5 and nota < 7.5 :
    print('Sua nota é "C"')
elif nota > 3 and nota < 6 :
    print('Sua nota é "D"')
elif nota == 0 and nota < 4 :
    print('Sua nota é "F"')
else :
    print('Digite uma nota de 0 a 10')

