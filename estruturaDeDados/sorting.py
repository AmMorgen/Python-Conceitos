
#procurar menor valor de uma lista

"""
Isso aqui não é exatamente uma ordenação. a ideia é comparar cada elemento da lista 
segurando um valor e trocando por um menor. começo pelo primeiro valor, comparo com o segundo
caso o segundo seja menor,eu troco os valores. ai compara o segundo com o terceiroe vou indo
até terminar a lista
"""
def menor_valor(lista):
    n = len(lista)
    minimo = lista[0]
    for i in range(n):
        if lista[i] < minimo:
            minimo = lista[i]
        
    return minimo


#selection sort

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

