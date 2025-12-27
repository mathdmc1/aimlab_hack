# 🎯 Aimbot Project

Configurable and easy-to-use aimbot, with full control over mouse movement, shooting, and display. Designed to be
**precise, adjustable, and easy to modify** from the code.

 

----------

## 🚀 Installation and Execution

Clone the repository and run the main file:

    `python aimbot.py`

----------

## 🎮 Controls

During program execution, you can use the following keys:

|KEY|FUNCTION |
|--|--|
| 1 |Start program
2  |Temporary pause
|3| End program




----------

## ⌨️ Key Configuration

The keys can be modified directly from the code:


STARTING_KEY = "1" Start program
SLEEPING_KEY = "2"  Temporary pause
STOP_KEY     = "3"  End program

----------

## 👁️ Preview

    PREVIEW=TRUE/FALSE

 
|VARIABLE| FUNTION |
|--|--|
| TRUE|It displays on screen what the program detects  |
|FALSE|Does not show any window


----------

## ⚙️ Aimbot configuration

### 🎯 DEADZONE

    DEADZONE=1

Define the central area of ​​the target where the pointer must reach to allow the shot.

- Lower value → greater accuracy    
- Higher value → more tolerance
    

----------

### 🔧 FACTOR

Controls the force of the mouse movement towards the target.

-   Prevent the aimbot from going over the target

You can change it to go to the target faster, but you run the risk of it overshooting the target.
    

----------

### 🔫 SHOOT

    SHOOT=TRUE/FALSE
  


|VARIABLE| FUNTION |
|--|--|
| TRUE|Automatic fire  |
|FALSE|Manual fire
----

### 🧲 AIM

`AIM = True` 

-   Activa o desactiva el movimiento automático de la mira hacia el objetivo
    

----------

### 🖱️ MAX_MOVE_PER_FRAME

`MAX_MOVE_PER_FRAME = 10` 

-   Maximum number of pixels the mouse can move per frame
    
-   Low values ​​→ smoother, more human-like movement
    
-  High values ​​→ faster and more aggressive movement
    

----------

## 🧠 NOTE

-   All values ​​are **fully customizable**
    
-   Adjusting the parameters improves accuracy and naturalness
    
-  It is recommended to try low values ​​and adjust them as needed.
