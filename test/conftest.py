import pytest
#preparador de recursos que se necesita para los test, da algo listo para correr el test cuando lo necesites: 

@pytest.fixture
def numeros ():
    return 5, 5