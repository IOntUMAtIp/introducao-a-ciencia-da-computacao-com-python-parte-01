def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n - 1)

import pytest

@pytest.mark.parametrize("entrada, saida",[
                                            (0, 1),
                                            (1, 1),
                                            (2, 2),
                                            (3, 6)])
def test_fatorial(entrada, saida):
    assert fatorial(entrada) == saida
