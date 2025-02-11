1. Escribe un párrafo explicando, en tus propias palabras, cómo se representan los datos en una computadora. Por ejemplo, ¿cómo se ingresan números, letras, imágenes a una computadora?


        En una computadora, todos los datos, ya sean números, letras, imágenes o sonidos, se representan mediante el sistema binario, que utiliza únicamente dos dígitos: 0 y 1. Estos dígitos, llamados bits, son la unidad más básica de información. Los números se convierten a binario mediante procesos de conversión entre sistemas numéricos, como el decimal y el binario. Las letras y caracteres se representan mediante códigos como ASCII o Unicode, donde cada carácter tiene una combinación única de bits. Las imágenes se descomponen en píxeles, y cada píxel se representa con valores binarios que indican su color y brillo. De manera similar, los sonidos se digitalizan y se convierten en secuencias de bits que representan ondas sonoras. En resumen, la computadora traduce toda la información a combinaciones de 0 y 1, lo que permite su procesamiento, almacenamiento y transmisión.

2. Luego de realizar el ejercicio 1, escribe tus conclusiones acerca de la pregunta planteada en la Figura 2. ¿Cuántos estados diferentes pueden ser representados por N variables binarias?


        En la Figura 2 se plantea la pregunta: ¿Cuántos estados diferentes se pueden representar usando N bits? Tras analizar el ejercicio, se concluye que el número de estados diferentes que se pueden representar con N bits sigue una progresión exponencial dada por la formula 2^N. Esto se debe a que cada bit añade una nueva dimensión binaria (0 o 1), duplicando las combinaciones posibles. Por lo tanto, la representación matemática para calcular el número de estados es 2^N, donde N es el número de bits. 

3. ¿Cuáles son las unidades de almacenamiento de datos que se utilizan en computación? Crea una tabla donde muestres estas unidades con sus prefijos. En este caso me refiero a KiloByte, MegaByte, etc. 



### Unidades de Almacenamiento de Datos en Computación

| Unidad    | Símbolo | Equivalencia               |
|-----------|---------|----------------------------|
| Bit       | b       | Unidad básica (0 o 1)      |
| Byte      | B       | 8 bits                     |
| Kilobyte  | KB      | 1,024 bytes                |
| Megabyte  | MB      | 1,024 kilobytes            |
| Gigabyte  | GB      | 1,024 megabytes            |
| Terabyte  | TB      | 1,024 gigabytes            |
| Petabyte  | PB      | 1,024 terabytes            |
| Exabyte   | EB      | 1,024 petabytes            |
| Zettabyte | ZB      | 1,024 exabytes             |
| Yottabyte | YB      | 1,024 zettabytes           |

4. Incluye un pequeño resumen, de un par de renglones, donde menciones la importancia del trabajo de George Bool en este tópico.

        George Boole sentó las bases de la lógica booleana, un sistema algebraico que utiliza valores binarios (verdadero/falso o 1/0) para representar y manipular proposiciones lógicas. Su trabajo es fundamental en la computación moderna, ya que permite el diseño de circuitos electrónicos, la programación de software y la toma de decisiones en sistemas digitales. Sin la lógica booleana, no sería posible el funcionamiento de las computadoras tal como las conocemos hoy.


# Conversion Entre binarios y decimales 

## Respuestas a los Ejercicios


### Ejercicio 1 (Estados representados con N bits):
Con **N bits**, se pueden representar **2^N** estados diferentes. Por ejemplo:

- **2 bits**: 2^2 = 4 estados.
- **3 bits**: 2^3 = 8 estados.
- **4 bits**: 2^4 = 16 estados.

---

### Ejercicio 2 (Conversión de binario a decimal):

| Binario       | Decimal |
|---------------|---------|
| `1010101010`  | 682     |
| `11111`       | 31      |
| `10000000`    | 128     |
| `100100100`   | 292     |
| `111000`      | 56      |

---

### Ejercicio 3 (Conversión de decimal a binario):

| Decimal | Binario        |
|---------|----------------|
| 127     | `01111111`     |
| 246     | `11110110`     |
| 1025    | `10000000001`  |
| 354     | `101100010`    |
| 187     | `10111011`     |

## Tipos de Datos 

#### **2. ¿Por qué crees que en las computadoras se usa una representación binaria en lugar de otro tipo de representación?**


        En las computadoras se usa la representación binaria porque es la más simple y eficiente para los sistemas electrónicos. Los dispositivos digitales funcionan con dos estados: encendido (1) y apagado (0), lo que corresponde directamente con el sistema binario. Esta simplicidad permite mayor fiabilidad, menor costo de fabricación y facilidad de implementación en circuitos electrónicos. Además, las operaciones lógicas y aritméticas son más rápidas y precisas en binario.

### **3. Actividad de investigación (para la bitácora)**

Investiga los diferentes tipos de datos que se utilizan en varios lenguajes de programación (por ejemplo, C, Java, Python). Ten en cuenta cómo cada lenguaje define los números enteros, los decimales (o flotantes), las letras del alfabeto, las cadenas de texto, valores booleanos, entre otros. Investiga qué nombres se asignan y qué abreviaciones se utilizan en cada lenguaje.

### **4. Organización de resultados**

Con la información recolectada, organiza los datos en una tabla que incluya:

- **Nombre de la variable**
- **Abreviación (si existe)**
- **Características principales** (rango, tipo de valor, etc.)

##


A continuación se presenta una comparativa de los tipos de datos comunes en los lenguajes de programación **C**, **Java** y **Python**, incluyendo cómo se definen números enteros, decimales, caracteres, cadenas de texto y valores booleanos.

---

## **Tipos de datos en C**

| **Tipo de dato** | **Nombre**          | **Abreviación** | **Características**                                                                 |
|------------------|---------------------|-----------------|-------------------------------------------------------------------------------------|
| Entero           | `int`              | -               | Números enteros de 32 bits (rango: -2,147,483,648 a 2,147,483,647).                |
| Decimal          | `float`            | -               | Números de punto flotante de 32 bits (precisión simple).                           |
| Decimal          | `double`           | -               | Números de punto flotante de 64 bits (precisión doble).                            |
| Carácter         | `char`             | -               | Un solo carácter (8 bits, rango: -128 a 127 o 0 a 255).                            |
| Cadena de texto  | `char[]`           | -               | Arreglo de caracteres (terminado con `\0`).                                        |
| Booleano         | `bool`             | -               | Valores `true` o `false` (requiere incluir la biblioteca `<stdbool.h>`).           |

---

## **Tipos de datos en Java**

| **Tipo de dato** | **Nombre**          | **Abreviación** | **Características**                                                                 |
|------------------|---------------------|-----------------|-------------------------------------------------------------------------------------|
| Entero           | `int`              | -               | Números enteros de 32 bits (rango: -2,147,483,648 a 2,147,483,647).                |
| Entero           | `long`             | -               | Números enteros de 64 bits (rango más amplio).                                     |
| Decimal          | `float`            | -               | Números de punto flotante de 32 bits (precisión simple).                           |
| Decimal          | `double`           | -               | Números de punto flotante de 64 bits (precisión doble).                            |
| Carácter         | `char`             | -               | Un solo carácter (16 bits, usando Unicode).                                        |
| Cadena de texto  | `String`           | -               | Secuencia de caracteres (inmutable).                                               |
| Booleano         | `boolean`          | -               | Valores `true` o `false`.                                                          |

---

### **Tipos de datos en Python**

| **Tipo de dato** | **Nombre**          | **Abreviación** | **Características**                                                                 |
|------------------|---------------------|-----------------|-------------------------------------------------------------------------------------|
| Entero           | `int`              | -               | Números enteros de precisión arbitraria (no tiene límite de tamaño).               |
| Decimal          | `float`            | -               | Números de punto flotante de 64 bits (precisión doble).                            |
| Carácter         | `str` (1 carácter) | -               | No existe un tipo específico para caracteres; se usa `str` con longitud 1.         |
| Cadena de texto  | `str`              | -               | Secuencia de caracteres (inmutable).                                               |
| Booleano         | `bool`             | -               | Valores `True` o `False`.                                                          |

---

### Observaciones:
- En **C**, los tipos de datos tienen un tamaño fijo y requieren gestión manual de memoria.
- En **Java**, los tipos de datos son más robustos y están orientados a objetos, con manejo automático de memoria para objetos como `String`.
- En **Python**, los tipos de datos son dinámicos y no requieren declaración explícita de tipos, lo que simplifica el código pero puede afectar el rendimiento en comparación con C y Java.

---

### Ejemplos de uso:

```c
# En C:

int edad = 25;
float precio = 19.99;
char letra = 'A';
char nombre[] = "Juan";
bool esValido = true;

# Java: 

int edad = 25;
double precio = 19.99;
char letra = 'A';
String nombre = "Juan";
boolean esValido = true;

# Python: 

edad = 25
precio = 19.99
letra = 'A'
nombre = "Juan"
es_valido = True


```

## **5. Ejercicio de cálculo de espacio en memoria**

Imagina que necesitas almacenar la siguiente información en un programa:

- Un identificador numérico (número entero)
- Una temperatura (valor de punto flotante)
- Un valor lógico (dato booleano)
- Un texto con 10 caracteres.

Se almacena la información cada 10 segundos durante 24 horas. Calcula cuánto espacio total se requiere en memoria para almacenar estos datos. Describe el procedimiento y muestra el resultado final.

## **5. Ejercicio de cálculo de espacio en memoria**

Para calcular el espacio total en memoria requerido, seguimos estos pasos:

1. **Tamaño de cada tipo de dato:**
   - Identificador numérico (entero): 4 bytes.
   - Temperatura (punto flotante): 4 bytes.
   - Valor lógico (booleano): 1 byte.
   - Texto de 10 caracteres: 10 bytes.

2. **Tamaño total de un registro:**
   - Identificador: 4 bytes.
   - Temperatura: 4 bytes.
   - Booleano: 1 byte.
   - Texto: 10 bytes.
   - **Total por registro: 19 bytes.**

3. **Número de registros en 24 horas:**
   - Cada registro se almacena cada 10 segundos.
   - En 24 horas hay 86,400 segundos.
   - Número de registros: 86,400 / 10 = 8,640 registros.

4. **Espacio total en memoria:**
   - Espacio total = 19 bytes × 8,640 = 164,160 bytes.

5. **Conversión a una unidad más legible:**
   - 164,160 bytes = 160.31 KB.

### **Resultado final:**
El espacio total requerido en memoria para almacenar los datos durante 24 horas es **164,160 bytes** (aproximadamente **160.31 KB**).


## **6. Conclusión**

En esta actividad, aprendí cómo se calcula el espacio en memoria necesario para almacenar diferentes tipos de datos en un programa. A través del ejercicio, comprendí que cada tipo de dato (entero, flotante, booleano y texto) tiene un tamaño específico en bytes, y que el espacio total requerido depende de la frecuencia con la que se almacenan estos datos.

Además, reforcé mi entendimiento sobre la importancia de la representación binaria en las computadoras. Los sistemas digitales utilizan el sistema binario porque es eficiente y fácil de implementar en hardware, ya que solo requiere dos estados (0 y 1). Esto permite que las operaciones sean rápidas y confiables.

Finalmente, el cálculo del espacio en memoria me mostró cómo optimizar el uso de recursos al programar, especialmente cuando se manejan grandes volúmenes de datos. Aprendí que es crucial considerar el tamaño de los datos y la frecuencia de almacenamiento para evitar problemas de rendimiento o sobrecarga en la memoria.

En resumen, esta actividad me ayudó a entender mejor cómo las computadoras manejan y almacenan la información, y cómo podemos calcular y optimizar el uso de la memoria en nuestros programas.