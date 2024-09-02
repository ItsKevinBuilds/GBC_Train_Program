"""
$$\      $$\                 $$\                 $$\                        $$$$$$\                                                                   $$$$$$$$\ 
$$$\    $$$ |                $$ |                $$ |                      $$  __$$\                                                                  \__$$  __|
$$$$\  $$$$ | $$$$$$\   $$$$$$$ | $$$$$$\        $$$$$$$\  $$\   $$\       $$ /  \__| $$$$$$\  $$$$$$\  $$\   $$\  $$$$$$$\  $$$$$$\  $$$$$$$\           $$ |   
$$\$$\$$ $$ | \____$$\ $$  __$$ |$$  __$$\       $$  __$$\ $$ |  $$ |      $$ |$$$$\ $$  __$$\ \____$$\ $$ |  $$ |$$  _____|$$  __$$\ $$  __$$\          $$ |   
$$ \$$$  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |      $$ |\_$$ |$$ |  \__|$$$$$$$ |$$ |  $$ |\$$$$$$\  $$ /  $$ |$$ |  $$ |         $$ |   
$$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |     $$  __$$ |$$ |  $$ | \____$$\ $$ |  $$ |$$ |  $$ |         $$ |   
$$ | \_/ $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\       $$$$$$$  |\$$$$$$$ |      \$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$ |$$$$$$$  |\$$$$$$  |$$ |  $$ |         $$ |   
\__|     \__| \_______| \_______| \_______|      \_______/  \____$$ |       \______/ \__|      \_______| \____$$ |\_______/  \______/ \__|  \__|         \__|   
                                                           $$\   $$ |                                   $$\   $$ |                                              
                                                           \$$$$$$  |                                   \$$$$$$  |                                              
                                                            \______/                                     \______/                                               
"""
import socket
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize and define devices
load_motor = Motor(Port.A)

# Setup Bluetooth socket
server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_socket.bind(("00:16:53:42:2B:09", 1))  # Replace with your EV3's Bluetooth MAC address
server_socket.listen(1)

print("Waiting for Bluetooth connection...")
client_socket, address = server_socket.accept()
print(f"Accepted connection from {address}")

while True:
    try:
        data = client_socket.recv(1024)  # Adjust buffer size as needed
        if data:
            load_motor_speed = int(data.decode().strip())  # Convert received data to an integer
            ev3.light.on(Color.GREEN)
            load_motor.run(load_motor_speed)
        else:
            ev3.light.on(Color.RED)
    except Exception as e:
        print(f"Error: {e}")
        ev3.light.on(Color.RED)
        break

    wait(10)

client_socket.close()
server_socket.close()
