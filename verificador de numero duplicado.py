# Lista "elementos" 
elementos = [1, 2, 3, 4, 4, 5, 5, 6, 7, 9]

# Variavel booleano será a confirmação se tem duplicados. ficara true se tiver  
tem_duplicados = False

# Variavel contador para contar os numeros dentro da lista.
contador = 0

# Enquanto contador que é zero for menor que len (elementos) que é leitor da quantidade de itens dentro da lista no caso len é 10 
# e a variavel tem_duplicados não for true faça: 
while contador < len (elementos) and not tem_duplicados:

# Variavel indice_interno sera = a contador + 1
    indice_interno = contador + 1

# Enquanto indice_interno for menor que len (elementos) faça:   
    while indice_interno < len (elementos):

# Se elementos[contador] = elementos[indice_interno]
# A variavel tem duplicados sera verdadeira
        if elementos[contador] == elementos [indice_interno]:
            tem_duplicados = True

# Mostre qual numero foi duplicado primeiro na lista 
            print('\033[033m')
            print('o primeiro numero duplicado é ',elementos[contador])
            print('\033[0m')
# Pare o loop while
            break

# Caso não encontre loop while rode ate contador e indice-interno ser = a len da lista que é 10
        indice_interno += 1
    contador += 1

# Se tem_duplicados for verdadeiro print a menssagem se não print outra mensagem
if tem_duplicados:
    print('A lista contém duplicados')
else:
    print('A lista não contém duplicados')   

# Mostre os elementos na cor preta
print('\033[030m')
print(elementos)
print('\033[0m')