
tentativa = 0

while tentativa < 3:
     
     senha = input('Digite sua senha: ')

     if senha == '1234':
       print('Senha correta! acesso permitido.')
       break
     tentativa += 1
     
else:
    print('Muitas tentativas tente novamente mais tarde')

