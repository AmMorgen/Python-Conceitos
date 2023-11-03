nome = 'miguel'
print(nome[0])#é possivel pegar cada letra como se fosse index qualquer de array
print(nome[0:2])#também é possivel fazer slice
for i in nome:
    print('***'+i+'***') 
novoNome = nome[0:6] + 'o bebe'#maneira de mudar uma string
print(novoNome)