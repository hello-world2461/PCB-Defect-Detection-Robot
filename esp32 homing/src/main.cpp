#include <Arduino.h>

// Define pin connections & motor's steps per revolution
//X Motor
#define dirX 14
#define stepX 12
#define homeSwitchX 32

//Y Motor
#define dirY 26
#define stepY 27
#define homeSwitchY 18

//Z Motor
#define dirZ 33
#define stepZ 25
#define homeSwitchZ 19

const double stepsPerRevolution = 200;

//Function to move the motor
//dir_of_motor: (TRUE = CLOCKWISE, FALSE = ANTICLOCKWISE)
//num_of_turns: 1 turn has 200 steps.
//speed_of_motor: Number of microseconds to wait (just use 2000)
void control_motor(int dir, int step, bool dir_of_motor, double num_of_turns, int speed_of_motor){
    //Set pins
	pinMode(step, OUTPUT);
	pinMode(dir, OUTPUT);
	
	//Change direction of motor
    if (dir_of_motor == true){
        digitalWrite(dir, HIGH);
    }
    else{
        digitalWrite(dir, LOW);
    }
    
	// Spin motor
	for(int x = 0; x < (int(num_of_turns * stepsPerRevolution)); x++){
		digitalWrite(step, HIGH);
		delayMicroseconds(speed_of_motor);  //set input to 2000
		digitalWrite(step, LOW);
		delayMicroseconds(speed_of_motor);  //set input to 2000
	}
}

void setup()
{
	Serial.begin(9600);
	//X AXIS
	// Declare pins as Outputs
	pinMode(homeSwitchX, INPUT_PULLUP);

	//Move motor X to home position without stopping
	while (digitalRead(homeSwitchX) == 0){
		control_motor(dirX, stepX, true, 0.125, 1000);
	}
	Serial.println("Motor X has been homed.");
	delay(1000);

	//Y AXIS
	pinMode(homeSwitchY, INPUT_PULLUP);
	//Move motor Y to home position without stopping
	while (digitalRead(homeSwitchY) == 0){
		control_motor(dirY, stepY, false, 0.125, 1000);
	}
	Serial.println("Motor Y has been homed.");

	//Z AXIS
	pinMode(homeSwitchZ, INPUT_PULLUP);
	//Move motor Z to home position without stopping
	while (digitalRead(homeSwitchZ) == 0){
		control_motor(dirZ, stepZ, true, 0.125, 1000);
	}
	Serial.println("Motor Z has been homed.");
}

void loop()
{
	//Serial.println(digitalRead(homeSwitchX));
	//delay(1000);
}
