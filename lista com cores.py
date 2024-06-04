# Criamos a variavel "lista" e adicinamos algumas palavras dentro da lista.
print()
print('\033[033m 1. Criamos uma lista e enumeramos ela de acordo com a posição de seus itens\033[0m')

lista = ['arroz','feijão','salada','macarrão']

# criamos um for e adicianamos 2 variaveis "numero" e "item" com a funçao enumarete numero = indice da lista e item = os itens da lista 
print('\033[035m')
for numero, item in enumerate(lista):

   print(f'                                        {numero} {item}')

print()
# Para buscar apenas um item na lista usamos o nome da variavel que criou a lista e buscamos o numero do indece dentro do []
print('\033[033m 2. Aqui buscamos um item na lista de acordo com sua posição que no caso foi o 3° item \033[0m')
print('\033[034m')

print('                                        ',lista[2])

# Tambem podemos usar a numeraçao negativa para buscar a ordem inversa
print()
print('\033[033m 3. Aqui também buscamos um item na lista de acordo com sua posição mas dessa vez usando a numeração negativa que busca a ordem inversa que foi o 1° item \033[0m')
print('\033[031m')

print('                                        ',lista[-4])

print()
# adicionando item no final da lista com o .append"
print('\033[033m 4. Adiconamos o item "laranja" no final da lista \033[0m')
print('\033[032m')

lista.append('laranja')
print(lista)

print()
# Removendo item na lista com base na posição indicada com o del
print('\033[033m 5. Retiramos o item "arroz" de acordo com sua posiçao na lista que no caso foi 0 \033[0m')
print('\033[034m')

del lista [0]

print(lista)
print()

# Adicinando item na lista com base na posiçao indicada com o .insert
print('\033[033m 6. Adicionamos o item "cebola" na posiçao 3 da lista \033[0m ')
print('\033[035m')

lista.insert(3,'cebola')
print(lista)
print('\033[0m')

# Removendo item com base no nome e não na posição com .remove
print('\033[033m 7. Removemos o item "macarrão" de acordo com seu nome \033[0m')
print('\033[036m')

lista.remove('macarrão')
print(lista)
print('\033[0m')

# É comum que as listas se iniciem sem nenhum valor. Como se fosse um papel em branco que gradualmente você adiciona informações.
# Para criarmos vamos usar novamente o colchetes, mas sem nenhum item:
print('\033[33m 8. Criamos uma lista sem itens. Depois retiramos o item 0 da primeira lista e armazenamos dentro da variavel item  \033[0m')

lista_nova = []

# Utilizando .pop(), iremos remover o último item da lista, mas sem excluí-lo.
# Nesse caso, o valor carro será armazenado na variável item:
print('\033[032m')
item = lista.pop(0)
print('item =', item)
print()

# Após retirar da lista, adicionamos ‘carro’ na nossa lista_nova:
print('\033[033m Agora adicionamos na lista nova a variavel que contem "o item 0" \033[0m')


lista_nova.append(item)
print('\033[035m')
print('lista nova >', lista_nova)
print('\033[032m')
print('primeira lista atualizada >', lista)
print('\033[0m')

print('\033[33m Primeira lista')
print('\033[034m')
for numero1, item1 in enumerate(lista):
    print(f'{numero1} {item1}')
print()

print('\033[033m Segunda lista')
print('\033[036m')
for numero2, item2 in enumerate(lista_nova):
    print(f'{numero2} {item2}')
print('\033[0m')


print('{}Olá, Mundo{}'.format('\033[4;34m', '\033[m'))
