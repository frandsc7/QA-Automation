import pytest
import operaciones
from typing import Literal

# para correr todos los tests: python -m pytest    
#para todos los tests pyhton -m pytest -v -m listo
#para uno especifico: python -m pytest -v -k test_sumar

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

def test_sumar_varios(a: Literal[2] | Literal[-4] | Literal[0], b: Literal[5] | Literal[-2] | Literal[0], esperado):
    assert operaciones.sumar(a,b) == esperado

def test_restar_varios(numeros: tuple[Literal[5], Literal[5]]):
    a,b = numeros
    assert operaciones.restar(a,b) == 0

def test_sumar_con_fixture (numeros: tuple[Literal[5], Literal[5]]):
    a,b = numeros
    assert operaciones.sumar (a,b) == 10   



"""def test_sumar_varios(a, b, esperado):
    assert operaciones.sumar(a,b) == esperado

def test_restar_com_fixture(numeros):
    a,b = numeros
    assert operaciones.restar(a,b) == 0

def test_sumar_com_fixture (numeros):
    a,b = numeros
    assert operaciones.sumar(a,b) == 10
"""
@pytest.mark.listo

def test_sumar_listo():
    assert operaciones.sumar(1,3) == 4        


def test_estructura_dicc():
#para preguntar por clave
    data = {"nombre": "Luisa", "edad": 34}

    assert "nombre" in data
    assert "edad" in data
#la palabra permite pasarle la clave de la data y decir de que tipo va a ser
    assert isinstance (data["nombre"], str) 
    assert isinstance (data["edad"], int)

def test_estructura_list():
    #esta estructura nos va a permitir si el elemento esta dentro de nuestra lista
    items = [{"id": 1, "id": 2 }]
#permite ejecutar una iteracion y corroborar que en la lista tengamos la clave que esperamos que tenga
    assert all("id" in item for item in items)

 #PARA GENERAR EL REPORTE HTML python -m pytest --html=report.html --self-contained-html