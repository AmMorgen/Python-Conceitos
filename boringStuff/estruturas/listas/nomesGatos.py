#exemplo de utilzação de  lista
catNames =[] #em python ao declarar uma lista vazia ela aloca o espaço dinamicamente
while True:
    print('entre com o nome do gato' + str(len(catNames)+1) + '(Apenas de enter ao final da lista): ')
    name = input()
    if name =='':
        break
    catNames = catNames + [name] #concatenação da lista
print("A lista com os nomes dos gatos: ")
for name in  catNames:
    print(' '+name)