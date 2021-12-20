from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from PIL import Image,ImageTk
#from UserHomePage import UserHomePagee
from confirmed import Confirmed
import mysql.connector

class DriverHomePagee:

    global ans

    def __init__(self,ans):

        self.ans = ans
        ans = ans
 
        # User Home Page GUI
        self.Home_Page_gui = Tk()
        self.Home_Page_gui.title("KUBER")
        self.Home_Page_gui.geometry("500x600")

        # Logo
        canvas = Canvas(self.Home_Page_gui, width = 300, height = 300)      
        canvas.pack(pady=(20,0))     
        img = ImageTk.PhotoImage(file="./images/kuber.png")      
        canvas.create_image(20,20, anchor=NW, image=img) 
        label = Label(image=img)
        label.image = img

        # Name
        self.name = StringVar()
        self.name_label = Label(self.Home_Page_gui, textvariable =self.name,font=("Ubuntu",16,BOLD))
        s = "Hi "+ans[1]+"Welcome To KUBER !"
        self.name.set(s)
        self.name_label.pack()
        self.name_label.place(x=150,y=180)
     
        
        self.on_to_off()
        self.Home_Page_gui.mainloop()


    def on_to_off(self):
        # History
        self.on_Button = Button(self.Home_Page_gui, text ="ON",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.delete_but)
        self.on_Button.pack()
        self.on_Button.place(x=220,y=250)      
           


    def off_to_on(self):

        self.off_Button = Button(self.Home_Page_gui, text ="OFF",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.delete_butt)
        self.off_Button.pack()
        self.off_Button.place(x=220,y=250)  

        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "Select pickuppoint,destinationpoint,Fare from Location"
        cur.execute(queryy)
        ans = cur.fetchone()
        conn.close()

        # Pickup Point
        self.PickupPoint = StringVar()
        self.PickupPointt = StringVar()
        self.PickupPoint_label = Label(self.Home_Page_gui, textvariable =self.PickupPoint,font=("Ubuntu",16,BOLD))
        self.PickupPoint.set("Pickup Point :")
        self.PickupPoint_label.pack()
        self.PickupPoint_label.place(x=65,y=320)
        self.PickupPoint_text = Label(self.Home_Page_gui, textvariable =self.PickupPointt,font=("Ubuntu",16,BOLD))
        self.PickupPointt.set(ans[0])
        self.PickupPoint_text.pack()
        self.PickupPoint_text.place(x=65,y=350)        
        
        # Destination Point
        self.DestinationPoint = StringVar()
        self.DestinationPointt = StringVar()
        self.DestinationPoint_label = Label(self.Home_Page_gui, textvariable =self.DestinationPoint,font=("Ubuntu",16,BOLD))
        self.DestinationPoint.set("Destination Point :")
        self.DestinationPoint_label.pack()
        self.DestinationPoint_label.place(x=65,y=395)
        self.DestinationPoint_text = Label(self.Home_Page_gui, textvariable =self.DestinationPointt,font=("Ubuntu",16,BOLD))
        self.DestinationPointt.set(ans[1])
        self.DestinationPoint_text.pack()
        self.DestinationPoint_text.place(x=65,y=425)   
        
        # Fare
        self.fare = StringVar()
        self.faree = StringVar()
        self.fare_label = Label(self.Home_Page_gui, textvariable =self.fare,font=("Ubuntu",16,BOLD))
        self.fare.set("Fare :")
        self.fare_label.pack()
        self.fare_label.place(x=65,y=465)
        self.fare_text = Label(self.Home_Page_gui, textvariable =self.faree,font=("Ubuntu",16,BOLD))
        self.faree.set(ans[2])
        self.fare_text.pack()
        self.fare_text.place(x=65,y=495)   

        # Book
        self.Book_Button = Button(self.Home_Page_gui, text ="Accept",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.driver_distance)
        self.Book_Button.pack()
        self.Book_Button.place(x=65,y=530)



    def delete_but(self):  
         self.on_Button.destroy()
         self.off_to_on()
    def delete_butt(self):  
         self.off_Button.destroy()
         self.PickupPoint_label.destroy()
         self.PickupPoint_text.destroy()
         self.DestinationPoint_label.destroy()
         self.DestinationPoint_text.destroy()
         self.Book_Button.destroy()
         self.on_to_off()

    def driver_distance(self):
        
        self.Book_Button.destroy()
        self.Home_Page_gui.geometry("500x750")
       
        # distance
        self.distance_to_pick = StringVar()
        self.label = Label(self.Home_Page_gui, textvariable = self.distance_to_pick,font=("Ubuntu",16,BOLD))
        self.distance_to_pick.set("Distance To Reach the Pick up Point :")
        self.label.pack()
        self.label.place(x=65,y=530)
        self.distance_to_pick_text = Text(self.Home_Page_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.distance_to_pick_text.pack()
        self.distance_to_pick_text.place(x=65,y=560)
        
        # time
        self.Time_to_pick = StringVar()
        self.Time_to_pick_label = Label(self.Home_Page_gui, textvariable =self.Time_to_pick,font=("Ubuntu",16,BOLD))
        self.Time_to_pick.set("Time To Reach the Pick up Point :")
        self.Time_to_pick_label.pack()
        self.Time_to_pick_label.place(x=65,y=600)
        self.Time_to_pick_text = Text(self.Home_Page_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.Time_to_pick_text.pack()
        self.Time_to_pick_text.place(x=65,y=630)

        # Submit
        self.submit_Button = Button(self.Home_Page_gui, text ="Submit",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.driver_distance_details)
        self.submit_Button.pack()
        self.submit_Button.place(x=65,y=675)
    
    def driver_distance_details(self):

        dis = self.distance_to_pick_text.get(1.0,END)
        time = self.Time_to_pick_text.get(1.0,END)

        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "Insert Into Time (distance,Time) values (%s,%s)"
        val = (dis,time)
        cur.execute(queryy,val)
        conn.commit()
        conn.close()
        print(cur)

        self.label.destroy()   
        self.distance_to_pick_text.destroy()     
        self.Time_to_pick_label.destroy()
        self.Time_to_pick_text.destroy()
        self.submit_Button.destroy()

        self.Home_Page_gui.geometry("500x600")
        
        # Book
        self.Arrived_Button = Button(self.Home_Page_gui, text ="Arrived",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.arrived)
        self.Arrived_Button.pack()
        self.Arrived_Button.place(x=65,y=530)


    def arrived(self):
        
        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()

        q1 = "DELETE FROM Location;"
        q2 = "DELETE FROM Time;"
        cur.execute(q1)
        cur.execute(q2)
        conn.commit()
        conn.close()

        self.Home_Page_gui.destroy()

        self.Greet_Page_gui = Tk()
        self.Greet_Page_gui.title("KUBER")
        self.Greet_Page_gui.geometry("600x300")

        # Logo
        canvas = Canvas(self.Greet_Page_gui, width = 300, height = 300)      
        canvas.pack(pady=(20,0))     
        img = ImageTk.PhotoImage(file="./images/kuber.png")      
        canvas.create_image(20,20, anchor=NW, image=img) 
        label = Label(image=img)
        label.image = img

        self.greet = StringVar()
        self.greet_label = Label(self.Greet_Page_gui, textvariable =self.greet,font=("Ubuntu",20,BOLD))
        self.greet.set("Thank! You For Using KUBER")
        self.greet_label.pack()
        self.greet_label.place(x=100,y=190)









        

#ans = ('123\n', 'driver\n', 123, 'mho4ab123\n')
#obj = DriverHomePagee(ans)