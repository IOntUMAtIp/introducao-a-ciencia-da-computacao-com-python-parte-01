def lista_grande(n):
    from random import randint
    numeros = []
    for vezes in range(n):
        numeros.append(randint(-n, n))
    return numeros

def test_lista_grande():
    lista = lista_grande(10)
    for i in lista:
        assert isinstance(i, int)

