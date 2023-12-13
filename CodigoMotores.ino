#include <Stepper.h>

const int stepsPerRevolution = 2048;

// Pines del controlador de motor ULN2003 - Motor 1
#define IN1 19
#define IN2 18
#define IN3 5
#define IN4 17

// Pines del controlador de motor ULN2003 - Motor 2
#define IN1_2 16
#define IN2_2 13
#define IN3_2 12
#define IN4_2 14

// Pin de la fotorresistencia
#define LDR_PIN 26

// Inicializar la biblioteca Stepper para ambos motores
Stepper myStepper(stepsPerRevolution, IN1, IN3, IN2, IN4);
Stepper myStepper2(stepsPerRevolution, IN1_2, IN3_2, IN2_2, IN4_2);

void setup() {
  // Establecer la velocidad de ambos motores
  myStepper.setSpeed(5);
  myStepper2.setSpeed(5);

  // Inicializar el puerto serial
  Serial.begin(115200);
}

void loop() {
  // Calcular los pasos necesarios para girar 90 grados (Motor 1)
  int stepsToTake = (90.0 / 360.0) * stepsPerRevolution;

  // Girar en sentido contrario a las agujas del reloj (Motor 1)
  Serial.println("Motor 1: En sentido contrario a las agujas del reloj");
  Serial.print("Valor del LDR: ");
  Serial.println(ldrValue);
  myStepper.step(-stepsToTake);
  delay(1000);

  // Girar en el sentido de las agujas del reloj (Motor 1)
  Serial.println("Motor 1: En el sentido de las agujas del reloj");
  Serial.print("Valor del LDR: ");
  Serial.println(ldrValue);
  myStepper.step(stepsToTake);
  delay(1000);

  // Leer el valor de la fotorresistencia
  int ldrValue = analogRead(LDR_PIN);

  // Imprimir el valor en el Monitor Serie
  Serial.print("Valor del LDR: ");
  Serial.println(ldrValue);

  // Acciones para el Motor 2 en función del valor del LDR
  if (ldrValue > 30) {
    // Si el valor del LDR es alto, girar el Motor 2 en sentido horario
    Serial.println("Motor 2: En sentido contrario a las agujas del reloj");
    Serial.print("Valor del LDR: ");
  Serial.println(ldrValue);
  myStepper2.step(-stepsToTake);
  delay(1000);

  // Girar en el sentido de las agujas del reloj (Motor 1)
  Serial.println("Motor 2: En el sentido de las agujas del reloj");
  Serial.print("Valor del LDR: ");
  Serial.println(ldrValue);
  myStepper2.step(stepsToTake);
  delay(1000);

  } else {
    // Si el valor del LDR es bajo, detener el Motor 2
    Serial.println("Motor 2: Detenido");
    myStepper2.step(0);
  }