def busca(lista, elemento):
    buscado = elemento
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i
    return False

def test_buscado():
    lista = [1, 2, 3, 4, 5]
    buscado = 3
    assert busca(lista, buscado) == 2

def test_erro_busca():
    lista = [1, 2, 3, 4, 5]
    buscado = 7
    assert busca(lista, buscado) == False
