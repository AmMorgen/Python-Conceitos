
lista = [1, 2, 3, 4]
print(lista)

def invert_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2
    for i in range(limite):
        aux = lista[i]
        lista[i] = lista[tamanho-i]
        lista[tamanho-i] = aux

invert_lista(lista)
print(lista)