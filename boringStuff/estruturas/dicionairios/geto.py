libertadores = {'flamengo': 3, 'vasco': 1, 'trikas': 3, 'internacional':2}
print('O flamengo tem ' + str(libertadores.get('flamengo', 0))+ ' libertadores')
print('O fluminense tem ' + str(libertadores.get('fluminense', 0))+ ' libertadores')#caso não esteja no dicionario se retorna o valor padrão definido