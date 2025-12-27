import cv2
import numpy as np
import keyboard
import win32api, win32con
import mss

#500 pixelSes {"top":290, "left":710, "width":500, "height":500}
#250 pixeles {"top": 415, "left": 835, "width": 250, "height": 250}
#1000 x 800 {"top":140,"left":460,"width":1000,"height":800}
monitor={"top":290, "left":710, "width":500, "height":500}


CENTER=(monitor["width"]//2, monitor["height"]//2)
"-----------CONFIG-------------"
PREVIEW=False
SHOOT=True
AIM=True
DEADZONE=1
FACTOR=0.2
MAX_MOVE_PER_FRAME=500 
STARTING_KEY="1"
SLEEPING_KEY="2"
STOP_KEY="3"
"------------------------------"
def main():
    global PREVIEW
    global STARTING_KEY
    global SLEEPING_KEY
    global STOP_KEY
    active=False
    with mss.mss() as sct:
        while True:
            
            if keyboard.is_pressed(STARTING_KEY):
                active=True
                print("Aimbot Activado")
            if keyboard.is_pressed(SLEEPING_KEY):
                active=False
                print("Aimbot Desactivado")
            if keyboard.is_pressed(STOP_KEY):
                print("Saliendo...")
                break
            if not active:
                continue
            img_array = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img_array, cv2.COLOR_BGRA2BGR)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_gray=cv2.GaussianBlur(img_gray,(5,5),0)
            img_gray=cv2.Canny(img_gray,50,150)
            contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                if len(cnt) < 20:
                    continue
                try:
                    ellipse = cv2.fitEllipse(cnt)
                except:
                    continue
                (x,y), (a,b), angle = ellipse

                if a / b > 5:
                    continue
                mover_mouse(x,y)
                if PREVIEW:
                    cv2.ellipse(img, ellipse, (0,255,0), 2)
            if PREVIEW:
                cv2.imshow('winname', img)
                cv2.waitKey(1)
def mover_mouse(x, y):
    global SHOOT
    global AIM
    global MAX_MOVE_PER_FRAME
    global CENTER

    factor=FACTOR
    umbral=DEADZONE
    max_move =MAX_MOVE_PER_FRAME
    dx = (int(x) - CENTER[0])*factor
    dy = (int(y) - CENTER[1])*factor

    #print(f"dx={dx}, dy={dy}")
    
    if abs(dx) > umbral or abs(dy) > umbral:
        # Limitar el movimiento máximo por frame
        if AIM:
            move_x = int(max(-max_move, min(max_move, dx)))
            move_y = int(max(-max_move, min(max_move, dy)))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, move_x, move_y, 0, 0)
    else:
        if SHOOT:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)





main()