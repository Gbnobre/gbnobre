# minhas variaveis

preço = float(input('Qual o preço do produto? '))
desconto = int(input('Quantos porcentos é seu desconto? '))

# formula de porcentagem
valor_desconto = (desconto * preço / 100) 
preço_com_desconto = (preço - valor_desconto )
 
print('seu produto custa R${} com o desconto de {}% o preço fica R${}'.format(preço, desconto, preço_com_desconto))