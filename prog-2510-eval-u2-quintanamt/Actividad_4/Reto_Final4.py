# Declarar variables para fecha de nacimiento y fecha actual
dia_nac = int(input("Ingrese su día de nacimiento (1-31): "))
mes_nac = int(input("Ingrese su mes de nacimiento (1-12): "))
anio_nac = int(input("Ingrese su año de nacimiento: "))

dia_actual = int(input("Ingrese el día actual (1-31): "))
mes_actual = int(input("Ingrese el mes actual (1-12): "))
anio_actual = int(input("Ingrese el año actual: "))

# Calcular la edad inicial
edad = anio_actual - anio_nac

# Verificar si ya cumplió años este año
if mes_actual < mes_nac:
    edad -= 1
    yaCelebro = False
elif mes_actual == mes_nac:
    if dia_actual < dia_nac:
        edad -= 1
        yaCelebro = False
    elif dia_actual == dia_nac:
        print("¡Feliz Cumpleaños!")
        yaCelebro = True
    else:
        yaCelebro = True
else:
    yaCelebro = True

# Mostrar la edad y el estado del cumpleaños
print("Edad actual:", edad)
if yaCelebro:
    print("Ya ha celebrado su cumpleaños este año.")
else:
    print("Aún no ha celebrado su cumpleaños este año.")