def encontra_impares(lista):
    impares = []
    if lista[0] % 2 is not 0:
        impares.append(lista[0])
    if len(lista) > 1:
        del lista[0]
        impares.extend(encontra_impares(lista))
    return impares
    
import pytest

@pytest.mark.parametrize("lista, saida", [
                                         ([7, 7, 7], [7, 7, 7]),
                                         ([1, 2, 3, 7], [1, 3, 7])])
                                         
def test_impares(lista, saida):
    assert encontra_impares(lista) == saida
