def ordenada(lista):
    ordenado = True
    for ind in range(len(lista) - 1):
        if lista[ind] > lista[ind + 1]:
            ordenado = False
    return ordenado

def test_desordenado():
    lista = [1, 3, 3, 2]
    assert ordenada(lista) == False

def test_ordenado():
    lista = [1, 1, 2, 3, 4, 5]
    assert ordenada(lista) == True
        
        
