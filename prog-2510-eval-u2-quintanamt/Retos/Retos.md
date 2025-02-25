### Ejercicio Extra de Bucles 

1. Solicitar al usuario 2 números enteros, imprimir en pantalla los numeros pares comprendidos entre ellos. 
            
        Inicio

        Escribir "Introduce el primer número entero:"
        Leer num1
        Escribir "Introduce el segundo número entero:"
        Leer num2
        
        Si num1 < num2 Entonces
            inicio = num1
            fin = num2
        Sino
            inicio = num2
            fin = num1
        Fin Si

        Escribir "Números pares entre", inicio, "y", fin, ":"
        
        Para numero = inicio + 1 Hasta fin - 1 Hacer
            Si numero % 2 == 0 Entonces
                Escribir numero
            Fin Si
        Fin Para
        
        Fin

2. Serie de Fibonacci 

       Inicio
        Escribir "¿Cuántos números de la serie de Fibonacci desea imprimir?"
        Leer cantidad

        Si cantidad <= 0 Entonces
        Escribir "La cantidad debe ser mayor que 0."
        Sino
        a = 0
        b = 1
        Escribir a
        Si cantidad > 1 Entonces
            Escribir b
        Fin Si

        Para i = 3 Hasta cantidad Hacer
            c = a + b
            Escribir c
            a = b
            b = c
        Fin Para
         Fin Si
        Fin



# Instrucciones

Analiza los siguientes ejercicios, para ello utiliza una tabla donde clasifiques las variables de entrada, las de salida y las constantes. Enuncia las ecuaciones involucradas y explique cuál es el análisis o estrategia que utilizará para llegar a la solución del problema.

# Problemas

1. Se requiere obtener la distancia entre dos puntos en el plano cartesiano,
tal y como se muestra en la figura 1. Realice un diagrama de flujo y pseudocódigo
que representen el algoritmo para obtener la distancia entre
esos puntos.

![alt text](<../Images/Captura de pantalla 2025-02-19 a la(s) 11.44.48 a.m..png>)



### Diagrama de flujo 

![alt text](<../Images/Captura de pantalla 2025-02-19 a la(s) 12.10.40 p.m..png>)

### Pseudocódigo 

    Inicio
    // Pedir las coordenadas del primer punto
    Escribir "Ingrese la coordenada x del primer punto:"
    Leer x1
    Escribir "Ingrese la coordenada y del primer punto:"
    Leer y1
    
    // Pedir las coordenadas del segundo punto
    Escribir "Ingrese la coordenada x del segundo punto:"
    Leer x2
    Escribir "Ingrese la coordenada y del segundo punto:"
    Leer y2
    
    // Calcular las diferencias
    deltaX = x2 - x1
    deltaY = y2 - y1
    
    // Calcular la distancia
    distancia = raizCuadrada(deltaX * deltaX + deltaY * deltaY)
    
    // Mostrar el resultado
    Escribir "La distancia entre los dos puntos es:", distancia
    Fin

2. Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero.
Para cada pedido, tiene que proporcionar las medidas de la tela
en pulgadas, pero ella generalmente las tiene en metros. Realice un algoritmo
para ayudar a resolver el problema, determinando cuántas pulgadas
debe pedir con base en los metros que requiere. Represéntelo mediante un
diagrama de flujo y pseudocódigo (1 pulgada = 0.0254 m).

### Diagrama de Flujo 

![alt text](<../Images/Captura de pantalla 2025-02-19 a la(s) 12.18.25 p.m..png>)

### Pseudocodigo
    Inicio
    // Pedir la cantidad de metros
    Escribir "Ingrese la cantidad de metros de tela que necesita:"
    Leer metros
    
    // Convertir metros a pulgadas
    pulgadas = metros / 0.0254
    
    // Mostrar el resultado
    Escribir "Debe pedir", pulgadas, "pulgadas de tela."
    Fin

3. Se requiere determinar la hipotenusa de un triángulo rectángulo. ¿Cómo sería el diagrama de flujo y el pseudocódigo que representen el algoritmo para obtenerla? 
Recuerde que por Pitágoras se tiene que: $C^2 = A^2 + B^2$.

### Diagrama de Flujo 
![alt text](<../Images/Captura de pantalla 2025-02-19 a la(s) 12.32.07 p.m..png>)

### Pseudoódigo

    Inicio
    // Pedir los valores de los catetos
    Escribir "Ingrese el valor del cateto A:"
    Leer A
    Escribir "Ingrese el valor del cateto B:"
    Leer B
    
    // Calcular los cuadrados de los catetos
    cuadradoA = A * A
    cuadradoB = B * B
    
    // Sumar los cuadrados
    sumaCuadrados = cuadradoA + cuadradoB
    
    // Calcular la hipotenusa
    C = raizCuadrada(sumaCuadrados)
    
    // Mostrar el resultado
    Escribir "La hipotenusa del triángulo rectángulo es:", C
    Fin


