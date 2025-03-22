from gpiozero import MCP3008
from config.settings import *

MCP_temperatura = MCP3008(channel=CH_NTC)
MCP_humedad = MCP3008(channel=CH_HIH5030)

def temperatura() -> float:
    """
    Lee la tensión del sensor NTC y la convierte a temperatura.
    La salida es aproximadamente lineal gracias al acondicionamiento del NTC.
    Retorna la temperatura estimada en ºC. 
    """
    voltage = MCP_temperatura.voltage
    
    # Por ejemplo: salida lineal entre 0.5V (0ºC) y 2.5V (100ºC)
    temp = (voltage - 0.5) * 100

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