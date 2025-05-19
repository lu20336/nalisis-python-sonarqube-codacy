def saludar(nombre):
    print("Hola " + nombre)

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división por cero"

saludar("Mundo")
print(dividir(10, 0))

