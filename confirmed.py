from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from PIL import Image,ImageTk
#from UserHomePage import UserHomePagee
import mysql.connector


class Confirmed:

    def __init__(self):

        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "SELECT Name,Mob,vehNo from Driver"
        cur.execute(queryy)
        self.ans = cur.fetchone()
        conn.close()


        # User details GUI
        self.details_gui = Tk()
        self.details_gui.title("KUBER")
        self.details_gui.geometry("500x300")

        # Booked 
        self.cab_book = StringVar()
        self.cab_book_label = Label(self.details_gui, textvariable =self.cab_book,font=("Ubuntu",16,BOLD))
        self.cab_book.set("Your Ride Has been Booked by :")
        self.cab_book_label.pack(pady=30)
        
        self.driver_name = StringVar()
        self.driver_name_label = Label(self.details_gui, textvariable =self.driver_name,justify=LEFT,font=("Ubuntu",16,BOLD))
        self.driver_name.set("Driver Name :"+self.ans[0])
        self.driver_name_label.pack()
        self.driver_name_label.place(x=65,y=100)
        
        self.mob = StringVar()
        self.mob_label = Label(self.details_gui, textvariable =self.mob,font=("Ubuntu",16,BOLD))
        self.mob.set("Phone No :"+str(self.ans[1]))
        self.mob_label.pack()
        self.mob_label.place(x=65,y=130)
        
        self.veh = StringVar()
        self.veh_label = Label(self.details_gui, textvariable =self.veh,font=("Ubuntu",16,BOLD))
        self.veh.set("Vehicle No :"+self.ans[2])
        self.veh_label.pack()
        self.veh_label.place(x=65,y=160)

        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        try:
            cur = conn.cursor()
            # q = "SELECT * FROM User where gmail = %s"%(e_maill)
            q = "SELECT distance,Time FROM Time"
            cur.execute(q)
            self.anss = cur.fetchone()
            # conn.commit()
        except Exception as err:
            print("Exception",err)
        finally:
            conn.close()
        
        self.dist = StringVar()
        self.dist_label = Label(self.details_gui, textvariable =self.dist,font=("Ubuntu",16,BOLD))
        self.dist.set("Distance from the Pickup Point :"+self.anss[0])
        self.dist_label.pack()
        self.dist_label.place(x=65,y=190)
        
        self.time = StringVar()
        self.time_label = Label(self.details_gui, textvariable =self.time,font=("Ubuntu",16,BOLD))
        self.time.set("Time to Reach :"+self.anss[1])
        self.time_label.pack()
        self.time_label.place(x=65,y=220)

        self.details_gui.mainloop()

# ans = ('123\n', 'driver\n', 123, 'mho4ab123\n')
#obj = Confirmed(ans)