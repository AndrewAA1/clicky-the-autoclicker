import win32api, win32con
import keyboard
import time

def clickR():
#clicks right mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def clickL():
#clicks left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clicker():
   if keyboard.is_pressed('`') == True:
   	# ^ keybind for right click
    	clickR()
    	time.sleep(0.01)
    	#change delay (in seconds) as needed
    	clickR()
   if keyboard.is_pressed(';') == True:
   	# ^ keybind for left click
    	clickL()
    	time.sleep(0.125)
    	#change delay (in seconds) as needed
    	clickL()
   if keyboard.is_pressed('=') == True:
   	# ^ keybind for exiting the program
   		exit()
while True:
	clicker()
	# ^ loops the program