import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.font as TkFont

#inventory
water = 1000
milk = 200
coffee = 50
cups = 30
funds = 80

#OOP Machine
class Apparatul:
    def __init__(self,water,milk,coffee,cups,money=0):
        self.water=water
        self.milk=milk
        self.coffee=coffee
        self.cups=cups
        self.money=money

        self.status()

    def status(self):
        return f"Apă: {self.water} ml\nLapte: {self.milk} ml\nCafea: {self.coffee} grame\nPahare: {self.cups} bucată"

    def espresso():
        global water
        global milk
        global coffee
        global cups
        global funds
        water = water - 75
        coffee = coffee - 20
        cups = cups - 1
        funds = funds - 30

    def cappucino():
        global water
        global milk
        global coffee
        global cups
        global funds
        water = water - 150
        coffee = coffee - 20
        milk = milk - 85
        cups = cups - 1
        funds = funds - 50


#VARIABLES
state = 0 #indicates if machine is on or off

root = tkinter.Tk()
#root.geometry('600x400+50+50') # if the window size needs to be changed
root.title("Automatul de Cafea")

#upper logo
logo = Image.open("c_logo.jpg")
logo = ImageTk.PhotoImage(logo)
front = Label(image=logo)
front.image = logo
front.grid(columnspan=2,column=0,row=0)

#modules
def start():
    screen.delete(1.0, 5.0)
    screen.insert(tkinter.END, "\n          Bine ati venit!")
    global state
    state = 1
    butt_on["state"] = "disabled"
    butt_on["bg"] = "gray70"
    butt_off["state"] = "normal"
    butt_off["bg"] = "coral"
    butt1["state"] = "normal"
    butt1["bg"] = "gold"
    butt2["state"] = "normal"
    butt2["bg"] = "gold"
    butt3["state"] = "normal"
    butt3["bg"] = "gold"
    butt4["state"] = "normal"
    butt4["bg"] = "gold"

def off():
    screen.delete(1.0, 5.0)
    screen.insert(tkinter.END, "\n           La revedere!")
    global state
    state = 0
    butt_on["state"] = "normal"
    butt_on["bg"] = "coral"
    butt_off["state"] = "disabled"
    butt_off["bg"] = "gray70"
    butt1["state"] = "disabled"
    butt1["bg"] = "white"
    butt2["state"] = "disabled"
    butt2["bg"] = "white"
    butt3["state"] = "disabled"
    butt3["bg"] = "white"
    butt4["state"] = "disabled"
    butt4["bg"] = "white"

def order(number):
    if state == 1:
        screen.delete(1.0,5.0)
        if number == 1:
            if funds < 30:
                screen.insert(tkinter.END, "           Preţ: 30 bani")
                screen.insert(tkinter.END,f"\n\n   Fonduri disponibile: {funds} bani")
            elif water < 75:
                screen.insert(tkinter.END, "          Cu puțină apă.")
                screen.insert(tkinter.END,f"\n\n     Cantitatea de apa: {water} ml")
            elif coffee < 20:
                screen.insert(tkinter.END, "           Puțin cafea.")
                screen.insert(tkinter.END, f"\n\n    Cantitatea de cafea: {coffee} ml")
            elif cups == 0:
                screen.insert(tkinter.END, "           Fara pahare.")
                screen.insert(tkinter.END, f"\n\n     Cantitatea de pahare: {cups} bucată")
            else:
                screen.insert(tkinter.END,"         Espresso servit.\n            Bucură-te!")
                Apparatul.espresso()
                screen.insert(tkinter.END,f"\n\n   Fonduri disponibile: {funds} bani")
        elif number == 2:
            if funds < 50:
                screen.insert(tkinter.END, "           Preţ: 50 bani")
                screen.insert(tkinter.END,f"\n\n   Fonduri disponibile: {funds} bani")
            elif water < 75:
                screen.insert(tkinter.END, "          Cu puțină apă.")
                screen.insert(tkinter.END, f"\n\n     Cantitatea de apa: {water} ml")
            elif milk < 85:
                screen.insert(tkinter.END, "            Fara lapte.")
                screen.insert(tkinter.END, f"\n\n     Cantitatea de lapte: {milk} ml")
            elif coffee < 20:
                screen.insert(tkinter.END, "           Puțin cafea.")
                screen.insert(tkinter.END, f"\n\n    Cantitatea de cafea: {coffee} ml")
            elif cups == 0:
                screen.insert(tkinter.END, "           Fara pahare.")
                screen.insert(tkinter.END, f"\n\n     Cantitatea de pahare: {cups} bucată")
            else:
                screen.insert(tkinter.END, "         Cappucino servit.\n            Bucură-te!")
                Apparatul.cappucino()
                screen.insert(tkinter.END,f"\n\n   Fonduri disponibile: {funds} bani")

def status():
    screen.delete(1.0, 5.0)
    screen.insert(tkinter.END, Apparatul(water, milk, coffee, cups).status())


#buttons
butt_on = Button(root,text="Pornește",height=3,width=20,bg="coral",state="normal",command=lambda:start())
butt_off = Button(root,text="Oprit",height=3,width=20,bg="gray70",state="disabled",command=lambda:off())
butt1 = Button(root,text="Espresso",height=3,width=20,state="disabled",command=lambda:order(1))
butt2 = Button(root,text="Cappucino",height=3,width=20,state="disabled",command=lambda:order(2))
butt3 = Button(root,text="Condiție",height=3,width=20,state="disabled",command=lambda:status())
butt4 = Button(root,text="---",height=3,width=20,state="disabled")

#text field
message = TkFont.Font(weight="bold") #if bold font is needed somewhere
screen = Text(root, height=4, borderwidth=5, width=36)
screen.insert(tkinter.END, "\n       Aparatul este oprit.") #one line can hold 35 characters and has 4 lines

#widgets
screen.grid(column=0,row=1, columnspan=2)
butt_on.grid(column=0,row=2)
butt_off.grid(column=1,row=2)
butt1.grid(column=0,row=3)
butt2.grid(column=1,row=3)
butt3.grid(column=0,row=4)
butt4.grid(column=1,row=4)

root.mainloop() # event loop needs to created for the windows to stay displayed
