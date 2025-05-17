# Reto 3: Calculadora de Tiempo 
# Problema: Crear una calculadora que convierta segundos en horas, minutos y segundos. ⏱️
# Descripción: El programa debe solicitar al usuario una cantidad de segundos y convertirlos a un formato de tiempo legible, 
# expresando las horas, minutos y segundos correspondientes. Esta herramienta es útil para trabajar con 
# duraciones de tiempo en programación, análisis de datos y aplicaciones multimedia.
# Casos de prueba:
# 3661 segundos → 1 hora, 1 minuto, 1 segundo ⏱️
# 7500 segundos → 2 horas, 5 minutos, 0 segundos ⏱️
# 45 segundos → 0 horas, 0 minutos, 45 segundos ⏱️
# 10800 segundos → 3 horas, 0 minutos, 0 segundos ⏱️
# 3723 segundos → 1 hora, 2 minutos, 3 segundos ⏱️
# Pista: Utiliza la división entera (//) y el operador módulo (%) para separar las horas, minutos y segundos. Por ejemplo, horas = segundos // 3600. 🧮


# 1 hora = 3600 segundos
# 1 minuto = 60 segundos


def time_calculator():
    #captura de input
    input_time = input("Ingresa una cantidad de segundos: ")
    # convertimos a int el input 
    time = int(input_time)

    # el simbolo => //  divide y retorna la parte entera
    # ejemp: 3601 // 3600 = 1 
    hours = time // 3600
    
    # 1. obtenemos el residuo  dividiendo el valor entre 3600 (1 hora) 
    # 2. dividimos entre 60 (minutos)  obteniendo la parte entera
    # ejemp: ( 3659 % 3600 ) // 60  => 59 // 60 => 0 minutos
    # ejemp: ( 3670 % 3600 ) // 60  => 70 // 60 => 1 minuto

    minutes = (time % 3600) // 60

    # Obtenemos el residuo del valor ingresado divido entre 60 (segundos)
    seconds = time % 60

    # declaramos los textos
    text_hour = "hora"
    text_minute = "minutos"
    text_second = "segundo"

   # validaciones de texto
    if hours > 1 or hours == 0: 
        text_hour = "horas"

    if minutes > 1 or minutes == 0: 
        text_minute = "minutos"

    if seconds > 1 or seconds == 0: 
        text_second = "segundos"

    # imprimimos resultado
    print("El resultado es: ", hours, " ", text_hour, ", ", minutes, " ", text_minute, ", ", seconds, " ", text_second )


time_calculator()