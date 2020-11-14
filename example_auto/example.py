import pyautogui
import time
import os
# alerts
# pyautogui.alert("welcome to automation with python")
# pyautogui.confirm("shall i proceed to automate")

# keyboard, mouse
# desktop -> screen

screenWidth,screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

# creating a new file
# writing c program in it
# executing it

# ctrl+n
# ctrl+s
pyautogui.hotkey('ctrl','n')
pyautogui.hotkey('ctrl','s')

time.sleep(1)
pyautogui.write('sample.c')
time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.write("#include<stdio.h>\nint main(int argc, char const *argv[])\n{\n\tprintf(\"this is a c code executed by python\");\nreturn 0;\n",interval=0.1)
time.sleep(1)

pyautogui.hotkey('win','r')
pyautogui.write("cmd")
pyautogui.press('enter')
time.sleep(1)

pyautogui.write(r"cd C:\Users\jacks\OneDrive\Desktop\example_auto",interval=0.1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("gcc sample.c",interval=0.1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.write("a.exe",interval=0.1)
pyautogui.press('enter')
time.sleep(2)

os.remove('sample.c')