                # INICIO E VARIÁVEIS

print('                     CONVERSOR DE MILHAS, POLEGADAS, PES, CENTIMETROS, METROS OU kILOMETROS')
print('')
print('')
valor = float(input('O valor da sua medida é: '))
medida1 = str(input('A medida que quer converte é: '))
medida2 = str(input("Para à medida: "))

            
               # MINHAS MEDIDAS MILHAS
milhas_polegadas = valor * 63360
milhas_pes = valor * 5280
milhas_centimetros = valor * 160934
milhas_metros = valor * 1609.34
milhas_kilometros = valor * 1.60934

               # MINHAS MEDIDAS POLEGADAS
polegadas_milhas = valor * 1.57828e-5
polegadas_pes = valor * 0.0833333
polegadas_centimetros = valor * 2.54
polegadas_metros = valor * 0.0254
polegadas_kilometros = valor * 2.54e-5


               # MINHAS MEDIDAS PES
pes_milhas = valor * 0.000189394
pes_polegadas = valor * 12
pes_centimetros = valor * 30.48
pes_metros = valor * 0.3048
pes_kilometros = valor * 0.0003048

             # MINHAS MEDIDAS CENTIMETROS
centimetros_milhas = v = valor * 6.21371e-6 
centimetros_polegadas = valor * 0.393701
centimetros_pes = valor * 0.0328084
centimetros_metros = valor * 0.01
centimetros_kilometros = valor *  0.00001
            
                      # MINHAS MEDIDAS METROS
metros_milhas = valor * 0.000621371
metros_polegadas = valor * 39.3701
metros_pes = valor * 3.28084
metros_centimetros = valor * 100
metros_kilometros = valor *  0.001

                      # MINHAS MEDIDAS METROS
kilometros_milhas = valor * 0.621371
kilometros_polegadas = valor * 39370.1
kilometros_pes = valor * 3280.84
kilometros_centimetros = valor * 100000
kilometros_metros = valor * 1000

                # MINHAS CONDIÇÕES

                # MILHAS
if medida1 == 'milhas' and medida2 == 'polegadas' :
    print(valor, medida1, ' é igual a', milhas_polegadas, medida2)
elif medida1 == 'milhas' and medida2 == 'pes' :
    print(valor, medida1, 'é igual a', milhas_pes, medida2)
elif medida1 == 'milhas' and medida2 == 'centimetros' :
    print(valor, medida1, 'é igual a', milhas_centimetros, medida2)    
elif medida1 == 'milhas' and medida2 == 'metros' : 
    print(valor, medida1, 'é igual a', milhas_metros, medida2)
elif medida1 == 'milhas' and medida2 == 'kilometros' :
     print(valor, medida1, 'é igual a', milhas_kilometros, medida2)
                # POLEGADAS     
elif  medida1 == 'polegadas' and medida2 == 'milhas' :
    print(valor, medida1, 'é igual a', polegadas_milhas, medida2)
elif  medida1 == 'polegadas' and medida2 == 'pes' :
    print(valor, medida1, 'é igual a', polegadas_pes, medida2)
elif  medida1 == 'polegadas' and medida2 == 'centimetros' :
    print(valor, medida1, 'é igual a', polegadas_centimetros, medida2)
elif  medida1 == 'polegadas' and medida2 == 'metros' :
    print(valor, medida1, 'é igual a', polegadas_metros, medida2)
elif  medida1 == 'polegadas' and medida2 == 'kilometros' :
    print(valor, medida1, 'é igual a', polegadas_kilometros, medida2)
               # PES
elif  medida1 == 'pes' and medida2 == 'milhas' :
    print(valor, medida1, 'é igual a', pes_milhas, medida2)
elif  medida1 == 'pes' and medida2 == 'polegdas' :
    print(valor, medida1, 'é igual a', pes_polegada, medida2)
elif  medida1 == 'pes' and medida2 == 'centimetros' :
    print(valor, medida1, 'é igual a', pes_centimetros, medida2)
elif  medida1 == 'pes' and medida2 == 'metros' :
    print(valor, medida1, 'é igual a', pes_metros, medida2)
elif  medida1 == 'pes' and medida2 == 'kilometros' :
    print(valor, medida1, 'é igual a', pes_kilometros, medida2)
               # CENTIMETROS
elif  medida1 == 'centimetros' and medida2 == 'milhas' :
    print(valor, medida1, 'é igual a', centimetros_milhas, medida2)
elif  medida1 == 'centimetros' and medida2 == 'polegdas' :
    print(valor, medida1, 'é igual a', centimetros_polegadas, medida2)
elif  medida1 == 'centimetros' and medida2 == 'pes' :
    print(valor, medida1, 'é igual a', centimetros_pes, medida2)
elif  medida1 == 'centimetros' and medida2 == 'metros' :
    print(valor, medida1, 'é igual a', centimetros_metros, medida2)
elif  medida1 == 'centimetros' and medida2 == 'kilometros' :
    print(valor, medida1, 'é igual a', centimetros_kilometros, medida2)
       # METROS
elif  medida1 == 'metros' and medida2 == 'milhas' :
    print(valor, medida1, 'é igual a', metros_milhas, medida2)
elif  medida1 == 'metros' and medida2 == 'polegdas' :
    print(valor, medida1, 'é igual a', metros_polegadas, medida2)
elif  medida1 == 'metros' and medida2 == 'pes' :
    print(valor, medida1, 'é igual a', metros_pes, medida2)
elif  medida1 == 'metros' and medida2 == 'centimetros' :
    print(valor, medida1, 'é igual a', metros_centimetros, medida2)
elif  medida1 == 'metros' and medida2 == 'kilometros' :
    print(valor, medida1, 'é igual a', metros_kilometros, medida2)
       # KILOMETROS
elif  medida1 == 'kilometros' and medida2 == 'milhas' :
    print(valor, medida1, 'é igual a', kilometros_milhas, medida2)
elif  medida1 == 'kilometros' and medida2 == 'polegdas' :
    print(valor, medida1, 'é igual a', kilometros_polegadas, medida2)
elif  medida1 == 'kilometros' and medida2 == 'pes' :
    print(valor, medida1, 'é igual a', kilometros_pes, medida2)
elif  medida1 == 'kilometros' and medida2 == 'centimetros' :
    print(valor, medida1, 'é igual a', kilometros_centimetros, medida2)
elif  medida1 == 'kilometros' and medida2 == 'metros' :
    print(valor, medida1, 'é igual a', kilometros_metros, medida2)
else:
    print('digite o nome da medida certa, MILHAS, "POLEGADAS, PES, CENTIMETROS, METROS OU KILOMETROS" com letra minúscula')