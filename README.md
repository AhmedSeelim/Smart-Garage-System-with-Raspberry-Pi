# Smart Garage System

## Project Overview
This project involves creating a garage system that automatically opens its door when a car approaches and remains closed when the garage is full. Inside sensors indicate if we have parked cars or not, connected by external LEDs. Components like infrared sensors, ultrasonic sensors, servo motors, LEDs, and Raspberry Pi are utilized.

## Components
- Raspberry Pi
- IR Sensors
- Ultrasonic Sensors
- Servo Motor
- LEDs (Red and Green)
- Buzzer
- Breadboard and Jumper Wires
- Resistors

## How It Works
1. **IR Sensor**: Detects if a car is near the garage.
2. **Ultrasonic Sensor**: Measures the distance to the car.
3. **Servo Motor**: Opens the garage door if a car is detected and the garage is not full; otherwise, it remains closed.
4. **LEDs**: Indicate the status of the garage.
   - **Red LED**: Turns on when the garage is full.
   - **Green LED**: Turns on when the garage is available.
5. **Buzzer**: Sounds an alert when the garage is full and a car is detected.

## Demonstration Video
For a visual demonstration of the project and its functionality, please watch our [YouTube video](https://youtu.be/HodAuc1V1po).

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
