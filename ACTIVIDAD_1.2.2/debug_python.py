#contador=0
#while contador <3:
    #print(f"contador:{contador}")
    #contador+=1

# def area_rectangulo(base, altura):
#     """Calcula el área de un rectángulo."""
#     area=base*altura
#     print(f"el area de un rectangulo es: {area}")
#     return area

# area_rectangulo(3,2)
# area_rectangulo(4,3)
# area_rectangulo(5,6)

# def saludo(nombre, mensaje="¡Hola!"):
#     """Muestra un saludo personalizado."""
#     return f"{mensaje} {nombre}"

# print(saludo("maria"))
# print(saludo("andres", mensaje ="hey que onda"))

def factorial(n):
    """Calcula el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejemplo de uso 5*4*3*2*1
print(factorial(5))  # Salida: 120

