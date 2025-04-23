def Calculadora (budget, rate):
    result = budget/rate
    return result

presupuesto = float(input("Insertar el presupuesto actual en dolares: "))
tasa = float(input("Insertar la tasa de cambio: "))

print("El dinero total es: " + str(Calculadora(presupuesto, tasa)))