#include <Servo.h>

// ESC
Servo esc;
const int escPin = 5;
bool wasForward = true;

// Servo lái
Servo steering;
const int servoPin = 4;

// ---- Hàm điều khiển ESC ----
void controlESC(int speed) {
  int pulse = 1500; // neutral

  // Giới hạn speed
  if (speed > 25)  speed = 25;
  if (speed < -25) speed = -25;

  if (speed > 0) {
    pulse = 1550 + speed * 4; // Forward
    esc.writeMicroseconds(pulse);
    Serial.print("Forward ESC: ");
    Serial.println(pulse);
    wasForward = true;
  }
  else if (speed == 0) {
    esc.writeMicroseconds(1500); // Neutral
    Serial.println("Stop ESC (1500 us)");
  }
  else {
    // Reverse
    if (wasForward) {
      Serial.println("Mồi lùi ESC 1 lần...");
      esc.writeMicroseconds(1200);
      delay(300);
      esc.writeMicroseconds(1500);
      delay(300);
      wasForward = false;
    }
    pulse = 1350 + speed * 4;
    esc.writeMicroseconds(pulse);
    Serial.print("Reverse ESC: ");
    Serial.println(pulse);
  }
}

// ---- Hàm điều khiển Servo lái ----
void controlServo(int angle) {
  angle = constrain(angle, -25, 25);
  int position = map(angle, -25, 25, 60, 120);
  steering.write(position);

  Serial.print("Steering angle: ");
  Serial.print(angle);
  Serial.print(" -> Servo pos: ");
  Serial.println(position);
}

// ---- Setup ----
void setup() {
  Serial.begin(115200);

  esc.attach(escPin, 1000, 2000);
  esc.writeMicroseconds(1500);  // Neutral ESC
  delay(3000);

  steering.attach(servoPin);

  Serial.println("Ready to receive: speed,angle");
}

// ---- Loop ----
void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input.length() > 0) {
      int commaIndex = input.indexOf(',');
      if (commaIndex > 0) {
        int speed = input.substring(0, commaIndex).toInt();
        int angle = input.substring(commaIndex + 1).toInt();

        Serial.print("Recv -> Speed: ");
        Serial.print(speed);
        Serial.print(" | Angle: ");
        Serial.println(angle);

        controlESC(speed);
        controlServo(angle);
      }
    }
  }
}
