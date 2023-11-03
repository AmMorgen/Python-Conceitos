lista=[2,4,3,4,5,7, 11,6]
print(lista)
def insertion(lista):
    tam = len(lista)
    for i in range(1, tam):
        chave = lista[i]
        j =i-1
        while j>=0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j-1
        lista[j+1]=chave

insertion(lista)
print(lista)