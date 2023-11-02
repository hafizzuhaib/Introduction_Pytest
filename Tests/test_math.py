import pytest

def test_one_plus_one():
    assert 1 + 1 == 2


products_Multiply = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5,-5,25),
    (2.5,6.7,16.75)
]

products_Add = [
    (2, 3, 5),
    (1, 99, 100),
    (0, 99, 99),
    (3, -4, -1),
    (-5, -5, -10),
    (2.5,6.7,9.2)
]

@pytest.mark.parametrize('a, b, products_Multiply', products_Multiply)



def test_multiplication(a, b , products_Multiply):
    assert a * b == products_Multiply


@pytest.mark.parametrize('a, b, products_Add', products_Add)

def test_Add(a, b , products_Add):
    assert a + b == products_Add


