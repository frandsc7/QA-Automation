import pytest
import operaciones


def test_sumar ():
    assert operaciones.calculadora_simple("sumar", 2,4) == 6

#Para que el test pase python -m pytest -v

def test_restar():
    assert operaciones.calculadora_simple("restar", 5, 3) == 2

def test_multiplicar():
    assert operaciones.multiplicar (5, 2) == 10

def test_division_por_cero():
    with pytest.raises(ValueError):   
        operaciones.dividir(10, 0)


# Permite pasarle dos argumentos, primero un string y después una lista

@pytest.mark.parametrize("a, b, esperado", [
(2,5,7), #numeros positivos
(-4,-2, -6), #numeros negativos
(0, 0, 0) #suma de ceros
])

@pytest.mark.listo

def test_sumar_varios(a, b, esperado):
    assert operaciones.sumar(a,b) == esperado

def test_restar_com_fixture(numeros):
    a,b = numeros
    assert operaciones.restar(a,b) == 0

def test_sumar_com_fixture (numeros):
    a,b = numeros
    assert operaciones.sumar(a,b) == 10

