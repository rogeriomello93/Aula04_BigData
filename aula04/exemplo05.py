compra = float(input('Qual valor total da compra? '))
freq = input('Programa de fidelidade? [S/N]:  ')

if compra > 100 or freq == 'S':
    print('Cliente tem direito a brinde')

else:
    print('Sem brinde dessa vez')
