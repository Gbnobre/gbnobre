# MINHAS VARIÁVEIS

numero = int(input('Digite um número: '))

# MINHAS CONDIÇÕES

if numero > 0 and numero % 2 == 0 and numero % 3 == 0 :
    print('O número é "positivo", é "par" e "multiplo de 3"')
elif numero > 0 and numero % 2 == 0 :
    print('O número é positivo e par')
elif numero > 0 and numero % 3 == 0 :
    print('O número é "positivo", e "mutiplo de 3"')
elif numero < 0 and numero % 2 != 0 :
    print('O número é "negativo" e "impar"')
elif numero == 0 :
    print('O número é zero')
else:
    print('O numnero não é par positivo, par multiplo de 3, negativo impar e nem zero')