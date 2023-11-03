aniversario = {'marlon': '30 setembro','miguel': '02 novembro', 'monica': '29 marco'}

while True:
    print("Entre com um nome (aperte enter para sair):")
    name = input()
    if name == '':
        break

    if name in aniversario:
        print(aniversario[name] + ' é o aniversario de '+ name)
    else:
        print('Eu não tenha informação do aniversario de '+name)
        print('qual é o aniversario dele?')
        bday = input()
        aniversario[name]= bday
        print('A database de aniversarios atualizada')