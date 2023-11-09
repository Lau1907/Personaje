# Personaje

## Nombre del personaje
Hombre con Herramientas

# Integrantes
Medrano Hernández Vanesa Monserrat
Tapia Cid Laura Berenice

# Objetivo General
El objetivo general de crear un personaje navideño como lo es el hombre con herramientas es utilizar los principios de IoT para mejorar la automatización, la eficiencia y la comodidad para hacer este personaje lo más apegado a la realidad. Esto implicará la integración de dispositivos y sensores inteligentes en el entorno especificado para poder controlar y gestionar diversas tareas y sistemas que se pretende que realice este personaje.

## Materiales Utilizados
|EsP32|Microcontrolador con comunicación serial, wifi, bluetooth|Cantidad: 1|$140.00|
|Cables Dupont|Cables MM HH MH para conexión de prototipos|Cantidad: 50|$60.00|
|Leds | Dispositivo que permite el paso de corriente en un solo sentido y que al ser polarizado emite un haz de luz | Cantidad: 3 | $3
| Buzzer | Transductor capaz de convertir la energía eléctrica en sonido | Cantidad: 1 | $49
| Servomotor | Actuador rotativo o lineal que permite lograr un control preciso en cuanto a posición angular, aceleración y velocidad del eje | Cantidad: 1 | $49
| Breadboard | Permite quitar y reemplazar componentes fácilmente | Cantidad : 1 | $69


## Software utilizado
| Id      | Software            | Versión   | Tipo                                              |
|---------|---------------------|-----------|---------------------------------------------------|
| ARDIDE  | Arduino IDE         | 2.0       | Entorno de Desarrollo Integrado IDE               |
|         | Thonny              | 3.10      | Entorno de Desarrollo Integrado IDE               |
| HA      | Asistente del hogar | 2023.11.1 | Plataforma de automatización del hogar            |
|         | sqLite              | 2.3.0     | sistema de gestión de bases de datos relacionales |

## Dibujo del prototipo a desarrollar
![image](https://github.com/Lau1907/Personaje/assets/146136106/e4b64210-3952-452c-9374-9baea7c37f4c)


## Comunicación
El proyecto "Hombre con Herramientas" utiliza el microcontrolador ESP32, que ofrece capacidades de comunicación serial, Wi-Fi y Bluetooth. Esto permite al dispositivo interactuar con otros dispositivos, enviar datos a la nube y comunicarse con una aplicación móvil o una interfaz web.

## Arquitectura
La arquitectura del proyecto se basa en el ESP32 como núcleo central. Este microcontrolador se encarga de controlar las herramientas con luz, sonido y movimiento. Se utiliza el software Thonny para programar el ESP32 y cargar el código necesario para el funcionamiento de las herramientas. Además, sqLite se emplea para diseñar y simular circuitos electrónicos que permiten la interacción entre el microcontrolador y las herramientas.

## Base de datos
Para el almacenamiento de datos, se puede integrar una base de datos en el proyecto si es necesario. Esto permitirá registrar información importante, como registros de uso de las herramientas, estadísticas y configuraciones. Puedes utilizar una base de datos compatible con el ESP32 y configurar la comunicación para almacenar y recuperar datos según sea necesario.
