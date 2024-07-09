import RPi.GPIO as g
import time

# Pin Definitions
ir_sensor_pin = 17
ir_led_pin = 18
ultrasonic_trig_pin = 23
ultrasonic_echo_pin = 26
ultrasonic_led_pin = 25
servo_pin = 19
ir_pin = 24
red_led_pin = 4
green_led_pin = 9
buzzer_pin = 3

# Setup GPIO
g.setwarnings(False)
g.setmode(g.BCM)

g.setup(ir_sensor_pin, g.IN)
g.setup(ir_led_pin, g.OUT)
g.setup(ultrasonic_trig_pin, g.OUT)
g.setup(ultrasonic_echo_pin, g.IN)
g.setup(ultrasonic_led_pin, g.OUT)
g.setup(servo_pin, g.OUT)
g.setup(ir_pin, g.IN)
g.setup(red_led_pin, g.OUT)
g.setup(green_led_pin, g.OUT)
g.setup(buzzer_pin, g.OUT)

# Initialize PWM for the servo
spwm = g.PWM(servo_pin, 50)
spwm.start(0)

# Function to read IR sensor
def read_ir_sensor():
    return g.input(ir_sensor_pin)

# Function to control IR LED
def control_ir_led(state):
    g.output(ir_led_pin, state)

# Function to read ultrasonic sensor
def read_ultrasonic_sensor():
    g.output(ultrasonic_trig_pin, True)
    time.sleep(0.00001)
    g.output(ultrasonic_trig_pin, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while g.input(ultrasonic_echo_pin) == 0:
        start_time = time.time()
    
    while g.input(ultrasonic_echo_pin) == 1:
        stop_time = time.time()
    
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound is 343 m/s
    
    return distance

# Function to control ultrasonic LED
def control_ultrasonic_led(state):
    g.output(ultrasonic_led_pin, state)

try:
    while True:
        ir_state = read_ir_sensor()
        ultrasonic_distance = read_ultrasonic_sensor()
        
        if ir_state == g.HIGH:
            print("IR Sensor Triggered!")
            control_ir_led(g.HIGH)  # Turn on IR LED
        else:
            control_ir_led(g.LOW)  # Turn off IR LED
        
        print(f"Ultrasonic Distance: {ultrasonic_distance:.2f} cm")
        
        if 3 <= ultrasonic_distance <= 5:
            # Adjust the distance threshold as needed
            g.output(red_led_pin, g.LOW)  # Turn off red LED
            g.output(green_led_pin, g.LOW)  # Turn off green LED
            g.output(buzzer_pin, g.LOW)  # Turn off buzzer
            control_ultrasonic_led(g.LOW)  # Turn on Ultrasonic LED
        elif ultrasonic_distance < 3:
            g.output(red_led_pin, g.HIGH)  # Turn on red LED
            g.output(green_led_pin, g.LOW)  # Turn off green LED
            g.output(buzzer_pin, g.HIGH)  # Turn on buzzer
            control_ultrasonic_led(g.LOW)  # Turn off Ultrasonic LED
        else:
            control_ultrasonic_led(g.HIGH)  # Turn off Ultrasonic LED
            g.output(red_led_pin, g.LOW)  # Turn off red LED
            g.output(green_led_pin, g.HIGH)  # Turn on green LED
            g.output(buzzer_pin, g.LOW)  # Turn off buzzer
        
        if g.input(ir_pin) == g.HIGH or (g.input(ultrasonic_led_pin) == g.HIGH or g.input(ir_led_pin) == g.HIGH):
            if g.input(ir_pin) == g.HIGH:
                print("close")
                spwm.ChangeDutyCycle(2)
                time.sleep(1)
            elif g.input(ir_pin) == g.LOW:
                print("open")
                spwm.ChangeDutyCycle(7)
                time.sleep(1)
            else:
                print("no place")
                spwm.ChangeDutyCycle(2)
                time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    spwm.stop()
    g.cleanup()
