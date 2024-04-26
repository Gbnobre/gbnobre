#lista = ['arroz', 'feijao', 'abacate', 'tomate']

#for item in lista:
    #print(item)

#for indicie, item in enumerate(lista):
    #print(f"na posição: {indicie} esta o item: {item}")

#numeros = [1, 2, 3, 4, 5]

#soma = 0

#indice = 0

#while indice < len (numeros):
    #soma += numeros [indice]
   # indice += 1

#print('A soma dos números na lista é:', soma)

#elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

#tem_duplicados = False

#contador = 0

#vermelho = '\033[32m' '\033[40m'

#while contador < len(elementos) and not tem_duplicados:
   # indice_interno = contador + 1
    #while indice_interno < len(elementos):
     #   if elementos[contador] == elementos[indice_interno]:
      #      tem_duplicados = True
       #     break
        #indice_interno += 1
    #contador += 1

#if tem_duplicados:
  #  print(vermelho, 'A lista contém elemntos duplicados.')
#else:
    #print('Todos os elementos na lista são unicos.')
#lista = [1 , 1, 2, 3, 4, 4, 4, 5, 5]

#lista_sem_duplicados = []

#indice = 0
#while indice < len (lista):
 #   if lista[indice] not in lista_sem_duplicados:
  #      lista_sem_duplicados.append(lista[indice])
   # indice += 1 
#print('A lista sem duplicados é:', lista_sem_duplicados)

## dicionario ##
#dicionario = {'nome': 'joão', 'idade': 30}

#dicionario['cidade'] = 'sao paulo'

#del dicionario['idade']

#dicionario.pop('nome')

#print(dicionario)
#print('idade:', dicionario['idade'])

#for chave, valor in dicionario.items():
 #   print(f'chaves: {chave} | valor: {valor}')

#chaves = dicionario.keys()
#print(chaves)

dicionario = {}