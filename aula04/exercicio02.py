salario = float(input('Qual o seu salario? '))
total_vendas = float(input('Qual o valor das vendas? '))

if total_vendas >= 1000:
    premio = 150
    valor_final = salario + premio
    print(f'O seu bonus será de R${premio}')
    print(f'Seu salario + bonus por vendas será de R$ {valor_final:.2f}')

elif total_vendas >= 500:
    premio = 75
    valor_final = salario + premio
    print(f'O seu bonus será de R${premio:.2f}')
    print(f'Seu salario + bonus por vendas será de R$ {valor_final:.2f}')

else:
    print (f'Você não obteve bonus por vendas e seu salário será de {salario:.2f}')