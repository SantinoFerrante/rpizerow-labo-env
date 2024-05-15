from gpiozero import LED, Button  # Importa las funciones LED y Button desde gpiozero
from signal import pause          # Importa la función pause desde signal
from time import sleep            # Importa la función sleep desde time

# Declara qué LED utilizar y su respectivo color
led_verde = LED(13)   # Declara un objeto LED para el LED verde en el pin GPIO 13
led_rojo = LED(19)    # Declara un objeto LED para el LED rojo en el pin GPIO 19
led_azul = LED(26)    # Declara un objeto LED para el LED azul en el pin GPIO 26

# Declara un bucle while True que enciende los LEDs durante un tiempo determinado y luego los apaga
while True:
    led_rojo.on()     # Enciende el LED rojo
    sleep(1)          # Espera 1 segundo
    led_rojo.off()    # Apaga el LED rojo
    
    led_azul.on()     # Enciende el LED azul
    sleep(0.5)        # Espera 0.5 segundos
    led_azul.off()    # Apaga el LED azul

    led_verde.on()    # Enciende el LED verde
    sleep(0.25)       # Espera 0.25 segundos
    led_verde.off()   # Apaga el LED verde

pause()  # Espera hasta que se reciba una señal de interrupción para finalizar el programa
