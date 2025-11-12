"""print("Hola mundo")"""
"""for i in range(11):
    if i == 5:
        break
    print(i)"""

"""for i in range (15, 0, -1):
    print(i)
    
    


i = 1
while i<=5:
    print(i)
    i = i + 1    
    """




#Listas 

#             0,       1,     2
mi_lista = ["Franco", 455, "negro"]
#mi_lista.pop(2)
#mi_lista.append(1998)
#print(mi_lista)








#tupla
 #              0,     1,     2  
mi_tupla = ("Azul", 200, "Rojo")
#inmutable
print(mi_tupla[1]) #Se accede por indice tambien, igual que la lista

#diccionarios
"""persona =  {
    "Nombre" : "Jaime",
    "Apellido": "Perez",
    "Edad": 34
}
"""

""""
def saludo(nombre):
    print(f"Hola {nombre}")

saludo("Maria") 
saludo("Jose")  
saludo("Adrian")
"""
"""def saludo(nombre):
    return f"Hola {nombre}"
< >
saludo("Maria") """

#Modularizar

"""def sumar(a,b):
    return a+ b

def calculadora_simple (operacion, a, b ):
    if operacion == "sumar":
        return sumar(a,b)
    else:
        return "Operación no válida"
    
print(calculadora_simple("sumar, 7, 3"))
    """

licencia = False
edad = int(input("Ingresa tu edad"))
if not (edad >= 18):
    print("No puedes cursar")
