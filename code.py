
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.GPIO)


led1 = LED(10)
led2 = LED(11)
led3 = LED(9)

tinker = Tk()
radio=IntVar()

tinker.title("LED Toggle")

myFont = tkinter.font.Font(family = 'Helvetica', size=14, weight="bold")



def funk():

     if radio.get() == 1:
          if led1.is_lit:
               led1.off()
          else:
               led1.on()
               led2.off()
               led3.off()
     if radio.get() == 2:
          if led2.is_lit:
               led1.off()
          else:
               led2.on()
               led1.off()
               led3.off()
     if radio.get() == 3:
          if led3.is_lit:
               led1.off()
          else:
               led3.on()
               led1.off()
               led2.off()


def exit():
    led1.off()
    led2.off()
    led3.off()
    GPIO.cleanup()
    tinker.destroy()


exitButton = Button(tinker, text="EXIT", font=myFont, 
command=exit, bg='bisque2', height=1, width=25 )

R1 = Radiobutton(tinker, text="RED", variable=radio, value=1)
R1.pack(anchor=W)
R2 = Radiobutton(tinker, text="GREEN", variable=radio, value=2)
R2.pack(anchor=W)
R3 = Radiobutton(tinker, text="YELLOW", variable=radio, value=3)
R3.pack(anchor=W)
exitButton.pack(anchor=W)


tinker.protocol("WM_DELETE_WINDOW", exit)

tinker.mainloop()

