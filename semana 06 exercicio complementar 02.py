def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

import pytest

@pytest.mark.parametrize("entrada, saida", [(0, 0),
                                            (1, 1),
                                            (2, 1),
                                            (3, 2),
                                            (4, 3),
                                            (5, 5)])
def test_fibonacci(entrada, saida):
    assert fibonacci(entrada) == saida
