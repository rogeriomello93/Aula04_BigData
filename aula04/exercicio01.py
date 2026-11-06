valor_compra = float(input('Qual foi o valor da compra? '))

if valor_compra >250:
    desconto = valor_compra * .16
    valor_final = valor_compra - desconto
    print(f'Você obteve um desconto no valor de R$ {desconto:.2f} e o valor final da sua compra é de R${valor_final}')

else:
    print(f'O valor final da sua compra é de R${valor_compra:.2f}') 