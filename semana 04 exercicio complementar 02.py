def ordena(lista):
    fim = len(lista)
    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    return lista
    
def bolha(lista):
    fim = len(lista)
    for i in range(fim - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenada(lista):
    ordenado = True
    for ind in range(len(lista) - 1):
        if lista[ind] > lista[ind + 1]:
            ordenado = False
    return ordenado

from random import randint

lista = []
lista_ordenada_selection = []
lista_ordenada_bolha = []

for i in range(1000):
    lista.append(randint(0,1000))

lista_ordenada_selection, lista_ordenada_bolha = lista.copy(), lista.copy()

def test_estaordenado():
    ordena(lista_ordenada_selection)
    assert ordenada(lista_ordenada_selection) == True

def test_naoestaordando():
    assert ordenada(lista) == False
    
def test_bolha():
    bolha(lista_ordenada_bolha)
    assert ordenada(lista_ordenada_bolha) == True

