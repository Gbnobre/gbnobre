print('\033[1;37m')
minutos = int(input('\t\t\t\t\t\tDigite quantos minutos foram gastos de internet:\n\n\t\t\t\t\t\t\t\t   > '))
print('\033[1;32m')

if minutos < 200:
    net1 = minutos * 0.20
    print(' '*60, 'O valor da sua conta é:\n\n\t\t\t\t\t\t\t\t   R$', net1)
elif minutos > 199 and minutos < 401:
    net2 = minutos * 0.18
    print(' '*60, 'O valor da sua conta é:\n\n\t\t\t\t\t\t\t\t   R$', net2)
elif minutos > 400:
    net3 = minutos * 0.15
    print(' '*60, 'O valor da sua conta é:\n\n\t\t\t\t\t\t\t\t   R$', net3)
print('\033[44m')

