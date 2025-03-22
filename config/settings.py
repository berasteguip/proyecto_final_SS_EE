# settings.py

# Pines de sensores
PIN_TRIG = 23
PIN_ECHO = 24

# Canal MCP3008
CH_NTC = 0
CH_HIH5030 = 1

# Parámetros eléctricos
VCC_SENSOR = 5.0      # Voltaje con el que alimentas el HIH-5030
VREF_ADC = 3.3        # Referencia del ADC (Raspberry Pi)

# TODO
# Parámetros de control
TEMP_UMBRAL_ENFRIAR = 30   # ºC
HUMEDAD_MIN = 30           # %
HUMEDAD_MAX = 70           # %