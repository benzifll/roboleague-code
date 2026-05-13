from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


hub = PrimeHub()
hub.system.set_stop_button(Button.LEFT)  # LEFT спира програмата веднага

# --- Hardware setup ---        
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.B)
motorE = Motor(Port.D)
motorA = Motor(Port.C)

wheel_diameter = 56
axle_track = 141
robot = DriveBase(motor_left, motor_right, wheel_diameter, axle_track)
robot.use_gyro(True)

robot.settings(
    straight_speed=800,
    straight_acceleration=900,
    turn_rate=500,
    turn_acceleration=600
)

# --- Movement helpers ---
def move_forward(distance_mm):
    robot.straight(distance_mm, then=Stop.BRAKE, wait=True)
    wait(100)

def turn(angle_degrees):
    robot.turn(angle_degrees, then=Stop.BRAKE, wait=True)
    wait(100)

def strong_move_left(power, time_ms):
    motorE.reset_angle(None)
    motorE.dc(power)
    wait(time_ms)
    motorE.stop()
    wait(50)

def strong_move(power, time_ms):
    motorA.reset_angle(None)
    motorA.dc(power)
    wait(time_ms)
    motorA.stop()
    wait(50)

def drive_until_black():
    robot.drive(100, 0)
    while True:
        reflection = color_right.reflection()
        if reflection < 10:
            robot.stop()
            break
        wait(50)

def arc(speed_left, speed_right, duration_ms):
    motor_left.dc(speed_left)
    motor_right.dc(speed_right)
    wait(duration_ms)
    motor_left.stop()
    motor_right.stop()
    wait(10)

def reset_motors(sleep = 10):
    motorA.reset_angle(None)
    motor_left.reset_angle(None)
    motorE.reset_angle(None)
    motor_right.reset_angle(None)
    wait(sleep)

def run7():
    #Ostavqne na artefakti
    move_forward(200)
    turn(53)  
    move_forward(250)
    move_forward(-400)

def run3():
   move_forward(560)
   turn(90)
   move_forward(175)
   # Бутаме мачтата
   motorE.run_angle(speed=500, rotation_angle=120, wait=True)
   motorE.run_angle(speed=500, rotation_angle=-120, wait=True)
   move_forward(-135) # И взимаме артефакта от 9 мисия
   turn(-138)
   turn(74)
   move_forward(126)
   motorA.run_angle(speed=500, rotation_angle=-150, wait=True)
   move_forward(330)
   motorA.run_angle(speed=400, rotation_angle=150, wait=True)
   turn(15)
   move_forward(-100) # Вдигаме скелета
   turn(-42)
   move_forward(800)
   stop()
  

def run5():
    # vzemane na artefakta i vlaka
    move_forward(640)
    turn(92)
    move_forward(350)
    turn(45)
    move_forward(-300)
    turn(-50)
    motorA.run_angle(100,-145,then=Stop.BRAKE,wait=True)
    move_forward(110)
    motorE.run_angle(500,390,then=Stop.BRAKE,wait=True)
    motorA.run_angle(100,145,then=Stop.BRAKE,wait=True)
    turn(4)
    move_forward(-110)
    turn(45)
    move_forward(200)
    arc(-90,-30,900)
    move_forward(-700)
    

    """
    move_forward(570)
    turn(93)
    move_forward(180)
    motorE.run_angle(100,150,then=Stop.BRAKE,wait=True)
    wait(100)
    motorE.run_angle(100,-150,then=Stop.BRAKE,wait=True)
    move_forward(-100)
    turn(-72)
    motorA.run_angle(100,-135,then=Stop.BRAKE,wait=True)
    move_forward(400)
    motorA.run_angle(100,70,then=Stop.BRAKE,wait=True)
    turn(40)
    move_forward(-80)
    turn(-55)
    move_forward(900)
    """
# --- RUN 1 ---
def run_1():
    reset_motors()

    move_forward(660)
    turn(-90)
    move_forward(290)
    motorA.run_angle(speed=400, rotation_angle=150, wait=True)
    move_forward(-290)
    turn(90)
    move_forward(660)

    """
    strong_move(-100, 300)
    strong_move(100, 300)
    wait(100)
    """
    strong_move(-100, 300)
    strong_move(35, 300)
    turn(-25)
    move_forward(280)
    strong_move(40, 500)
    move_forward(25)
    turn(-25)
    move_forward(-75)
    turn(-72)
    move_forward(-120)
    strong_move_left(80, 550)
    move_forward(-130)
    strong_move_left(-100, 550)
    arc(60,81,1200)
    move_forward(150)
    #turn(10)
    move_forward(-200)
    arc(65,100,2000)
    
    """
    move_forward(320)
    turn(-90)
    
    move_forward(210)

    #move_forward(-130)
    turn(44)
    strong_move(-100, 300)
    move_forward(200)
    move_forward()
    """
    
    stop()
def run2():
    #vdigane na artefakta i magazina
    move_forward(490)
    turn(-19)
    move_forward(70)
    turn(9)
    move_forward(20)
    strong_move_left(-300,1300)
    move_forward(-390)
    turn(58)
    move_forward(210)
    turn(-55)
    turn(50)
    strong_move(-100,200)
    move_forward(-500)
"""
def run_2():
    reset_motors()
    move_forward(520)
    wait(100)
    turn(-16)
    move_forward(70)
    strong_move_left(-450, 800)

    stop()
    reset_motors()
    move_forward(650)
    turn(-32)
    move_forward(105)
    turn(17)
    strong_move_left(190, 950) # Вдигаме артефакта с зъбни колелата 
    move_forward(-138)
    turn(110)
    move_forward(146)
    # Бутаме мачтата
    motorA.run_angle(speed=500, rotation_angle=250, wait=True)
    motorA.run_angle(speed=500, rotation_angle=-190, wait=True)
    move_forward(-135) # И взимаме артефакта от 9 мисия
    turn(-68)
    move_forward(120)
    motorA.run_angle(speed=500, rotation_angle=180, wait=True)
    move_forward(240)
    motorA.run_angle(speed=500, rotation_angle=-50, wait=True)
    turn(25) # Вдигаме скелета
    move_forward(-80)
    turn(-52)
    move_forward(300)
    arc(60, 80, 2000)
    stop()
"""
    # --- RUN 2 ---
def run_7():
    reset_motors()
    move_forward(140)
    turn(57)
    move_forward(150)
    motorE.run_angle(speed=500, rotation_angle=135, wait=True)
    move_forward(115)
    motorE.run_angle(speed=500, rotation_angle=60, wait=True)
    move_forward(-115)
    move_forward(40)
    motorE.run_angle(speed=500, rotation_angle=-75, wait=True)
    move_forward(-170)
    motorE.run_angle(speed=500, rotation_angle=-125, wait=True)
    turn(-60) 
    move_forward(430)
    turn(88)
    move_forward(175)
    motorA.run_angle(speed=500, rotation_angle=150, wait=True)
    motorA.run_angle(speed=500, rotation_angle=-150, wait=True)
    move_forward(-175)
    turn(30)
    move_forward(350)
    turn(30)
    motorA.run_angle(speed=500, rotation_angle=-50, wait=True)
    turn(25)
    move_forward(-80)
    turn(-52)
    move_forward(300)
    arc(60,80,2000)
    stop()

# --- RUN 3 ---
def run_3():
    reset_motors()
    move_forward(550)
    wait(300)
    move_forward(-260)
    turn(12)
    move_forward(270)
    turn(-57)
    
    motorA.run_angle(500, -150, wait=True)
    move_forward(110)
    move_forward(-40)
    motorA.run_angle(500, 70, wait=True)
    move_forward(-70)
    arc(-65,-100,2050)
    
    """
    reseting(10)
    move_forward(600)
    wait(100)
    reseting(10)
    move_forward(-300)
    turn(13)
    move_forward(250)
    turn(-61)
    motorE.run_angle(500, 207, wait=True)
    motorA.run_angle(500, -150, wait=True)
    move_forward(130)
    #motorA.run_angle(500, -55, wait=True)
    #move_forward(60)
    move_forward(-30)
    motorA.run_angle(500, 140)
    turn(15)
    turn(-15)
    move_forward(-100)

    turn(-125)
    move_forward(620)
    #arc(-65,-100,2050)
    """
    stop()

# --- RUN 4 ---
def run_4():
    reset_motors()
    move_forward(790)
    turn(94.5)
    motorE.run_angle(200, -254.5)
    motorA.run_angle(200, -86)
    robot.settings(straight_speed=300, straight_acceleration=200, turn_rate=500, turn_acceleration=500)
    move_forward(160)
    robot.settings(straight_speed=900, straight_acceleration=600, turn_rate=500, turn_acceleration=500)
    
    
    motorE.run_angle(200, 32)
    
    
    motorA.run_angle(200, 100)
    wait(100)
    motorA.run_angle(200, -60)
    move_forward(-150)
    turn(120)
    move_forward(800)
    
    stop()

# --- RUN 5 ---
def run_5():
    reset_motors()
    move_forward(400)
    move_forward(-500)
    turn(-19)
    move_forward(750)
    turn(40)
    move_forward(300)
    motorA
    stop()
  
# --- RUN 6 ---
def run_6():
    reset_motors()
    move_forward(630)
    strong_move(-100, 100)
    move_forward(-50)
    motorA.run_angle(100, 30)
    move_forward(-490)
    stop()

# --- RUN 7 ---
def run_7():

    reset_motors()
    move_forward(730)
    turn(90)
    move_forward(940)
    turn(-95)
    move_forward(120)
    move_forward(-120)
    turn(90)
    move_forward(-490)
    turn(-7)
    move_forward(-380)
    """
    na ivan
    #move_forward(300)
    arc(76,94,290)
    move_forward(250)
    """
    """move_forward(480)
    turn(-53)
    move_forward(850)
    #arc(-100,90,400)
    turn(-67)
    move_forward(-260)
    arc(75,40,720)
    #move_forward(170)
    #turn(30)""
    #move_forward(-10)
    arc(-100,0,600)
    move_forward(-260)
    move_forward(400)
    """
    stop()

# --- Меню система ---
button = 1
prev_pressed = []
hub.display.number(button)

while True:
    pressed = hub.buttons.pressed()

    if Button.RIGHT in pressed and Button.RIGHT not in prev_pressed:
        button += 1
        if button > 8:
            button = 1
        hub.display.number(button)

    elif Button.CENTER in pressed and Button.CENTER not in prev_pressed:
        if button == 1:
            run1()
        elif button == 2:
            run_2()
        elif button == 3:
            newrun3()
        elif button == 4:
            run_3()
        elif button == 5:
            run_4()
        elif button == 6:
            run_5()
        elif button == 7:
            run_6()
        elif button == 8:
            run_7()

        hub.display.number(button)

    prev_pressed = pressed
    wait(100)