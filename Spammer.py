import pyautogui
from time import sleep
arr = [i for i in range(100)]
sleep(5)
for i in arr:
    pyautogui.typewrite(str(i))
    pyautogui.press("enter")
print(arr)