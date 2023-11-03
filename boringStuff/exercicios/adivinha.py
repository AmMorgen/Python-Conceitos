import random
numeroSecreto = random.randint(1, 10)
print("adivinhe um numero inteiro entre 1 e 20\n")
print("voce tem 3 tentativas:")
i = 0
for chanceAcerto in range(1,4):
    i +=1
    print('use sua {} tentativa'.format(i))
    tentativa = int(input())
    if tentativa < numeroSecreto:
        print("Sua escolha é menor que o numero secreto")
    elif tentativa > numeroSecreto:
        print("Sua escolhe é maior que o numero secreto")
    else:
        break #aqui garante que foi a escolha correta e sai do loop

if tentativa == numeroSecreto:
    print("parabens voce acertou o numero secreto")
else:
    print("Não foi dessa vez!! O numero secreto era {}".format(numeroSecreto))