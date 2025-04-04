# Pedir al usuario que ingrese los valores de los catetos
A = float(input("Ingrese el valor del cateto A: "))
B = float(input("Ingrese el valor del cateto B: "))

# Calcular los cuadrados de los catetos
cuadradoA = A**2
cuadradoB = B**2

# Sumar los cuadrados
sumaCuadrados = cuadradoA + cuadradoB

# Calcular la hipotenusa usando **0.5
C = sumaCuadrados**0.5

# Mostrar el resultado
print("La hipotenusa del triángulo rectángulo es:", C)