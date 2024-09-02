# LEGO EV3 Bluetooth Setup

## Overview

This document provides a step-by-step guide to setting up Bluetooth communication with the LEGO EV3 Brick using Python and the Pybricks library. It includes instructions for hardware setup, software installation, and code implementation.

## Hardware Setup

1. **LEGO EV3 Brick**: Ensure you have the LEGO EV3 Brick fully assembled and powered on.
2. **Bluetooth Device**: Ensure that your EV3 Brick is paired with a Bluetooth device (e.g., a computer or smartphone) that will communicate with it.

## Software Setup

### 1. Install Required Software

Ensure you have the following software installed:

- **Python 3.x**: Install Python 3.x from the [official Python website](https://www.python.org/downloads/).
- **Pybricks**: Install the Pybricks library using pip:
  ```sh
  pip install pybricks
  ```

### 2. Configure Bluetooth on EV3

1. **Turn on the EV3 Brick**.
2. **Navigate to Bluetooth Settings**:
   - Go to the `Bluetooth` menu on the EV3 Brick.
   - Make sure Bluetooth is enabled and set to `Discoverable` mode.
3. **Pair the EV3 Brick** with your Bluetooth device:
   - On your Bluetooth device, search for new devices.
   - Select the EV3 Brick from the list and complete the pairing process.
   - Note the Bluetooth MAC address of the EV3 Brick, which will be used in the Python script.

### 3. Python Script for EV3 Bluetooth Communication

Here’s a sample Python script to handle Bluetooth communication, motor control, and sensor reading:

```python
import socket
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait, StopWatch

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize and define devices
train_motor = Motor(Port.A)
dump_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
sensor = ColorSensor(Port.C)

# Define constants
max_load_time = 13000

# Setup Bluetooth socket
server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_socket.bind(("00:16:53:42:2B:09", 1))  # Replace with your EV3's Bluetooth MAC address
server_socket.listen(1)

print("Waiting for Bluetooth connection...")
client_socket, address = server_socket.accept()
print(f"Accepted connection from {address}")

# Wait for the desired color
def wait_for_color(desired_color):
    while sensor.color() != desired_color:
        wait(20)

# Time the train return trip
def time_return_trip():
    stopwatch = StopWatch()
    train_motor.dc(50)
    wait(1000)
    wait_for_color(Color.BLUE)
    train_motor.stop()
    wait(300)
    train_motor.dc(-30)
    wait_for_color(Color.BLUE)
    train_motor.brake()
    return stopwatch.time()

# Calculate the load time
def calculate_load_time(return_time):
    doubled_time = 2 * return_time
    load_time = 0.4 * doubled_time
    if load_time > max_load_time:
        load_time = max_load_time
    return load_time

# Initialization sequence
train_motor.dc(50)
wait(1000)
wait_for_color(Color.BLUE)
train_motor.stop()
wait(300)
train_motor.dc(-30)
wait_for_color(Color.BLUE)
train_motor.brake()
wait(2000)
train_motor.dc(-50)
wait(1000)
wait_for_color(Color.BLUE)
train_motor.stop()
wait(300)
train_motor.dc(30)
wait_for_color(Color.BLUE)
train_motor.brake()
wait(500)
dump_motor.run_until_stalled(50, duty_limit=35)
dump_motor.run_until_stalled(-50, duty_limit=20)
wait(250)
dump_motor.reset_angle(0)
wait(250)

# Main program loop
while True:
    try:
        # Receive data via Bluetooth
        data = client_socket.recv(1024)  # Adjust buffer size as needed
        
        if data:
            load_motor_speed = int(data.decode().strip())  # Convert received data to an integer
            ev3.light.on(Color.GREEN)
            train_motor.dc(load_motor_speed)  # Use received data for controlling the train motor
        else:
            ev3.light.on(Color.RED)
        
        # Perform timed actions
        return_time = time_return_trip()
        load_time = calculate_load_time(return_time)
        
        # Placeholder for BLE broadcasting
        print(f"Load motor speed: 1000")
        
        wait(load_time)
        
        # Placeholder for stopping the load motor
        print(f"Load motor speed: 0")
        
        wait(500)
        train_motor.dc(-50)
        wait(1000)
        wait_for_color(Color.BLUE)
        train_motor.stop()
        wait(300)
        train_motor.dc(30)
        wait_for_color(Color.BLUE)
        train_motor.brake()
        wait(100)
        dump_motor.run_angle(150, 110)
        wait(1000)
        dump_motor.run_angle(150, -110)
        wait(100)
        
    except Exception as e:
        print(f"Error: {e}")
        ev3.light.on(Color.RED)
        break

client_socket.close()
server_socket.close()
```

### 4. Running the Script

1. **Connect to the EV3**:
   - Ensure that the EV3 Brick is connected to your Bluetooth device.
2. **Execute the Script**:
   - Run the Python script from your computer or device.
   - The script will handle Bluetooth communication, motor control, and sensor data.

## Troubleshooting

- **Bluetooth Connection Issues**:
  - Ensure that the EV3 Brick is in discoverable mode and paired correctly with the Bluetooth device.
  - Verify that the MAC address in the script matches your EV3 Brick’s MAC address.

- **Script Errors**:
  - Check for any syntax errors or exceptions in the script.
  - Ensure that all required libraries are installed and up to date.

## Additional Resources

- [Pybricks Documentation](https://pybricks.com/guide/)
- [LEGO EV3 Documentation](https://www.lego.com/en-us/themes/ev3)

