meuGato = {'tamanho': 'grande', 'raca':'frajola', 'idade': 3}
#print(meuGato)
#print(meuGato['tamanho'])
teste = {'cor': 'vermelho', 'idade': 20, 'peso': 90.5}

for v in teste.values():#imprime o valores dos dicionarios
    print(v)
print("-----------------------\n")

for k in teste.keys():#imprime as chaves dos dicionario
    print(k)

print("----------------------")
for i in teste.items():#imprime cada item separadamente
    print(i)