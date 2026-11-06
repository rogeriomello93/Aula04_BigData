pontos = int(input('Informe sua pontuação: '))

if pontos >= 100:
    pontos = pontos + 10
    print(f'Excelente! Você obteve 10 pontos extras e agora tem {pontos} pontos! ')

if pontos >= 50:
    pontos = pontos + 5
    print(f'Parabens! Você obteve 5 pontos extra e agora tem {pontos} pontos! ')

else:
    print(f'Você não obteve nenhum ponto extra! Sua pontuação é de {pontos} pontos!')



# Caso nao use o elif, o programa vai executar duas vezes o comando if e vai somar duas vezes! 