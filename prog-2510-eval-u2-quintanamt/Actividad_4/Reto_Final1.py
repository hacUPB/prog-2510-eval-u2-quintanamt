## 6. Reto final

### Reto: toma el pseudocódigo de los 5 primeros ejercicios del reto y realiza la traducción a Python:
#- Revisa el pseudocódigo y asegúrate que no contiene errores.
#- **Traduce** ese pseudocódigo a Python.
#- **Comenta** tu código para indicar los pasos principales.

#RETO 1
## Solicitar las coordenadas del primer punto
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))

## Solicitar las coordenadas del segundo punto
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

## Calcular las diferencias
deltax = x2 - x1
deltay = y2 - y1

## Calcular la distancia usando la fórmula de la distancia entre dos puntos
distancia = (deltax**2 + deltay**2)**0.5  # Raíz cuadrada usando **0.5

## Mostrar el resultado
print("La distancia entre los dos puntos es:", distancia)

