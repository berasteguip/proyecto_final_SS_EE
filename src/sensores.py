from gpiozero import MCP3008, DigitalOutputDevice, DigitalInputDevice
from config.settings import *
from time import time, sleep

MCP_temperatura = MCP3008(channel=CH_NTC)
MCP_humedad = MCP3008(channel=CH_HIH5030)
trig = DigitalOutputDevice(TRIG_PIN)
echo = DigitalInputDevice(ECHO_PIN)

def temperatura() -> float:
    """
    Lee la tensión del sensor NTC y la convierte a temperatura.
    La salida es aproximadamente lineal gracias al acondicionamiento del NTC.
    Retorna la temperatura estimada en ºC. 
    Nuestro sensor fue acondicionado para leer el oltaje de la siguiente manera:
        v_0 (T) =  0.0825 V/(ºC)*T
    """
    voltage = MCP_temperatura.voltage
    
    # Por ejemplo: salida lineal entre 0.5V (0ºC) y 2.5V (100ºC)
    temp = voltage/0.0825

    return temp


def humedad() -> int:
    """
    Lee el sensor HIH-5030 y calcula la humedad relativa en %.
    Fórmula (datasheet, para alimentación de 5V):
    RH = ((Vout / Vcc) - 0.16) / 0.0062
    """
    Vcc_sensor = VCC_SENSOR        # Alimentación del HIH-5030
    Vref_adc = VREF_ADC          # Vref del MCP3008

    lectura = MCP_humedad.value           # valor normalizado entre 0.0 y 1.0
    Vout_medido = lectura * Vref_adc      # Vout en voltios

    Vout_normalizado = Vout_medido / Vcc_sensor

    humedad = (Vout_normalizado - 0.16) / 0.0062     # Valores aproximados de ejemplo
    humedad = max(0, min(humedad, 100))  # Limitar entre 0% y 100%

    return round(humedad, 2)


def medir_distancia():
    # Asegurarse de que TRIG está en bajo
    trig.off()
    time.sleep(0.5)  # Pequeña pausa para estabilizar

    # Enviar un pulso de 10 microsegundos al pin TRIG
    trig.on()
    time.sleep(0.00001)  # 10 microsegundos
    trig.off()

    # Esperar a que ECHO se ponga en alto (comienzo del pulso)
    while echo.value == 0:
        pulse_start = time.time()

    # Esperar a que ECHO se ponga en bajo (fin del pulso)
    while echo.value == 1:
        pulse_end = time.time()

    # Calcular la duración del pulso
    pulse_duration = pulse_end - pulse_start

    # Calcular la distancia (cm), asumiendo velocidad del sonido ~34300 cm/s
    distancia = (pulse_duration * 34300) / 2

    return distancia