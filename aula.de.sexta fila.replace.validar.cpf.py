# Fução para verificar CPF

def validar_cpf (cpf):
    # Tirando pontos, espaços, itens indesejados
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    
    # Conferindo se os digitos são iguais a 11 e se nãop contém letras
    if not cpf.isdigit() or len(cpf) !=11:
        print()
        print('\033[031m CPF são um conjunto de numeros de 11 digitos \033[0m')
        return False
    
    # Conferindo o primeiro digito verificador
    soma = 0
    peso = 10
    for i in range (9):
        soma += int (cpf[i]) * peso
        peso -= 1
    digito1 = 11 - (soma % 11) 
    if digito1 > 9:
        digito1 = 0
    if int (cpf[9]) != digito1:
        return False
    
    # Conferindo o segundo digito verificador
    soma = 0
    peso = 11
    for i in range (10):
        soma += int (cpf[i]) * peso
        peso -= 1
    digito2 = 11 - (soma % 11) 
    if digito2 > 9:
        digito2 = 0
    if int (cpf[10]) != digito2:
        return False
    return True

# Criando uma condição que rode enquanto o usuario nao colocar
# um cpf valido

controler = True
while controler:
    cpf = input('\033[033m Digite um cpf:\033[0m \n')
    if validar_cpf (cpf): 
        print()
        print(f'\033[032m O número de CPF {cpf} é valido! \033[0m')
        print()
        controler = False
    else:
        print()
        print('\033[031m CPF invalido! tente novamente \033[0m')
        print() 
        


# Exemplo de replace 

texto = 'o python é uma linguagem de programação muito poderosa e versátil. '

novo_texto = texto.replace('poderosa', 'incrivel')

print(novo_texto)

# Exemplo de fila

from typing import Deque, Any
from collections import deque
queue : Deque[Any] = deque([])

queue.append('a')
queue.append('b')

for item in queue:
    print(item)