# Minhas variáveis

capital = float(input('Qual o valor do seu investimento? '))
taxa = float(input('Qual a taxa de juros ao mês? '))
tempo = int(input('Quanto meses pretende deixar seu dinheiro rendendo? '))

# Fórmula da porcentagem da taxa

juros_ao_mes = (capital * taxa / 100)

# Fórmula do juros simples

total = (juros_ao_mes * tempo ) + capital  

print('Seu investimento foi de R${} com taxa de {}% ao mês no período de {} meses'.format(capital, taxa, tempo))
print('No final de {} meses o total de seu dinheiro será de R${}'.format(tempo, total))
