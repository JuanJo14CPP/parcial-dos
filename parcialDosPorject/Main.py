salarioBaseMensual = input(print("Salario base mensual $: "))
cargoEmpleado = input(print("Cargo empleado: "))
nivelDesempeño = input(print("Nivel de Desempeño: "))

def nivel_directivo (directivo_alto, directivo_medio):

    if directivo_alto == 1:
        bonificacion1 = "Alto"
    elif directivo_medio == 2:
        bonificacion1 = "Medio"
    else:
        return None

    total_sin_bonificacion1 = salarioBaseMensual

    if directivo_alto == 1:
        bonificacion_directivo = round(total_sin_bonificacion1 + directivo_alto)
    elif directivo_medio == 2:
        bonificacion_directivo = round(total_sin_bonificacion1 + directivo_medio)
    else:
        bonificacion_directivo = 0
    total1 = round(total_sin_bonificacion1 + bonificacion_directivo)

    return bonificacion1, total1, directivo_alto, directivo_medio, bonificacion_directivo

def nivel_operativo (operativo_alto, operativo_medio):
    if operativo_alto == 3:
        bonificacion2 = "Alto"
    elif operativo_medio == 4:
        bonificacion2 = "Medio"
    else:
        return None

    total_sin_bonificacion2 = salarioBaseMensual

    if operativo_alto == 3:
        bonificacion_operativo = round(total_sin_bonificacion2 + operativo_alto)
    elif operativo_medio == 4:
        bonificacion_operativo = round(total_sin_bonificacion2 + operativo_medio)
    else:
        bonificacion_operativo = 0
    total2 = round(total_sin_bonificacion2 + bonificacion_operativo)

    return bonificacion2, total2, operativo_alto, operativo_medio

def mensaje1 (total1, bonificacion_directivo):
    print("-----Resumen del Pago-----")
    return(f"Cargo: {cargoEmpleado}\n"
    f"Nivel de Desempeño: {nivelDesempeño}\n"
    f"Salario Base: {salarioBaseMensual}\n"
    f"Bonificacion: {bonificacion_directivo}\n"
    f"Total a Recibir: {total1}\n")

def mensaje2 (total2, bonificacion_operativo):
    print("-----Resumen del Pago-----")
    return(f"Cargo: {cargoEmpleado}\n"
    f"Nivel de Desempeño: {nivelDesempeño}\n"
    f"Salario Base: {salarioBaseMensual}\n"
    f"Bonificacion: {bonificacion_operativo}\n"
    f"Total a Recibir: {total2}\n")




