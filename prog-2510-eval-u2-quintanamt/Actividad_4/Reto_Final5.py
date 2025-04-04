# Pedir las horas trabajadas y el pago por hora
horasTrabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
pagoPorHora = float(input("Ingrese el pago por hora: "))

# Inicializar el sueldo semanal
sueldoSemanal = 0

# Calcular el sueldo basado en las horas trabajadas
if horasTrabajadas <= 40:
    sueldoSemanal = horasTrabajadas * pagoPorHora
elif horasTrabajadas <= 45:
    sueldoSemanal = 40 * pagoPorHora + (horasTrabajadas - 40) * pagoPorHora * 2
elif horasTrabajadas <= 50:
    sueldoSemanal = 40 * pagoPorHora + 5 * pagoPorHora * 2 + (horasTrabajadas - 45) * pagoPorHora * 3
else:
    print("No está permitido trabajar más de 50 horas.")
    sueldoSemanal = 0

# Mostrar el sueldo semanal
if sueldoSemanal > 0:
    print("El sueldo semanal es:", sueldoSemanal)