#FUNCIONES

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def sumar (a , b):
    return a + b

def dividir (a , b):
    if b == 0:
        raise ValueError("Error al dividir por cero")
    return a/b




def calculadora_simple (operacion, a, b):
    try:
        if operacion == "sumar":
            return a + b
        elif operacion == "restar":
            return a - b
        elif operacion == "division":
            return a/b
        elif operacion == "multiplicacion":
            return a * b
        else:
            return KeyError("Operación no válida")
        
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"
    except ValueError:
        raise "Error: los valores deben ser numéricos"

print(calculadora_simple("sumar", 3, 4))

#try and except
""" 
try: 
    resultado = 10 / 0 
except ZeroDivisionError as e:
    print("Error: No se puede dividir por cero")
    print(f"Detalles del error: {e}")

try: 
    numero = int ("123")
except ValueError as e:
    print(f"Error: {e}")

try:
    print(persona["documento"])
except KeyError as e:
    print("La clave no existe en el diccionario")    

"""