convidados = { 'miguel' : {'banana', 'maca', 'pera'}, 'monica': {'bife', 'ovo', 'frango'}, 'marlon':{'suco', 'cafe', 'leite'}}

def itensTotal(convidados, item):
    numItem = 0
    for k, v in convidados.items():
        numItem = numItem + v.get(item, 0)
    return numItem
print('numero de coisas levadas:')
