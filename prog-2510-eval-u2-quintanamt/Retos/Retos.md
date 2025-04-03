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



**1. Que variables voy a utilizar:**


* **Metodología:** Se declaran variables de tipo entero (`Entero`) para almacenar el día, mes y año de nacimiento (`dia_nac`, `mes_nac`, `anio_nac`) y la fecha actual (`dia_actual`, `mes_actual`, `anio_actual`). También se declara una variable entera llamada `edad` para guardar el resultado del cálculo de la edad y una variable booleana (`Booleano`) llamada `yaCelebro` para indicar si el cumpleaños ya ha ocurrido este año.

**2. Entrada de Datos:**


* **Metodología:** Se utilizan instrucciones de escritura (`Escribir`) para mostrar mensajes al usuario solicitando el día, mes y año de nacimiento, así como el día, mes y año actual. Posteriormente, se utilizan instrucciones de lectura (`Leer`) para almacenar los valores ingresados por el usuario en las variables correspondientes. Se incluyen mensajes indicando los rangos esperados para el día (1-31) y el mes (1-12).

**3. Cálculo Inicial de la Edad:**


* **Metodología:** Se resta el año de nacimiento (`anio_nac`) del año actual (`anio_actual`) y el resultado se asigna a la variable `edad`. Esta operación proporciona la diferencia de años, pero no considera aún el mes y el día de nacimiento.

**4. Ajuste por Cumpleaños:**

* **Metodología:** Se utiliza una estructura condicional anidada (`Si-Entonces-Sino Si-Entonces-Sino-Fin Si`) para comparar el mes y el día actual con el mes y el día de nacimiento:
    * **Si el mes actual es menor que el mes de nacimiento:** Significa que el cumpleaños aún no ha ocurrido este año. Se decrementa la `edad` en 1 y se asigna `Falso` a la variable `yaCelebro`.
    * **Sino Si el mes actual es igual al mes de nacimiento:** Se verifica el día:
        * **Si el día actual es menor que el día de nacimiento:** El cumpleaños aún no ha ocurrido. Se decrementa la `edad` en 1 y se asigna `Falso` a `yaCelebro`.
        * **Sino Si el día actual es igual al día de nacimiento:** ¡Es el día del cumpleaños! Se muestra un mensaje de felicitación y se asigna `Verdadero` a `yaCelebro`.
        * **Sino (el día actual es mayor que el día de nacimiento):** El cumpleaños ya pasó. Se asigna `Verdadero` a `yaCelebro`.
    * **Sino (el mes actual es mayor que el mes de nacimiento):** El cumpleaños ya ocurrió en un mes anterior. Se asigna `Verdadero` a `yaCelebro`.

**5. Salida de Resultados:**


* **Metodología:** Se utiliza una instrucción de escritura (`Escribir`) para mostrar el valor de la variable `edad`. Posteriormente, se utiliza una estructura condicional (`Si-Entonces-Sino-Fin Si`) para verificar el valor de la variable `yaCelebro`:
    * **Si `yaCelebro` es `Verdadero`:** Se muestra un mensaje indicando que ya ha celebrado su cumpleaños este año.
    * **Sino (`yaCelebro` es `Falso`):** Se muestra un mensaje indicando que aún no ha celebrado su cumpleaños este año.




        Inicio
            // DECLARACIÓN DE VARIABLES //
            (Entero) dia_nac, mes_nac, anio_nac   // Almacena la  fecha de nacimiento //
            (Entero) dia_actual, mes_actual, anio_actual // Almacena la fecha actual //
        (Entero) edad                         // Guardará la edad calculada //
            yaCelebro                  // Indica si celebró cumpleaños //

            // ENTRADA DE DATOS //
            (Escribir) "Ingrese su día de nacimiento (1-31):"
            Leer dia_nac                        // Guarda día de nacimiento //
            Escribir "Ingrese su mes de nacimiento (1-12):"
            Leer mes_nac                        // Guarda mes de nacimiento //
            Escribir "Ingrese su año de nacimiento:"
            Leer anio_nac                       // Guarda año de nacimiento //

            Escribir "Ingrese el día actual (1-31):"
            Leer dia_actual                     // Guarda día actual//
            Escribir "Ingrese el mes actual (1-12):"
            Leer mes_actual                     // Guarda mes actual //
            Escribir "Ingrese el año actual:"
            Leer anio_actual                    // Guarda año actual // 

            // CÁLCULO INICIAL DE EDAD // 

            edad = anio_actual - anio_nac       // Diferencia básica de años //

            // AJUSTE POR CUMPLEAÑOS // 
            Si mes_actual < mes_nac Entonces    // Si no ha llegado al mes Reduce edad calculada // 
                edad = edad - 1                 
                yaCelebro = Falso               // No ha celebrado // 
            Sino Si mes_actual == mes_nac Entonces // Mes de cumpleaños //
                Si dia_actual < dia_nac Entonces // Antes del día // 
                    edad = edad - 1             // Reduce edad // 
                    yaCelebro = Falso           // No ha celebrado // 
                Sino Si dia_actual == dia_nac Entonces // ¡Es hoy! // 
                    Escribir "¡Feliz Cumpleaños!" // Mensaje especial // 
                    yaCelebro = Verdadero        // Sí celebró (hoy mismo) //
                Sino                            // Pasó el día //
                    yaCelebro = Verdadero       // Ya celebró //
                Fin Si
            Sino                                // Mes posterior //
                yaCelebro = Verdadero           // Ya celebró // 
            Fin Si

            // SALIDA DE RESULTADOS
            Escribir "Edad actual: ", edad      // Muestra edad calculada //
            
            Si yaCelebro Entonces               // Evaluación final // 
                Escribir "Ya ha celebrado su cumpleaños este año."
            Sino
                Escribir "Aún no ha celebrado su cumpleaños este año."
            Fin Si
        Fin


5. Realice un algoritmo que permita determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora, considerando que a partir de la hora número 41 y hasta la 45, cada hora se le paga el doble, de la hora 46 a la 50, el triple, y que trabajar
más de 50 horas no está permitido. Represente el algoritmo mediante pseudocódigo.



**1. Los datos de entrada que se le pide al usuario:**


* **Metodología:**
    * Se utiliza la instrucción `Escribir` para mostrar mensajes al usuario solicitando que ingrese la cantidad de horas trabajadas durante la semana.
    * La instrucción `Leer horasTrabajadas` captura el valor ingresado por el usuario y lo almacena en la variable `horasTrabajadas`.
    * De manera similar, se solicita al usuario que ingrese el pago por hora, y este valor se almacena en la variable `pagoPorHora`.

**2. Valor para empezar:**

* **Metodología:** Se declara e inicializa la variable `sueldoSemanal` con el valor de 0. Esto asegura que cualquier cálculo posterior se realice a partir de un valor base conocido.

**3. Lógica de Cálculo:**


* **Metodología:** Se utiliza una estructura condicional anidada (`Si-Entonces-Sino Si-Entonces-Sino Si-Entonces-Sino-Fin Si`) para evaluar la cantidad de `horasTrabajadas` y aplicar la lógica de cálculo correspondiente:
    * **Si `horasTrabajadas` es menor o igual a 40:** Se considera que todas las horas son normales. El `sueldoSemanal` se calcula multiplicando `horasTrabajadas` por `pagoPorHora`.
    * **Sino Si `horasTrabajadas` es menor o igual a 45:** Se asume que se trabajaron 40 horas normales y las horas restantes (hasta 45) son horas extras dobles. El `sueldoSemanal` se calcula sumando el pago de las 40 horas normales (`40 * pagoPorHora`) y el pago de las horas extras dobles `((horasTrabajadas - 40) * pagoPorHora * 2)`.
    * **Sino Si `horasTrabajadas` es menor o igual a 50:** Se considera que hay 40 horas normales, 5 horas extras dobles (de 41 a 45), y las horas restantes (hasta 50) son horas extras triples. El `sueldoSemanal` se calcula sumando el pago de las 40 horas normales (`40 * pagoPorHora`), el pago de las 5 horas extras dobles (`5 * pagoPorHora * 2`), y el pago de las horas extras triples `((horasTrabajadas - 45) * pagoPorHora * 3)`.
    * **Sino (si `horasTrabajadas` es mayor que 50):** Se considera que se ha excedido el límite de horas de trabajo permitido. Se muestra un mensaje de advertencia al usuario y se asigna el valor de 0 a `sueldoSemanal` para indicar un resultado inválido.

**4. Salida que se le muestra al usuario:**


* **Metodología:** Se utiliza una estructura condicional (`Si-Entonces-Fin Si`) para verificar si el valor de `sueldoSemanal` es mayor que 0. Si lo es (lo que indica que no se excedió el límite de horas), se utiliza la instrucción `Escribir` para mostrar el mensaje "El sueldo semanal es:" seguido del valor calculado de `sueldoSemanal`. Si `sueldoSemanal` no es mayor que 0 (debido al exceso de horas), no se muestra ningún sueldo.




        Inicio
            // ENTRADA DE DATOS //
            Escribir "Ingrese las horas trabajadas en la semana:"
            Leer horasTrabajadas  // Almacena el total de horas trabajadas //
            
            Escribir "Ingrese el pago por hora:"
            Leer pagoPorHora      // Almacena el valor de la tarifa por hora //

            // Valor inicial de la variable// 
            sueldoSemanal = 0     // Variable para acumular el cálculo //

            // Calculo de las horas // 
            Si horasTrabajadas <= 40 Entonces
                // Caso 1: Horas normales (sin extras)
                sueldoSemanal = horasTrabajadas * pagoPorHora
            Sino
                Si horasTrabajadas <= 45 Entonces
                    // Caso 2: Horas extras dobles (41-45)
                    sueldoSemanal = 40 * pagoPorHora + (horasTrabajadas - 40) * pagoPorHora * 2
                Sino
                    Si horasTrabajadas <= 50 Entonces
                        // Caso 3: Horas extras triples (46-50)
                        sueldoSemanal = 40 * pagoPorHora + 5 * pagoPorHora * 2 + (horasTrabajadas - 45) * pagoPorHora * 3
                    Sino
                        // Caso 4: Horas excedidas
                        Escribir "No está permitido trabajar más de 50 horas."
                        sueldoSemanal = 0  // Valor inválido
                    Fin Si
                Fin Si
            Fin Si

            // SALIDA DE DATOS //
            Si sueldoSemanal > 0 Entonces
                Escribir "El sueldo semanal es:", sueldoSemanal
            Fin Si
        Fin

        
6. Se requiere un algoritmo para determinar, de N cantidades, cuántas son cero, cuántas son menores a cero, y cuántas son mayores a cero. Realice el pseudocódigo para representarlo, utilizando el ciclo apropiado.



**1. Declaración de Variables:**

* **Metodología:** Se declaran e inicializan tres variables de tipo entero:
    * `contadorCero`: Se inicializa en 0 y se utilizará para almacenar la cantidad de números iguales a cero.
    * `contadorMenorCero`: Se inicializa en 0 y se utilizará para almacenar la cantidad de números menores que cero (negativos).
    * `contadorMayorCero`: Se inicializa en 0 y se utilizará para almacenar la cantidad de números mayores que cero (positivos).
    La inicialización en cero asegura que los contadores comiencen sin ningún valor previo acumulado.

**2. Entrada de Datos (Cantidad de Números):**


* **Metodología:**
    * Se utiliza la instrucción `Escribir` para mostrar un mensaje al usuario solicitando que ingrese el número de cantidades a evaluar, representado por la variable `N`.
    * La instrucción `Leer N` captura el valor ingresado por el usuario y lo almacena en la variable entera `N`. Este valor determinará cuántas veces se repetirá el proceso de lectura y clasificación de números.

**3. Procesamiento con Bucle:**

* **Objetivo:** Iterar un número específico de veces para leer y clasificar cada cantidad ingresada por el usuario.
* **Metodología:** Se utiliza una estructura de control de bucle `Para` que se ejecutará desde `i = 1` hasta `N` (inclusive). En cada iteración del bucle:
    * Se muestra un mensaje al usuario utilizando `Escribir`, indicando el número de la cantidad que se espera ingresar (utilizando el valor actual de la variable de control `i`).
    * La instrucción `Leer cantidad` captura el número ingresado por el usuario en cada iteración y lo almacena en la variable `cantidad`.

**4. Estructura de Clasificación:**


* **Metodología:** Dentro del bucle `Para`, se utiliza una estructura condicional anidada (`Si-Entonces-Sino Si-Entonces-Sino-Fin Si`) para clasificar cada valor de la variable `cantidad`:
    * **Si `cantidad` es igual a 0:** Se incrementa el `contadorCero` en 1 (`contadorCero = contadorCero + 1`).
    * **Sino (si `cantidad` no es igual a 0):** Se evalúa si es negativo:
        * **Si `cantidad` es menor que 0:** Se incrementa el `contadorMenorCero` en 1 (`contadorMenorCero = contadorMenorCero + 1`).
        * **Sino (si `cantidad` no es cero y no es menor que cero):** Se deduce que es mayor que cero (positivo), por lo que se incrementa el `contadorMayorCero` en 1 (`contadorMayorCero = contadorMayorCero + 1`).
    Esta estructura asegura que cada número ingresado se clasifique en una y solo una de las tres categorías.

**5. Salida de resultados para mostrar al usuario:**


* **Metodología:** Una vez que el bucle `Para` ha finalizado (es decir, se han evaluado las `N` cantidades), se utilizan varias instrucciones `Escribir` para mostrar los resultados:
    * Se imprime un encabezado "---- Resultados Finales ----" para organizar la salida.
    * Se muestra la cantidad de números iguales a cero, utilizando el valor almacenado en `contadorCero`.
    * Se muestra la cantidad de números menores a cero (negativos), utilizando el valor almacenado en `contadorMenorCero`.
    * Se muestra la cantidad de números mayores a cero (positivos), utilizando el valor almacenado en `contadorMayorCero`.



            Inicio
                // INICIALIZACIÓN DE CONTADORES // 
                contadorCero = 0         // Almacena la cantidad de ceros //
                contadorMenorCero = 0    // Almacena la cantidad de negativos // 
                contadorMayorCero = 0    // Almacena la cantidad de positivos // 

                // ENTRADA DE DATOS // 
                Escribir "Ingrese el número de cantidades a evaluar (N):"
                Leer N                   // Captura el total de números a procesar // 

                // PROCESAMIENTO CON BUCLE // 
                Para i = 1 Hasta N Hacer // Itera N veces
                    Escribir "Ingrese la cantidad ", i, ":"
                    Leer cantidad        // Guarda cada número // 

                    // ESTRUCTURA DE CLASIFICACIÓN
                    Si cantidad == 0 Entonces
                        contadorCero = contadorCero + 1  // Caso cero // 
                    Sino
                        Si cantidad < 0 Entonces
                            contadorMenorCero = contadorMenorCero + 1  // Caso negativo // 
                        Sino
                            contadorMayorCero = contadorMayorCero + 1  // Caso positivo // 
                        Fin Si
                    Fin Si
                Fin Para

                // SALIDA DE RESULTADOS // 
                Escribir "---- Resultados Finales ----"
                Escribir "Cantidades iguales a cero:", contadorCero
                Escribir "Cantidades menores a cero:", contadorMenorCero
                Escribir "Cantidades mayores a cero:", contadorMayorCero
            Fin

7. Se requiere un algoritmo para determinar cuánto ahorrará en pesos una persona diariamente, y en un año, si ahorra 3¢ el primero de enero, 9¢ el dos de enero, 27¢ el 3 de enero y así sucesivamente todo el año. Represente la solución mediante pseudocódigo.



**1. Declaración de Variables:**


* **Metodología:**
    * `ahorroDiario`: Se declara e inicializa con un valor de `0.03`. Esta variable representa la cantidad de dinero ahorrada en el día actual. El uso de un número decimal (`0.03`) es importante para representar correctamente las cantidades en centavos.
    * `ahorroTotal`: Se declara e inicializa con un valor de `0.0`. Esta variable actuará como un acumulador, guardando la suma total de los ahorros diarios a lo largo del año.
    * `diasEnAnio`: Se declara e inicializa con un valor de `365`. Esta constante representa el número de días en un año y determina la duración del bucle de simulación.

**2. Bucle Principal (Simulación Diaria):**

* **Metodología:** Se utiliza una estructura de control de bucle `Para` que se ejecutará desde `dia = 1` hasta `diasEnAnio` (365 iteraciones). En cada iteración, que representa un día del año:
    * **Mostrar Progreso Diario:** Se utiliza la instrucción `Escribir` para mostrar el número del día actual (`dia`) y la cantidad ahorrada en ese día (`ahorroDiario`). Esto permite visualizar cómo el ahorro diario va aumentando.
    * **Acumular al Total:** El valor actual de `ahorroDiario` se suma al `ahorroTotal` (`ahorroTotal = ahorroTotal + ahorroDiario`). Esta línea acumula el ahorro del día actual al total ahorrado hasta ese momento.
    * **Actualizar Ahorro para Mañana:** El valor de `ahorroDiario` se multiplica por 3 (`ahorroDiario = ahorroDiario * 3`). Esta es la regla clave del plan de ahorro: la cantidad ahorrada para el día siguiente es el triple de la cantidad ahorrada en el día actual.

**3. Resultado Final mostrar el ahorro del año:**


* **Metodología:** Una vez que el bucle `Para` ha completado sus 365 iteraciones (simulando el ahorro durante todo el año), se utiliza la instrucción `Escribir` para mostrar un mensaje indicando el ahorro total anual (`➤ Ahorro total anual: $`, `ahorroTotal`). El símbolo "➤" se utiliza aquí para destacar el resultado final.





    Inicio
        // DECLARACIÓN DE VARIABLES
        ahorroDiario = 0.03      // 3 centavos iniciales (día 1)
        ahorroTotal = 0.0        // Acumulador total
        diasEnAnio = 365         // Constante de días anuales

        // BUCLE PRINCIPAL (365 iteraciones)
        Para dia = 1 Hasta diasEnAnio Hacer
            // MOSTRAR PROGRESO DIARIO
            Escribir "Día ", dia, ": Ahorro = $", ahorroDiario
            
            // ACUMULAR AL TOTAL
            ahorroTotal = ahorroTotal + ahorroDiario  // Suma compuesta
            
            // ACTUALIZAR AHORRO PARA MAÑANA
            ahorroDiario = ahorroDiario * 3  // Regla de triplicación
        Fin Para

        // RESULTADO FINAL PARA MOSTRAR AL USUARIO // 
        Escribir "➤ Ahorro total anual: $", ahorroTotal
    Fin


8. Realice el algoritmo para determinar cuánto pagará una persona que adquiere N artículos, los cuales están de promoción. Considere que si su precio es mayor o igual a $200 se le aplica un descuento de 15%, y si su precio es mayor a $100, pero menor a $200, el descuento es de
  12%; de lo contrario, solo se le aplica 10%. Se debe saber cuál es el costo y el descuento que tendrá cada uno de los artículos y finalmente cuánto se pagará por todos los artículos obtenidos. Represente la solución mediante pseudocódigo.



**1. Variable de acumulación de costos:**


* **Metodología:** Se declara e inicializa la variable `totalPagar` con un valor de `0.0`. Esta variable de tipo decimal se utilizará para sumar el precio de cada artículo después de aplicar el descuento correspondiente.

**2. Entrada Principal (Cantidad de Artículos):**

.
* **Metodología:**
    * Se utiliza la instrucción `Escribir` para mostrar un mensaje al usuario solicitando que ingrese el número de artículos.
    * La instrucción `Leer N` captura el valor ingresado por el usuario y lo almacena en la variable entera `N`. Este valor determinará cuántas veces se repetirá el proceso de lectura del precio, cálculo del descuento y acumulación al total.

**3. Procesamiento por Artículo (Bucle):**


* **Metodología:** Se utiliza una estructura de control de bucle `Para` que se ejecutará desde `i = 1` hasta `N` (inclusive). En cada iteración, que representa el procesamiento de un artículo:
    * **Captura de Datos:**
        * Se utiliza la instrucción `Escribir` para solicitar al usuario que ingrese el precio del artículo actual (indicando el número del artículo `i`).
        * La instrucción `Leer precio` captura el valor ingresado por el usuario y lo almacena en la variable `precio`.
    * **Lógica de Descuentos (Escalonada):** Se aplica una serie de condiciones (`Si-Entonces-Sino Si-Entonces-Sino-Fin Si`) para determinar el porcentaje de descuento basado en el precio del artículo:
        * **Si `precio` es mayor o igual a 200:** Se calcula un descuento del 15% del precio (`descuento = precio * 0.15`).
        * **Sino Si `precio` es mayor que 100 (y menor que 200):** Se calcula un descuento del 12% del precio (`descuento = precio * 0.12`).
        * **Sino (si `precio` es menor o igual a 100):** Se calcula un descuento del 10% del precio (`descuento = precio * 0.10`).
    * **Cálculo de Precio Final:** Se calcula el precio del artículo después de aplicar el descuento, restando el valor del descuento al precio original (`costoConDescuento = precio - descuento`).
    * **Salida por Artículo:** Se utiliza la instrucción `Escribir` para mostrar un resumen de la información del artículo actual, incluyendo el precio original, el descuento aplicado y el precio con descuento.
    * **Acumulación del Total:** El `costoConDescuento` del artículo actual se suma a la variable `totalPagar` (`totalPagar = totalPagar + costoConDescuento`).

**4. Resultado Final:**


* **Metodología:** Una vez que el bucle `Para` ha completado sus `N` iteraciones (es decir, se han procesado todos los artículos), se utilizan instrucciones `Escribir` para mostrar el resultado final:
    * Se imprime una línea de separación (`=================================`) para destacar el resultado final.
    * Se muestra el mensaje "TOTAL A PAGAR: $" seguido del valor acumulado en la variable `totalPagar`.



        Inicio
            // INICIALIZACIÓN //
            totalPagar = 0.0  // Variable acumuladora del total //
            
            // ENTRADA PRINCIPAL
            Escribir "Ingrese el número de artículos:"
            Leer N  // Cantidad total de artículos a procesar // 

            // PROCESAMIENTO POR ARTÍCULO // 
            Para i = 1 Hasta N Hacer
                // CAPTURA DE DATOS // 
                Escribir "Ingrese el precio del artículo ", i, ":"
                Leer precio  // Precio bruto del artículo // 

                // LÓGICA DE DESCUENTOS (ESCALONADA) // 
                Si precio >= 200 Entonces
                    descuento = precio * 0.15  // 15% para artículos caros// 
                Sino Si precio > 100 Entonces
                    descuento = precio * 0.12  // 12% para precios medios//
                Sino
                    descuento = precio * 0.10  // 10% para artículos //económicos
                Fin Si

                // CÁLCULO DE PRECIO FINAL
                costoConDescuento = precio - descuento
                
                // SALIDA POR ARTÍCULO
                Escribir "--- Artículo ", i, " ---"
                Escribir "Precio original: $", precio
                Escribir "Descuento aplicado: $", descuento
                Escribir "Precio con descuento: $", costoConDescuento

                // ACUMULACIÓN DEL TOTAL // 
                totalPagar = totalPagar + costoConDescuento
            Fin Para

            // RESULTADO FINAL
            Escribir "================================="
            Escribir "TOTAL A PAGAR: $", totalPagar
        Fin

9. Realice un algoritmo y represéntelo mediante pseudocódigo para obtener una función exponencial, la cual está dada por:
    
    $𝑒^𝑥 = 1+\frac x {1!} + \frac {x^2}{2!}+ \frac {x^3}{3!}+ …$
## Análisis y Metodología de Solución del Pseudocódigo para Aproximar eˣ usando la Serie de Taylor



**1. Entrada de Datos valor que desea del exponente:**


* **Metodología:**
    * Se utiliza la instrucción `Escribir` para solicitar al usuario que ingrese el valor de $x$.
    * La instrucción `Leer x` captura el valor ingresado por el usuario y lo almacena en la variable `x`.
    * De manera similar, se solicita al usuario que ingrese la precisión deseada (el número de términos de la serie).
    * La instrucción `Leer precision` captura este valor y lo almacena en la variable `precision`.

**2. Inicialización:**


* **Metodología:**
    * `resultado`: Se inicializa en `1.0`. Esto representa el primer término de la serie de Taylor para $e^x$, que es $\frac{x^0}{0!} = 1$.
    * `termino`: Se inicializa en `1.0`. Esta variable almacenará el valor del término actual de la serie que se está calculando en cada iteración. Inicialmente, corresponde al primer término.
    * `factorial`: Se inicializa en `1`. Esta variable se utilizará para calcular el factorial del índice del término en cada iteración (recordando que $0! = 1$).

**3. Cálculo Iterativo (Serie de Taylor):**

* **Objetivo:** Calcular y sumar los siguientes términos de la serie de Taylor hasta alcanzar la precisión deseada.
* **Metodología:** Se utiliza una estructura de control de bucle `Para` que se ejecutará desde `i = 1` hasta `precision` (inclusive). En cada iteración, que representa el cálculo de un nuevo término de la serie:
    * `factorial = factorial * i`: Se calcula el factorial del número actual de la iteración (`i`). En la primera iteración, calcula $1!$, en la segunda $2!$, y así sucesivamente.
    * `termino = (x^i) / factorial`: Se calcula el valor del $i$-ésimo término de la serie de Taylor para $e^x$, que es $\frac{x^i}{i!}$. Se utiliza el valor de $x$ ingresado por el usuario y el factorial calculado en el paso anterior.
    * `resultado = resultado + termino`: El valor del término actual (`termino`) se suma al `resultado` acumulativo. De esta manera, se van sumando los términos de la serie para obtener una aproximación cada vez más precisa de $e^x$.

**4. Resultado Final:**


* **Metodología:** Una vez que el bucle `Para` ha completado sus iteraciones (se han sumado la cantidad de términos especificada por `precision`), se utiliza la instrucción `Escribir` para mostrar el resultado final. Se incluye el valor de $x$, la cantidad de términos utilizados (`precision`), y la aproximación calculada de $e^x$ almacenada en la variable `resultado`.




        Inicio
            // ENTRADA DE DATOS // 
            Escribir "Ingrese el valor de x:" 
            Leer x  // Exponente para eˣ // 
            Escribir "Ingrese la precisión deseada (número de términos):"
            Leer precision  // Cantidad de términos de la serie // 

            // INICIALIZACIÓN // 
            resultado = 1.0     // Primer término (n=0: x⁰/0! = 1) //
            termino = 1.0       // Valor inicial del término // 
            factorial = 1       // Inicia factorial (0! = 1) // 

            // CÁLCULO ITERATIVO // 
            Para i = 1 Hasta precision Hacer
                factorial = factorial * i  // Calcula i! (1!, 2!, 3!,...)
                termino = (x^i) / factorial  // Fórmula del término n-ésimo // 
                resultado = resultado + termino  // Suma acumulativa // 
            Fin Para

            // RESULTADO FINAL // 
            Escribir "Aproximación de e^", x, " con ", precision, " términos: ", resultado
        Fin




10. Realice un algoritmo para obtener el seno de un ángulo y represéntelo mediante pseudocódigo. Utilice la siguiente ecuación:


$Sen x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...$


1.  **Inicializar las variables** necesarias: la aproximación del seno (comenzando con el primer término), el valor del término actual y el signo para la alternancia.
2.  **Iterar un número de veces igual a la precisión deseada:**
    * **Calcular el siguiente término** de la serie de Taylor utilizando una relación de recurrencia para mayor eficiencia.
    * **Sumar o restar el término actual** al resultado acumulativo, basándose en el signo correspondiente.
    * **Alternar el signo** para el siguiente término.
3.  **Devolver el valor acumulado**, que es la aproximación de $\sin(x)$.



        Función calcularSeno(x, precision):
            // INICIALIZACIÓN // 
            seno = x           # Primer término de la serie (x)
            termino = x        # Valor inicial del término
            signo = -1         # Alternador de signo (comienza en -1 para el segundo término)
            
            // CÁLCULO ITERATIVO
            Para i desde 1 hasta precision Hacer:
                // Cálculo del término actual (x^(2n+1)/(2n+1)!)
                termino = termino * x * x / ((2 * i) * (2 * i + 1))
                
                // Suma/resta alternante al resultado
                seno = seno + signo * termino
                
                // Alternar signo para siguiente término
                signo = -signo
            
            Fin Para
            
            // RESULTADO FINAL
            Retornar seno
        Fin Función
