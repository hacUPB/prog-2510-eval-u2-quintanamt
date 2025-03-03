# Pedir la cantidad de metros
#Convierte cadena de texto en un número decimal
metros = float(input("Ingrese la cantidad de metros de tela que necesita: "))

# Convertir metros a pulgadas (1 metro = 39.3701 pulgadas)
pulgadas = metros / 0.0254

# Mostrar el resultado
print("Debe pedir", pulgadas, "pulgadas de tela.")