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
from pybricks.hubs import EV3Brick, TechnicHub
from pybricks.tools import wait
import os

# Try to initialize as EV3Brick
try:
    ev3 = EV3Brick()
    print("This is an EV3 Brick.")
    # Run the EV3-specific script
    os.system("python3 /ev3/main.py")
except:
    ev3 = None

# Try to initialize as TechnicHub
try:
    technic = TechnicHub()
    print("This is a Technic (Powered Up) Hub.")
    # Run the Technic Hub-specific script
    os.system("python3 /TechnicHub/main.py")
except:
    technic = None

# Handle cases where the hub type is not identified
if ev3 is None and technic is None:
    print("Unknown hub type.")

# Add a wait to prevent the script from ending immediately
wait(2000)
