// Arduino sketch to control a robot based on serial input from Python
// Receives '1' to stop, '0' to move forward

// Motor control pins (adjust based on your H-bridge setup)
#define MOTOR_A_EN 9   // PWM pin for Motor A speed
#define MOTOR_A_IN1 7  // Motor A direction 1
#define MOTOR_A_IN2 8  // Motor A direction 2
#define MOTOR_B_EN 10  // PWM pin for Motor B speed
#define MOTOR_B_IN1 11 // Motor B direction 1
#define MOTOR_B_IN2 12 // Motor B direction 2

// Motor speed (0-255)
#define MOTOR_SPEED 200

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);

  // Set motor control pins as outputs
  pinMode(MOTOR_A_EN, OUTPUT);
  pinMode(MOTOR_A_IN1, OUTPUT);
  pinMode(MOTOR_A_IN2, OUTPUT);
  pinMode(MOTOR_B_EN, OUTPUT);
  pinMode(MOTOR_B_IN1, OUTPUT);
  pinMode(MOTOR_B_IN2, OUTPUT);

  // Ensure motors are stopped initially
  stopMotors();
}

void loop() {
  // Check if data is available on serial port
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read incoming byte

    // Process command
    if (command == '1') {
      stopMotors(); // Stop the robot
    } else if (command == '0') {
      moveForward(); // Move the robot forward
    }
  }
}

// Function to move the robot forward
void moveForward() {
  // Motor A forward
  digitalWrite(MOTOR_A_IN1, HIGH);
  digitalWrite(MOTOR_A_IN2, LOW);
  analogWrite(MOTOR_A_EN, MOTOR_SPEED);

  // Motor B forward
  digitalWrite(MOTOR_B_IN1, HIGH);
  digitalWrite(MOTOR_B_IN2, LOW);
  analogWrite(MOTOR_B_EN, MOTOR_SPEED);
}

// Function to stop the robot
void stopMotors() {
  // Stop Motor A
  digitalWrite(MOTOR_A_IN1, LOW);
  digitalWrite(MOTOR_A_IN2, LOW);
  analogWrite(MOTOR_A_EN, 0);

  // Stop Motor B
  digitalWrite(MOTOR_B_IN1, LOW);
  digitalWrite(MOTOR_B_IN2, LOW);
  analogWrite(MOTOR_B_EN, 0);
}