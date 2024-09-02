from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor, DCMotor, Light, ColorDistanceSensor
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait, StopWatch

# Initialize and define devices
hub = TechnicHub(broadcast_channel=1)
train_motor = DCMotor(Port.A)
dump_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [12, 36])
sensor = ColorDistanceSensor(Port.C)
headlights = Light (Port.D)

# Define constants
max_load_time = 13000

# Wait for desired color
def wait_for_color(desired_color):
    while sensor.color() != desired_color:
        wait(20)

# Time train return trip
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

# Calculate load time
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

# Main program
while True:
    return_time = time_return_trip()
    load_time = calculate_load_time(return_time)
    load_motor_speed = 1000
    data = load_motor_speed
    hub.ble.broadcast(data)
    wait(load_time)
    load_motor_speed = 0
    data = load_motor_speed
    hub.ble.broadcast(data)
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