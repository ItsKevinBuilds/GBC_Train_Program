from pybricks.hubs import CityHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize and define devices
hub = CityHub(observe_channels=[1])
load_motor = Motor(Port.A)

while True:
    data = hub.ble.observe(1)
    if data is None:
        hub.light.on(Color.RED)
    else:
        hub.light.on(Color.GREEN)
        load_motor_speed = data
        load_motor.run(load_motor_speed)
        wait(10)