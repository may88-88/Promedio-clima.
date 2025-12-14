# Programación Orientada a Objetos
# Cálculo del promedio semanal del clima

class ClimaSemanal:
    """
    Clase que representa el clima semanal
    """

    def __init__(self):
        # Encapsulamiento de las temperaturas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias
        """
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal
        """
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa principal
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()

print(f"El promedio semanal del clima es: {promedio:.2f} °C")
