from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from PIL import Image,ImageTk
from user_login_signup import USER_LS
from driver_login_signup import DRIVER_LS


class FrontPage():

    def __init__(self):

        # Front Page GUI
        self.gui = Tk()
        self.gui.title("KUBER")
        self.gui.geometry("300x300")

        # Logo
        canvas = Canvas(self.gui, width = 300, height = 300)      
        canvas.pack(pady=(20,0))     
        img = ImageTk.PhotoImage(file="./images/kuber.png")      
        canvas.create_image(20,20, anchor=NW, image=img) 
        label = Label(image=img)
        label.image = img

        # User Button
        user_button_img = PhotoImage(file = r"./images/USER_BUTTON.png")
        user_Button = Button(self.gui, text ="USER",justify=CENTER,font=("Ubuntu",12,BOLD),fg="#ffc000",bg="#000",relief=RAISED,image=user_button_img,compound = RIGHT,command=self.User_loginn)
        user_Button.pack()
        user_Button.place(x=100,y=180)

        # Driver Button
        employer_button_img = PhotoImage(file = r"./images/DRIVER_BUTTON.png")
        Employer_Button = Button(self.gui, text ="DRIVER",justify=CENTER,font=("Ubuntu",12,BOLD),fg="#ffc000",bg="#000",relief=RAISED,image=employer_button_img,compound = RIGHT,command=self.Driver_loginn)
        Employer_Button.pack()
        Employer_Button.place(x=90,y=220)

        # Main
        self.gui.mainloop()

    def User_loginn(self):
        self.gui.destroy()
        obj = USER_LS()
        obj.home()
    
    def Driver_loginn(self):
        self.gui.destroy()
        obj = DRIVER_LS()
        obj.home()

obj = FrontPage()


