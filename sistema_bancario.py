#criar o menu do projeto
menu = """ 
[d] = Depositar
[s] = Sacar
[e] = Extrato
[sa] = Sair
"""
saldo = 0
extrato = ''
contador = 0
valor = 0

while True:
    opcao = input(menu)
    if  opcao == 'd':
        try:
            valor  = float(input(f'Digite o valor do deposito: R$'))
            if valor >= 0:
                saldo+=valor
                extrato += f'Deposito: R${valor}'
                print(f'Deposto: R$ {valor}')
                print('\nDeposito realizado com suceso!\n')
            else:
                print('Erro: o valor invalido!')
        except ValueError:
            print('Erro: valor invalido!')
    elif opcao == 's':
            if contador < 3:    
                try:
                    valor = float(input(f'Digite o valor do saque: R$'))
                    if valor > 0 and valor <= saldo:
                        saldo-=valor
                        extrato += f'\nSaque: {valor}'
                        print('\nSaque realizado com suceso!\n')
                        contador+=1
                    else:
                        print('Erro: Valor invalido')
                except ValueError:
                    print('Erro: Valor invalido')        
            else:
                print('Quantidade de saques diários excedidos!')  
    elif opcao == 'e':
        print(extrato)
        print(f'Saldo: R$ {saldo}\n')

    elif opcao == 'sa':
        break
    else:
        print('Erro: Opção invalida!')     
