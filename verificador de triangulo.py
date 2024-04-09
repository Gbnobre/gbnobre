                # Minhas Variáveis 

a_b = float(input('Qual a medida do lado "A_B": '))
a_c = float(input('Qual a medida da lado "A_C": '))
b_c = float(input('Qual a medida da base "B_C": '))

                # Minhas Condições
if a_b == a_c and b_c == a_b :
    print('Sim é um triângulo do tipo "equilátero"')
elif a_b == a_c and b_c != a_b :
    print(' Sim é um triângulo do tipo "isósceles"')
elif a_b != a_c and b_c != a_b :
    print(' Sim é um triângulo do tipo "escaleno"')
else:
    print('Com essas medidas nao é possivel forma nenhum dos 3 tipos de triângulo')

                # FIM 
