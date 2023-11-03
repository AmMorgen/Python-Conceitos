
#A nossa funcao recebe uma lista e o elemento a ser procurado
def busca(lista, elem):
    """retorna o indice de um elemento na lista ou none, caso o contrario"""
    for i in range(len(lista)):#pecorre toda a lista  até encontrar a condicao 
        if lista[i] == elem:#caso o elemento for igual ao procurado ele retorna o indice
            return i
    return None #caso não exista elemento el retorna none
    
lista_exemplo=[2, 4, 3, 6, 5, 8, 7]
elemento = 3


indice = busca(lista_exemplo, elemento)
if indice is not None:#só exibe o elemento caso ele pertença a lista
    print("O indice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))