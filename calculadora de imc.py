#Minhas variaveis

altura = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))
imc = peso / (altura ** altura)

#condiçoes para classificar o imc

if imc < 18.5: 
    print('seu imc e classicado como "Magreza"')
elif imc > 18.4 and imc < 25 :
    print('seu imc e classicado como "Saudável"')  
elif imc > 24.9 and imc < 30 :
    print('seu imc e classicado como "Sobrepeso"')
elif imc > 29 and imc < 35 :
    print('seu imc e classicado como "Obsidade grau 1"')
elif imc > 34 and imc < 40 :
    print('seu imc e classicado como "Obsidade grau 2" (severa)')
elif imc > 39 :
    print('seu imc e classicado como "Obsidade grau 3" (morbida)')
else:
    print('erro')
