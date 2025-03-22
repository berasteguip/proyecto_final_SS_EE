# proyecto_final_SS_EE
Proyecto Final de Laboratorio de Sistemas Electrónicos

## Descripción del Proyecto
El objetivo de este proyecto es diseñar y construir un ventilador inteligente que se controle automáticamente en función de la temperatura y el nivel de humedad del entorno. Además, el sistema incluye medidas de seguridad y opciones de control manual para garantizar su funcionalidad y seguridad.

## Objetivos
1. Construir un ventilador que funcione automáticamente según las condiciones ambientales (temperatura y humedad).
2. Implementar un sistema de seguridad que apague el ventilador cuando detecte la presencia de una persona cerca.
3. Permitir al usuario controlar manualmente el ventilador mediante un pulsador sencillo, alternando entre los modos automático y manual.

## Características Principales
- **Modo Automático**: El ventilador se enciende o apaga automáticamente según los valores de temperatura y humedad predefinidos.
- **Modo Manual**: El usuario puede encender o apagar el ventilador manualmente utilizando un pulsador.
- **Medidas de Seguridad**: El ventilador se apaga automáticamente si detecta la presencia de una persona cerca, evitando posibles accidentes.

## Funcionamiento
1. **Modo Automático**: 
   - El sistema mide continuamente la temperatura y la humedad.
   - Si las condiciones superan los umbrales establecidos, el ventilador se enciende automáticamente.
   - Si las condiciones vuelven a valores normales, el ventilador se apaga.

2. **Modo Manual**:
   - El usuario puede activar o desactivar el ventilador manualmente mediante un pulsador.
   - Este modo permite al usuario tener control directo sobre el ventilador, independientemente de las condiciones ambientales.

3. **Detección de Presencia**:
   - Un sensor detecta la proximidad de una persona.
   - Si se detecta una persona cerca, el ventilador se apaga automáticamente como medida de seguridad.

## Componentes Utilizados
- Sensor de temperatura y humedad.
- Sensor de proximidad.
- Ventilador.
- Pulsador para control manual.
- Microcontrolador para gestionar el sistema.

## Autor
Este proyecto ha sido desarrollado como parte del curso de Laboratorio de Sistemas Electrónicos en la Universidad Pontificia Comillas por:
- Miguel Gabaldón Poncela
- Santiago Córdoba Artieda
- Pablo Berástegui Magallón
