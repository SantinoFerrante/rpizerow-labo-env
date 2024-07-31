import ADS1x15
import math 
from gpiozero import PWMLED
import time

# Inicializa el objeto ADS1115 en el bus I2C 1 y la dirección 0x48
adc = ADS1x15.ADS1115(1, 0x48)
adc.setMode(adc.MODE_SINGLE)
adc.setGain(adc.PGA_4_096V)
conv_fac = adc.toVoltage()  # Factor de conversión para voltaje
led_b = PWMLED(26)  # LED azul conectado al pin GPIO 26
led_r = PWMLED(19)  # LED rojo conectado al pin GPIO 19
v_ref = 3.3  # Voltaje de referencia de 3.3V
v_therm = 0
r_therm = 0
temp_c = 0
r_ref = 10000  # Resistencia de referencia
beta = 3977  # Constante beta para el termistor

while True:
    p_val = adc.readADC(3)  # Lee el valor del ADC en el canal 3
    t_val = adc.readADC(1)  # Lee el valor del ADC en el canal 1
    p_volt = p_val * conv_fac  # Convierte el valor ADC del potenciómetro a voltaje
    t_volt = t_val * conv_fac  # Convierte el valor ADC del termistor a voltaje

    # Calcula el voltaje en el termistor
    v_therm = (3.3 * t_volt) / 4095
    r_therm = r_ref / ((v_ref / v_therm) - 1)  # Calcula la resistencia del termistor
    temp_k = beta / (math.log10(r_therm / r_ref) + (beta / 298.0))  # Calcula la temperatura en Kelvin
    temp_c = temp_k - 273.15  # Convierte la temperatura a grados Celsius

    # Control del LED rojo basado en la diferencia de voltaje entre p_volt y t_volt
    if p_volt > t_volt:
        led_r.value = (p_volt - t_volt) * 0.2  # Ajusta el brillo del LED rojo

        if led_r.value > 1:
            led_r.value = 1
        time.sleep(1)

    # Control del LED azul basado en la temperatura
    led_b.value = temp_c / 100  # Ajusta el brillo del LED azul según la temperatura

    if led_b.value > 1:
        led_b.value = 1
    elif led_b.value < 0:
        led_b.value = 0

    # Imprime los valores leídos y calculados
    print("Voltaje del Termistor: {0:.3f} V".format(t_volt))
    print("Voltaje del Potenciómetro: {0:.3f} V".format(p_volt))
