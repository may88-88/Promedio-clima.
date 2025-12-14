# Programación Tradicional
# Cálculo del promedio semanal del clima

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de la semana
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de temperaturas
    """
    return sum(temperaturas) / len(temperaturas)

# Programa principal
temperaturas_semana = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas_semana)

print(f"El promedio semanal del clima es: {promedio:.2f} °C")
