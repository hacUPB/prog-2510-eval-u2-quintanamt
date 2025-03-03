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


### Puntos a tener en cuenta para realizar el Diagrama de Flujo y el Algoritmo:
1. Para hallar la distancia entre 2 puntos tomamos los puntos de la recta para hallar la pendiente  P1 (x1,y1) y P2 (x2,y2)
2. Sacamos las diferencias de x=x2-x1  y y=y2-y1
3. Y se aplica el cuadrado a x^2 y y^2, después lo sumamos (x^2) y (y^2)
4. Calculo de la raiz cuadrada para obtener la distancia D 
5. Imprimimos la distancia D
6. Fin

### Diagrama de flujo 

![alt text](<../Images/Captura de pantalla 2025-02-25 a la(s) 3.08.41 p.m..png>)

### Pseudocódigo 

    Inicio
    
    Escribir "Ingrese la coordenada x del primer punto:"
    Leer x1
    Escribir "Ingrese la coordenada y del primer punto:"
    Leer y1
    
  
    Escribir "Ingrese la coordenada x del segundo punto:"
    Leer x2
    Escribir "Ingrese la coordenada y del segundo punto:"
    Leer y2
    
    // Calcular las diferencias
    deltax = x2 - x1
    deltay = y2 - y1
    
 
    distancia = raizCuadrada(deltax * deltax + deltay * deltay)
    
    // Mostrar el resultado
    Escribir "La distancia entre los dos puntos es:", d
    Fin



2. Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero.
Para cada pedido, tiene que proporcionar las medidas de la tela
en pulgadas, pero ella generalmente las tiene en metros. Realice un algoritmo
para ayudar a resolver el problema, determinando cuántas pulgadas
debe pedir con base en los metros que requiere. Represéntelo mediante un
diagrama de flujo y pseudocódigo (1 pulgada = 0.0254 m).

### Analisis 
1. Se solicita a la persona los metros que desea convertir en pulgadas
2. Se escribe la conversion de m a in 
3. Se imprime el valor de la distancia en pulgadas

### Diagrama de Flujo 
![alt text](<../Images/Captura de pantalla 2025-02-25 a la(s) 3.12.17 p.m..png>)

### Pseudocodigo
    Inicio
    // Pedir la cantidad de metros
    Escribir "Ingrese la cantidad de metros de tela que necesita:"
    Leer metros
    
    // Convertir metros a pulgadas
    in = metros / 0.0254
    
    // Mostrar el resultado
    Escribir "Debe pedir", in, "pulgadas de tela."
    Fin

3. Se requiere determinar la hipotenusa de un triángulo rectángulo. ¿Cómo sería el diagrama de flujo y el pseudocódigo que representen el algoritmo para obtenerla? 
Recuerde que por Pitágoras se tiene que: $C^2 = A^2 + B^2$.

### Analisis
1. Tenemos el cateto A y el cateto B
2. Se le saca el cuadrado a cada cateto, cuando le sacamos el cuadrado se hace la suma de estos y el resultado de esa suma se le aplica raiz cuadrada
3. Nos imprimiria la C que es la hipotenusa
4. Fin 

### Diagrama de Flujo 

![alt text](<../Images/Captura de pantalla 2025-02-25 a la(s) 3.25.41 p.m..png>)

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

4. Se requiere determinar la edad actual de una persona basándose en su fecha de nacimiento. Además, es necesario establecer si la persona ya ha cumplido años en el año en curso, si aún no lo ha hecho, o si hoy es su cumpleaños, para celebrarlo. La fecha de nacimiento y la fecha actual estarán representadas mediante tres variables: día, mes y año.
    
    **Instrucciones:**
    
    - Diseñe un algoritmo que permita calcular la edad de la persona.
    - Dentro de la solución, determine si la persona ya celebró su cumpleaños este año o si aún no lo ha hecho.
    - Verifique si la fecha actual corresponde al día de su cumpleaños. De ser así, imprima el mensaje “Feliz Cumpleaños”.
    - Represente la solución utilizando **pseudocódigo** claro y estructurado.

### Analisis 

Entrada de Datos:

Se solicitan la fecha de nacimiento (dia_nac, mes_nac, anio_nac) y la fecha actual (dia_actual, mes_actual, anio_actual).

Cálculo Inicial de la Edad:

La edad se inicializa como la diferencia entre el año actual y el año de nacimiento:
edad = anio_actual - anio_nac.

Ajuste de la Edad:

Si el mes actual es anterior al mes de nacimiento:
La persona aún no cumple años, por lo que se reduce la edad en 1.
Ejemplo: Nacido en noviembre y estamos en enero.

Si el mes actual es igual al mes de nacimiento pero el día actual es anterior al día de nacimiento:
Tampoco ha cumplido años, y se resta 1 a la edad.
Ejemplo: Nacido el 15 de marzo y estamos el 10 de marzo.

Verificación del Cumpleaños:

Si el día y mes actuales coinciden con los de nacimiento, se imprime: "¡Feliz Cumpleaños!".

Determinación del Estado del Cumpleaños:

Ya celebró:
Si el mes actual es posterior al mes de nacimiento, o si es el mismo mes pero el día actual es igual o posterior.
Ejemplo: Nacido en abril y estamos en mayo, o nacido el 5 de junio y estamos el 10 de junio.

Aún no ha celebrado:
En caso contrario.
Ejemplo: Nacido en diciembre y estamos en enero.


    Inicio

        // Declarar variables para fecha de nacimiento y fecha actual
        Entero dia_nac, mes_nac, anio_nac
        Entero dia_actual, mes_actual, anio_actual
        Entero edad
        Booleano yaCelebro

        // Solicitar fecha de nacimiento
        Escribir "Ingrese su día de nacimiento (1-31):"
        Leer dia_nac
        Escribir "Ingrese su mes de nacimiento (1-12):"
        Leer mes_nac
        Escribir "Ingrese su año de nacimiento:"
        Leer anio_nac

        // Solicitar fecha actual
        Escribir "Ingrese el día actual (1-31):"
        Leer dia_actual
        Escribir "Ingrese el mes actual (1-12):"
        Leer mes_actual
        Escribir "Ingrese el año actual:"
        Leer anio_actual

        // Calcular la edad inicial
        edad = anio_actual - anio_nac

        // Verificar si ya cumplió años este año
        Si mes_actual < mes_nac Entonces
            edad = edad - 1
            yaCelebro = Falso
        Sino Si mes_actual == mes_nac Entonces
            Si dia_actual < dia_nac Entonces
                edad = edad - 1
                yaCelebro = Falso
            Sino Si dia_actual == dia_nac Entonces
                Escribir "¡Feliz Cumpleaños!"
                yaCelebro = Verdadero
            Sino
                yaCelebro = Verdadero
            Fin Si
        Sino
            yaCelebro = Verdadero
        Fin Si

        // Mostrar la edad y el estado del cumpleaños
        Escribir "Edad actual: ", edad
        Si yaCelebro Entonces
            Escribir "Ya ha celebrado su cumpleaños este año."
        Sino
            Escribir "Aún no ha celebrado su cumpleaños este año."
        Fin Si
    Fin

5. Realice un algoritmo que permita determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora, considerando que a partir de la hora número 41 y hasta la 45, cada hora se le paga el doble, de la hora 46 a la 50, el triple, y que trabajar
más de 50 horas no está permitido. Represente el algoritmo mediante pseudocódigo.

#### Analisis 
1. Objetivo: Obtener las horas trabajadas y el pago por horas
-Se solicitan los valores necesarios para el cálculo: Horas trabajadas y tarifas por hora. 
2. Inicialización del Sueldo
-Se inicializa la variable que almacenará el resultado final
3.  Evaluacion de las horas en diferentes rangos

(a) si horas trabajadas <= 40 
(Horas normales)

(b) si horas trabajadas (41-45) Horas se multiplica
Sino Si horasTrabajadas <= 45 Entonces
    sueldoSemanal = 40 * pagoPorHora + (horasTrabajadas - 40) * pagoPorHora * 2
(Horas extras dobles)

(c) Sino Si horasTrabajadas <= 50 Entonces
    sueldoSemanal = 40 * pagoPorHora + 5 * pagoPorHora * 2 + (horasTrabajadas - 45) * pagoPorHora * 3
(Horas extra tiples)

    Inicio

        // Pedir las horas trabajadas y el pago por hora
        Escribir "Ingrese las horas trabajadas en la semana:"
        Leer horasTrabajadas
        Escribir "Ingrese el pago por hora:"
        Leer pagoPorHora

        // Inicializar el sueldo semanal
        sueldoSemanal = 0

        // Calcular el sueldo basado en las horas trabajadas
        Si horasTrabajadas <= 40 
            sueldoSemanal = horasTrabajadas * pagoPorHora
        Sino
            Si horasTrabajadas <= 45 
                sueldoSemanal = 40 * pagoPorHora + (horasTrabajadas - 40) * pagoPorHora * 2
            Sino
                Si horasTrabajadas <= 50 
                    sueldoSemanal = 40 * pagoPorHora + 5 * pagoPorHora * 2 + (horasTrabajadas - 45) * pagoPorHora * 3
                Sino
                    Escribir "No está permitido trabajar más de 50 horas."
                    sueldoSemanal = 0
                Fin Si
            Fin Si
        Fin Si

        // Mostrar el sueldo semanal
        Si sueldoSemanal > 0 Entonces
            Escribir "El sueldo semanal es:", sueldoSemanal
        
        Fin Si
        
6. Se requiere un algoritmo para determinar, de N cantidades, cuántas son cero, cuántas son menores a cero, y cuántas son mayores a cero. Realice el pseudocódigo para representarlo, utilizando el ciclo apropiado.

(a) Se inicializan tres variables para almacenar los conteos de cada categoría:

-contadorCero: Cantidad de números iguales a cero.

-contadorMenorCero: Cantidad de números negativos.

-contadorMayorCero: Cantidad de números positivos.

(b) Se solicita al usuario el valor de N (total de números a evaluar).

(c)Se utiliza un bucle Para (ciclo definido) para iterar N veces:

(d)Para cada número ingresado, se evalúa su valor mediante condiciones anidadas:

(e) Estructura lógica:

Si el número es cero, incrementa contadorCero.

Si no es cero, verifica si es negativo:

Si es negativo, incrementa contadorMenorCero.

Si no es negativo (y ya se descartó que sea cero), es positivo, por lo que incrementa contadorMayorCero.

(f) mostrar resultados 


    Inicio

        // Inicializar contadores
        contadorCero = 0
        contadorMenorCero = 0
        contadorMayorCero = 0

        // Pedir el número de cantidades
        Escribir "Ingrese el número de cantidades:"
        Leer N

        // Iterar sobre las N cantidades
        Para i = 1 Hasta N Hacer
            Escribir "Ingrese la cantidad ", i, ":"
            Leer cantidad

            // Determinar si la cantidad es cero, menor a cero o mayor a cero
            Si cantidad == 0 
                contadorCero = contadorCero + 1
            Sino
                Si cantidad < 0
                    contadorMenorCero = contadorMenorCero + 1
                Sino
                    contadorMayorCero = contadorMayorCero + 1
                Fin Si
            Fin Si
        Fin Para

        // Mostrar los resultados
        Escribir "Cantidades iguales a cero:", contadorCero
        Escribir "Cantidades menores a cero:", contadorMenorCero
        Escribir "Cantidades mayores a cero:", contadorMayorCero

    Fin 

7. Se requiere un algoritmo para determinar cuánto ahorrará en pesos una persona diariamente, y en un año, si ahorra 3¢ el primero de enero, 9¢ el dos de enero, 27¢ el 3 de enero y así sucesivamente todo el año. Represente la solución mediante pseudocódigo.

Inicialización de Variables:

ahorroDiario = 0.03: Se establece el ahorro inicial del primer día en 0.03 pesos (3 centavos).

ahorroTotal = 0.0: Se inicializa el ahorro total acumulado en 0.

diasEnAnio = 365: Se define el número de días en un año como 365.

Bucle para Cada Día del Año:

Para dia = 1 Hasta diasEnAnio Hacer: Se inicia un bucle que se repite 365 veces, una vez para cada día del año.

Escribir "Día", dia, ": Ahorro diario =", ahorroDiario, "pesos": Se muestra el número del día y el ahorro correspondiente a ese día.

ahorroTotal = ahorroTotal + ahorroDiario: Se suma el ahorro del día actual al ahorro total acumulado.

ahorroDiario = ahorroDiario * 3: Se calcula el ahorro para el siguiente día, triplicando el ahorro del día actual.

Fin Para: Termina el bucle.

Mostrar el Ahorro Total:

Escribir "El ahorro total en un año es:", ahorroTotal, "pesos": Se muestra el ahorro total acumulado al final del año.
En palabras simples:



        Inicio

            // Inicializar variables
            ahorroDiario = 0.03  // Ahorro inicial en pesos (3 centavos)
            ahorroTotal = 0.0
            diasEnAnio = 365

            // Iterar sobre cada día del año
            Para dia = 1 Hasta diasEnAnio Hacer
                // Mostrar el ahorro del día actual
                Escribir "Día", dia, ": Ahorro diario =", ahorroDiario, "pesos"

                // Sumar el ahorro diario al ahorro total
                ahorroTotal = ahorroTotal + ahorroDiario

                // Calcular el ahorro para el próximo día (multiplicar por 3)
                ahorroDiario = ahorroDiario * 3
            Fin Para

            // Mostrar el ahorro total en el año
            Escribir "El ahorro total en un año es:", ahorroTotal, "pesos"

       
        Fin

8. Realice el algoritmo para determinar cuánto pagará una persona que adquiere N artículos, los cuales están de promoción. Considere que si su precio es mayor o igual a $200 se le aplica un descuento de 15%, y si su precio es mayor a $100, pero menor a $200, el descuento es de
  12%; de lo contrario, solo se le aplica 10%. Se debe saber cuál es el costo y el descuento que tendrá cada uno de los artículos y finalmente cuánto se pagará por todos los artículos obtenidos. Represente la solución mediante pseudocódigo.

 ### Analisis 
 1. Inicialización de Variables:

 totalPagar = 0.0: 
   2. Entrada del Número de Artículos:

   Leer N: Se lee el número de artículos ingresado por el usuario y se almacena en la variable N.

 3. Bucle para Procesar Cada Artículo:

Para i = 1 Hasta N Hacer: Se inicia un bucle que se ejecutará N veces, una vez por cada artículo. La variable i se utiliza como contador del bucle.
 
 Escribir "Ingrese el precio del artículo ", i, ":": Se solicita al usuario que ingrese el precio del artículo actual (indicado por el valor de i).
 
 Leer precio: Se lee el precio ingresado por el usuario y se almacena en la variable precio.

 4. Cálculo del Descuento:

  Se utiliza una estructura condicional Si-Sino-Fin Si para determinar el descuento aplicable según el precio del artículo:
 Si precio >= 200
 descuento = precio * 0.15: Se calcula el descuento y se almacena en la variable descuento.
 
 Sino Si precio > 100 
 descuento = precio * 0.12: 
 
 Sino: Si el precio es menor o igual a 100
descuento = precio * 0.10: Se calcula el descuento y se almacena en descuento.

 Fin Si: Fin de la estructura condicional.
  5. Cálculo del Costo con Descuento:

costoConDescuento = precio - descuento
 6. Mostrar Información del Artículo:

 7. Acumulación del Total a Pagar:

 totalPagar = totalPagar + costoConDescuento: Se suma el costo del artículo actual (con descuento) al total acumulado en la variable totalPagar.

  8. Fin del Bucle:

  9. Mostrar el Total a Pagar

    Inicio

            // Inicializar variables
            totalPagar = 0.0

            // Pedir el número de artículos
            Escribir "Ingrese el número de artículos:"
            Leer N

            // Iterar sobre cada artículo
            Para i = 1 Hasta N Hacer
                // Pedir el precio del artículo
                Escribir "Ingrese el precio del artículo ", i, ":"
                Leer precio

                // Determinar el descuento según el precio
                Si precio >= 200 
                    descuento = precio * 0.15
                Sino
                    Si precio > 100
                        descuento = precio * 0.12
                    Sino
                        descuento = precio * 0.10
                    Fin Si
                Fin Si

                // Calcular el costo con descuento
                costoConDescuento = precio - descuento

                // Mostrar el costo y el descuento del artículo
                Escribir "Artículo ", i, ":"
                Escribir "  Precio original:", precio
                Escribir "  Descuento:", descuento
                Escribir "  Costo con descuento:", costoConDescuento

                // Sumar al total a pagar
                totalPagar = totalPagar + costoConDescuento
            Fin Para

            // Mostrar el total a pagar por todos los artículos
            Escribir "El total a pagar por todos los artículos es:", totalPagar

    Fin

9. Realice un algoritmo y represéntelo mediante pseudocódigo para obtener una función exponencial, la cual está dada por:
    
    $𝑒^𝑥 = 1+\frac x {1!} + \frac {x^2}{2!}+ \frac {x^3}{3!}+ …$

#### Analisis 
Entrada de Datos:

Escribir "Ingrese el valor de x:": Se le pide al usuario que introduzca el valor de "x".
x= Variable 
Pedimos la precisión deseada (número de términos)

Leer precision: Se guarda el valor de la "precisión" que ingresó el usuario.

Inicialización de Variables:

resultado = 1.0: Se empieza con un resultado inicial de 1. Esto se debe a que el primer término de la serie de Taylor para e^x es 1.

termino = 1.0: Se inicializa el primer término en 1.
factorial = 1: Se inicializa la variable "factorial" en 1, ya que se usará para calcular factoriales.

Cálculo de la Serie de Taylor:

Para i = 1 Hasta precision Hacer: Se inicia un bucle que se repite tantas veces como el valor de "precisión" que ingresó el usuario.

factorial = factorial * i: Se calcula el factorial del número actual ("i").

termino = (x^i) / factorial: Se calcula el siguiente término de la serie de Taylor.

resultado = resultado + termino: Se suma el término calculado al "resultado" acumulado.

Fin Para: Termina el bucle.
Mostrar el Resultado:

Escribir "El valor aproximado de e^", x, " es:", resultado: Se muestra el resultado final, que es la aproximación de e^x.



    Inicio

        // Pedir el valor de x y la precisión deseada
        Escribir "Ingrese el valor de x:"
        Leer x
        Escribir "Ingrese la precisión deseada (número de términos):"
        Leer precision

        // Inicializar variables
        resultado = 1.0  // El primer término de la serie es 1
        termino = 1.0    // Inicializar el primer término
        factorial = 1    // Inicializar el factorial

        // Calcular la serie de Taylor para e^x
        Para i = 1 Hasta precision Hacer
            factorial = factorial * i  // Calcular el factorial de i
            termino = (x^i) / factorial  // Calcular el término actual
            resultado = resultado + termino  // Sumar el término al resultado
        Fin Para

        // Mostrar el resultado
        Escribir "El valor aproximado de e^", x, " es:", resultado
    Fin




10. Realice un algoritmo para obtener el seno de un ángulo y represéntelo mediante pseudocódigo. Utilice la siguiente ecuación:
$Sen x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...$

Explicación:

calcular Seno(x, precision):

x: El ángulo en radianes.

precision: Cuántos términos de la serie usar.

Inicialización:
seno comienza con el primer término (x).
termino guarda el valor del término actual.
signo alterna entre -1 y 1.

Bucle:
Se calcula termino usando el anterior y la fórmula.

Suma o resta termino a seno según el signo.

Cambia el signo.

Resultado:

Devuelve el valor aproximado del seno.






    Inicio

        Función calcularSeno(x, precision):
            seno = x
            termino = x
            signo = -1
            
            Para i desde 1 hasta precision:
                termino = termino * x * x / ((2 * i) * (2 * i + 1))
                seno = seno + signo * termino
                signo = -signo
            
            Retornar seno
    Fin
    
