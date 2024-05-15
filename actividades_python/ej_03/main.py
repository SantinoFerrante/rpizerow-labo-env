from gpiozero import LED, Buzzer
from time import sleep

# Declaración de componentes
led_verde = LED(13)
led_rojo = LED(19)
led_azul = LED(26)
buzzer = Buzzer(22)

while True:
    # Solicitar entrada de comando al usuario
    command = input("Ingrese comando (Sintaxis: comando.opción): ")

    # Opciones de comando, con manejo de errores
    if command == "buzzer.encender":
        buzzer.on()
    elif command == "buzzer.apagar":
        buzzer.off()
    elif command == "rgb.rojo":
        led_rojo.on()
        led_verde.off()
        led_azul.off()
    elif command == "rgb.verde":
        led_verde.on()
        led_rojo.off()
        led_azul.off()
    elif command == "rgb.azul":
        led_azul.on()
        led_rojo.off()
        led_verde.off()
    elif command == "rgb.cyan":
        led_azul.on()
        led_verde.on()
        led_rojo.off()
    elif command == "rgb.magenta":
        led_azul.on()
        led_rojo.on()
        led_verde.off()
    elif command == "rgb.amarillo":
        led_verde.on()
        led_rojo.on()
        led_azul.off()
    else:
        # Manejo de errores para comandos incorrectos
        print("Error: Comando no reconocido")
