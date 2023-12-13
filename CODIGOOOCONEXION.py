from machine import Pin, PWM
from time import sleep
import network
from umqtt.simple import MQTTClient

# Definir las frecuencias para las notas musicales en Hz
D5 = 587
E5 = 659
F5 = 698
G5 = 784
A5 = 880
B5 = 988
C6 = 1047
B4 = 494
C5 = 523
D6 = 1175

reproduciendo_melodia = False

# Configurar el pin del zumbador como PWM
buzzer = PWM(Pin(26))
buzzer.duty(0)  # Inicializar el zumbador con un ciclo de trabajo del 0%

# Función para iniciar una nota con una frecuencia específica
def iniciar_nota(frecuencia):
    if frecuencia > 0:
        buzzer.freq(frecuencia)
        buzzer.duty(512)

# Función para detener la nota
def detener_nota():
    buzzer.duty(0)

def detener_todo():
    global reproduciendo_melodia
    detener_nota()  # Detener la melodía si se está reproduciendo
    reproduciendo_melodia = False
    apagar_leds()  # Apagar todos los LEDs    

# Función encargada de encender el zumbador cuando llega un mensaje
def llegada_mensaje(topic, msg):
    global reproduciendo_melodia

    print(msg)
    if msg == b'1':
        # Reproducir melodías y establecer la bandera en True
        reproducir_melodia(melodia_jingle_bells)
        reproducir_melodia(melodia_wish_you_merry_christmas)
        reproduciendo_melodia = True
    elif msg == b'0':
        detener_nota()
        reproduciendo_melodia = False
    elif msg == b'2':
        encender_leds()
    elif msg == b'3':
        apagar_leds()
    elif msg == b'4':
        detener_todo()  # Detener la melodía y apagar LEDs inmediatamente
    elif msg == b'5':
        encender_leds()  # Encender LEDs


# Función para reproducir una melodía
def reproducir_melodia(melodia):
    for frecuencia, duracion in melodia:
        iniciar_nota(frecuencia)
        sleep(duracion / 1000)
        detener_nota()
        sleep(0.1)

# Función para encender todos los LEDs
def encender_leds():
    for led in leds:
        led.value(1)

# Función para apagar todos los LEDs
def apagar_leds():
    for led in leds:
        led.value(0)

# Declarar función para conectarnos a WiFi
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('linksys', '')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Connected!!")

# Configurar pines para los LEDs
led_pins = [13, 12, 33, 32, 25]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Conectar a WiFi
conectar_wifi()
# Detalles de MQTT
MQTT_BROKER = "192.168.1.100"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/homher/leds_buzzer"
MQTT_PORT = 1883

# Subscribirse al broker MQTT
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.set_callback(llegada_mensaje)
client.connect()
client.subscribe(MQTT_TOPIC)
print("Conectado a %s, en el topic %s" % (MQTT_BROKER, MQTT_TOPIC))

# Melodía de "Jingle Bells"
melodia_jingle_bells = [
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (G5, 300), (D5, 300), (C6, 300),
    (B5, 300), (A5, 300), (G5, 1200),
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (G5, 300), (D5, 300), (C6, 300),
    (B5, 300), (A5, 300), (G5, 1200)
]

# Melodía de "We Wish You a Merry Christmas"
melodia_wish_you_merry_christmas = [
    (G5, 500), (G5, 500), (A5, 500),
    (G5, 500), (C6, 1000), (B5, 500),
    (B5, 500), (A5, 500), (G5, 500),
    (F5, 1000), (E5, 500), (E5, 500),
    (D5, 500), (B4, 500), (C5, 1000),
    (G5, 500), (G5, 500), (A5, 500),
    (G5, 500), (D6, 1000), (C6, 500),
    (B5, 500), (A5, 500), (F5, 1000),
    (E5, 500), (E5, 500), (D5, 500),
    (B4, 500), (C5, 1000)
]

# Ciclo infinito para esperar mensajes MQTT
while True:
    client.check_msg()  # Revisa si hay nuevos mensajes MQTT