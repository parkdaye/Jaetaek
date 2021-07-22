from tkinter import *
import pyautogui

isActive = True
i = 1
range = 100

def start_cmd():
    global isActive, range
    interval = int(input.get())
    range *= -1

    if isActive:
        pyautogui.move(range, 0)
        root.after(interval * 1000, start_cmd)
    else :
        print("프로그램이 종료되었습니다")
        isActive = True

def stop_cmd():
    global isActive
    isActive = False

root = Tk()
root.title("MM")

label = Label(root, text="간격(초 단위) : ")
label.grid(column = 0, row = 0)

input = Entry(root, width = 10)
input.grid(column = 1, row = 0)

start_button = Button(root, text = "Start", command= start_cmd)
stop_button = Button(root, text = "Stop", command=stop_cmd)

start_button.grid(column = 0, row = 1)
stop_button.grid(column = 1, row = 1)

root.mainloop()

