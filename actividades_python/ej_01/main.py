from gpiozero import LED, Button #se asignan librerias
from signal import pause #se asignan librerias

led = LED(26) #le asigno pin 26 al led azul
button = Button(18) #asigno el pin 18 al bot

button.when_pressed = led.on #cuando el boton esta apretado el led se enciende 
button.when_released = led.off #cuando el botn no esta precionado el led esta apagado

pause()
