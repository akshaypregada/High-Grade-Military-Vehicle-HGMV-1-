#include <Wire.h>
#include <Arduino.h>

#define MOTOR1_PIN1 5
#define MOTOR1_PIN2 6
#define MOTOR2_PIN1 9
#define MOTOR2_PIN2 10

void setup() {
    pinMode(MOTOR1_PIN1, OUTPUT);
    pinMode(MOTOR1_PIN2, OUTPUT);
    pinMode(MOTOR2_PIN1, OUTPUT);
    pinMode(MOTOR2_PIN2, OUTPUT);
}

void moveForward() {
    digitalWrite(MOTOR1_PIN1, HIGH);
    digitalWrite(MOTOR1_PIN2, LOW);
    digitalWrite(MOTOR2_PIN1, HIGH);
    digitalWrite(MOTOR2_PIN2, LOW);
}

void moveBackward() {
    digitalWrite(MOTOR1_PIN1, LOW);
    digitalWrite(MOTOR1_PIN2, HIGH);
    digitalWrite(MOTOR2_PIN1, LOW);
    digitalWrite(MOTOR2_PIN2, HIGH);
}

void stopMotors() {
    digitalWrite(MOTOR1_PIN1, LOW);
    digitalWrite(MOTOR1_PIN2, LOW);
    digitalWrite(MOTOR2_PIN1, LOW);
    digitalWrite(MOTOR2_PIN2, LOW);
}

void loop() {
    moveForward();
    delay(3000);
    stopMotors();
    delay(2000);
    moveBackward();
    delay(3000);
    stopMotors();
    delay(2000);
}
