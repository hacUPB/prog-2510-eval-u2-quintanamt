## Ejercicio 1.

Investiga cuáles son los símbolos que se utilizan para representar cada operación de un algorimo con un diagrama de flujo. Asegúrate de que la fuente es confiable, discute lo que encontraste con tus compañeros y con el profe. Cuando estés seguro/a de tener los símbolos correctos, consigna la información en la bitácora.

    Los diagramas de flujo son herramientas visuales que representan algoritmos o procesos mediante símbolos estandarizados. Cada símbolo tiene un significado específico y se utiliza para representar una acción, decisión, entrada, salida, o conexión dentro del flujo del proceso. A continuación, se presentan los símbolos más comunes utilizados en diagramas de flujo, basados en fuentes confiables y estándares internacionales:
---

    
<h4>1. Óvalo (Elipse)</h4>
<ul>
    <li><strong>Nombre:</strong> Inicio/Final.</li>
    <li><strong>Uso:</strong> Representa el inicio o el final de un proceso.</li>
    <li><strong>Descripción:</strong> Siempre se utiliza para indicar el punto de partida ("Inicio") o el punto de finalización ("Fin") del algoritmo.</li>
</ul>
<hr>

<h4>2. Rectángulo</h4>
<ul>
    <li><strong>Nombre:</strong> Proceso.</li>
    <li><strong>Uso:</strong> Representa una acción o un paso en el proceso.</li>
    <li><strong>Descripción:</strong> Se utiliza para indicar operaciones como cálculos, asignaciones de variables, o cualquier acción que transforme datos.</li>
</ul>
<hr>

<h4>3. Rombo</h4>
<ul>
    <li><strong>Nombre:</strong> Decisión.</li>
    <li><strong>Uso:</strong> Representa una condición o pregunta que requiere una respuesta binaria (Sí/No, Verdadero/Falso).</li>
    <li><strong>Descripción:</strong> Tiene una entrada y dos salidas, que representan los dos posibles caminos que puede tomar el flujo del proceso.</li>
</ul>
<hr>

<h4>4. Flechas</h4>
<ul>
    <li><strong>Nombre:</strong> Conector de flujo.</li>
    <li><strong>Uso:</strong> Indica la dirección del flujo del proceso.</li>
    <li><strong>Descripción:</strong> Conectan los símbolos y muestran el orden en que se ejecutan las acciones.</li>
</ul>
<hr>

<h4>5. Paralelogramo</h4>
<ul>
    <li><strong>Nombre:</strong> Entrada/Salida.</li>
    <li><strong>Uso:</strong> Representa la entrada de datos (por ejemplo, desde el usuario) o la salida de resultados (por ejemplo, mostrar información en pantalla).</li>
    <li><strong>Descripción:</strong> Se utiliza para operaciones de lectura o escritura de datos.</li>
</ul>
<hr>

<h4>6. Círculo pequeño</h4>
<ul>
    <li><strong>Nombre:</strong> Conector.</li>
    <li><strong>Uso:</strong> Representa una conexión entre dos partes del diagrama de flujo, especialmente cuando el diagrama se divide en varias páginas o secciones.</li>
    <li><strong>Descripción:</strong> Se utiliza para evitar cruces de líneas y mantener la claridad del diagrama.</li>
</ul>
<hr>

<h4>7. Rectángulo con líneas verticales</h4>
<ul>
    <li><strong>Nombre:</strong> Subproceso.</li>
    <li><strong>Uso:</strong> Representa un proceso

---


*Referencias bibliograficas:*
*International Organization for Standardization (ISO). (1985). ISO 5807: Information processing — Documentation symbols and conventions for data, program and system flowcharts, program network charts and system resources charts.*

*American National Standards Institute (ANSI). (1970). ANSI X3.5: Flowchart Symbols and Their Usage in Information Processing.*

*Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.*


![alt text](<../Captura de pantalla 2025-02-11 a la(s) 3.09.58 p.m..png>)

*Imagen obtenida de "Problemario de algoritmos resueltos con diagramas de flujo y pseudocodigo*

## Ejercicio 2 
Analicemos el siguiente problema y representemos su solución mediante un algoritmo secuencial.

- Construye un algoritmo que, al recibir como datos **el ID** del empleado y los seis primeros sueldos del año, calcule el ingreso total semestral y el promedio mensual, e imprima el ID del empleado, el ingreso total y el promedio mensual.

### Algoritmo Calcular Ingresos Empleado ###

    // Declaración de variables
    Definir ID_Empleado Como Cadena
    Definir Sueldo1, Sueldo2, Sueldo3, Sueldo4, Sueldo5, Sueldo6 Como Real
    Definir IngresoTotal, PromedioMensual Como Real

    // Entrada de datos
    Escribir "Ingrese el ID del empleado:"
    Leer ID_Empleado

    Escribir "Ingrese el sueldo del mes 1:"
    Leer Sueldo1

    Escribir "Ingrese el sueldo del mes 2:"
    Leer Sueldo2

    Escribir "Ingrese el sueldo del mes 3:"
    Leer Sueldo3

    Escribir "Ingrese el sueldo del mes 4:"
    Leer Sueldo4

    Escribir "Ingrese el sueldo del mes 5:"
    Leer Sueldo5

    Escribir "Ingrese el sueldo del mes 6:"
    Leer Sueldo6

    // Procesamiento de datos
    IngresoTotal = Sueldo1 + Sueldo2 + Sueldo3 + Sueldo4 + Sueldo5 + Sueldo6
    PromedioMensual = IngresoTotal / 6

    // Salida de resultados
    Escribir "ID del empleado: ", ID_Empleado
    Escribir "Ingreso total semestral: ", IngresoTotal
    Escribir "Promedio mensual: ", PromedioMensual

FinAlgoritmo
