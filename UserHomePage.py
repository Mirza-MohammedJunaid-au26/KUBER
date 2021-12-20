from tkinter import *
import tkinter as tk
import tkinter as t
from tkinter.font import BOLD
from PIL import Image,ImageTk
from confirmed import Confirmed
import mysql.connector

class UserHomePagee:

    global ans

    def __init__(self,ans):

        self.ans = ans

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

        # Pickup Point
        self.PickupPoint = StringVar()
        self.PickupPoint_label = Label(self.Home_Page_gui, textvariable =self.PickupPoint,font=("Ubuntu",16,BOLD))
        self.PickupPoint.set("Pickup Point :")
        self.PickupPoint_label.pack()
        self.PickupPoint_label.place(x=65,y=270)
        self.PickupPoint_text = Text(self.Home_Page_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.PickupPoint_text.pack()
        self.PickupPoint_text.place(x=65,y=300)        
        
        # Destination Point
        self.DestinationPoint = StringVar()
        self.DestinationPoint_label = Label(self.Home_Page_gui, textvariable =self.DestinationPoint,font=("Ubuntu",16,BOLD))
        self.DestinationPoint.set("Destination Point :")
        self.DestinationPoint_label.pack()
        self.DestinationPoint_label.place(x=65,y=345)
        self.DestinationPoint_text = Text(self.Home_Page_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.DestinationPoint_text.pack()
        self.DestinationPoint_text.place(x=65,y=375)   
        
        # Fare
        self.Fare = StringVar()
        self.Fare_label = Label(self.Home_Page_gui, textvariable =self.Fare,font=("Ubuntu",16,BOLD))
        self.Fare.set("Fare :")
        self.Fare_label.pack()
        self.Fare_label.place(x=65,y=420)
        self.Fare_text = Text(self.Home_Page_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.Fare_text.pack()
        self.Fare_text.place(x=65,y=450)   

        # Book
        self.Book_Button = Button(self.Home_Page_gui, text ="Book",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.cab_book)
        self.Book_Button.pack()
        self.Book_Button.place(x=65,y=500)     

        
        
        # History
        self.History_Button = Button(self.Home_Page_gui, text ="History",font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.show_History)
        self.History_Button.pack()
        self.History_Button.place(x=335,y=500)     

        self.Home_Page_gui.mainloop()

    def cab_book(self):

        pick = self.PickupPoint_text.get(1.0,END)
        des =  self.DestinationPoint_text.get(1.0,END)
        fare = self.Fare_text.get(1.0,END)

        # Database Connection
        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "Insert Into Location (pickuppoint,destinationpoint,Fare) values (%s,%s,%s)"
        query = "Insert Into History (pick,dest,Fare) values (%s,%s,%s)"
        val = (pick,des,fare)
        cur.execute(queryy,val)
        cur.execute(query,val)
        conn.commit()
        conn.close()

        self.check()
    
    def details(self,det):

        self.ans = det

        # Booked 
        self.cab_book = StringVar()
        self.cab_book_label = t.Label(self.Home_Page_gui, textvariable =self.cab_book,font=("Ubuntu",16,BOLD))
        self.cab_book.set("Your Ride Has been Booked by :")
        self.cab_book_label.pack(pady=30)
        
        self.driver_name = StringVar()
        self.driver_name_label = t.Label(self.Home_Page_gui, textvariable =self.driver_name,justify=LEFT,font=("Ubuntu",16,BOLD))
        self.driver_name.set("Driver Name :"+self.ans[1])
        self.driver_name_label.pack()
        self.driver_name_label.place(x=65,y=100)
        
        self.mob = StringVar()
        self.mob_label = t.Label(self.Home_Page_gui, textvariable =self.mob,font=("Ubuntu",16,BOLD))
        self.mob.set("Phone No :"+str(self.ans[2]))
        self.mob_label.pack()
        self.mob_label.place(x=65,y=130)
        
        self.veh = StringVar()
        self.veh_label = t.Label(self.Home_Page_gui, textvariable =self.veh,font=("Ubuntu",16,BOLD))
        self.veh.set("Vehicle No :"+self.ans[3])
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
        self.dist_label = t.Label(self.Home_Page_gui, textvariable =self.dist,font=("Ubuntu",16,BOLD))
        self.dist.set("Distance from the Pickup Point :"+self.anss[0])
        self.dist_label.pack()
        self.dist_label.place(x=65,y=190)
        
        self.time = StringVar()
        self.time_label = t.Label(self.Home_Page_gui, textvariable =self.time,font=("Ubuntu",16,BOLD))
        self.time.set("Time to Reach :"+self.anss[1])
        self.time_label.pack()
        self.time_label.place(x=65,y=220)

        #self.Home_Page_gui.mainloop()

    def check(self):
        self.PickupPoint_label.destroy()
        self.PickupPoint_text.destroy()
        self.DestinationPoint_label.destroy()
        self.DestinationPoint_text.destroy()
        self.Fare_label.destroy()
        self.Fare_text.destroy()
        self.Book_Button.destroy()
        self.History_Button.destroy()

        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "SELECT pickuppoint,destinationpoint,Fare from Location"
        cur.execute(queryy)
        loc = cur.fetchone()
        conn.close()

         # Pickup Point
        self.PickupPoint = StringVar()
        self.PickupPoint_label = Label(self.Home_Page_gui, textvariable =self.PickupPoint,font=("Ubuntu",16,BOLD))
        self.PickupPoint.set("Pickup Point :")
        self.PickupPoint_label.pack()
        self.PickupPoint_label.place(x=65,y=270)
        self.PickupPointt = StringVar()
        self.PickupPoint_text = Label(self.Home_Page_gui, textvariable =self.PickupPointt,font=("Ubuntu",16,BOLD))
        self.PickupPointt.set(loc[0])
        self.PickupPoint_text.pack()
        self.PickupPoint_text.place(x=65,y=300)        
        
        # Destination Point
        self.DestinationPoint = StringVar()
        self.DestinationPoint_label = Label(self.Home_Page_gui, textvariable =self.DestinationPoint,font=("Ubuntu",16,BOLD))
        self.DestinationPoint.set("Destination Point :")
        self.DestinationPoint_label.pack()
        self.DestinationPoint_label.place(x=65,y=345)
        self.DestinationPointt = StringVar()
        self.DestinationPoint_text = Label(self.Home_Page_gui, textvariable =self.DestinationPointt,font=("Ubuntu",16,BOLD))
        self.DestinationPointt.set(loc[1])
        self.DestinationPoint_text.pack()
        self.DestinationPoint_text.place(x=65,y=375)   
        
        # Destination Point
        self.fare = StringVar()
        self.fare_label = Label(self.Home_Page_gui, textvariable =self.fare,font=("Ubuntu",16,BOLD))
        self.fare.set("Fare :")
        self.fare_label.pack()
        self.fare_label.place(x=65,y=420)
        self.faret = StringVar()
        self.fare_text = Label(self.Home_Page_gui, textvariable =self.faret,font=("Ubuntu",16,BOLD))
        self.faret.set(loc[2])
        self.fare_text.pack()
        self.fare_text.place(x=65,y=450)   


        self.check_Button = Button(self.Home_Page_gui, text ="Check",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.confirm)
        self.check_Button.pack()
        self.check_Button.place(x=65,y=500) 

    def confirm(self):
        self.Home_Page_gui.destroy()
        obj = Confirmed()
    
    def show_History(self):

        self.Home_Page_gui.destroy()

        # User Home Page GUI
        self.History_Page_gui = Tk()
        self.History_Page_gui.title("KUBER")
        self.History_Page_gui.geometry("500x500")

        self.hist = StringVar()
        self.hist_text = Label(self.History_Page_gui, justify=CENTER,textvariable =self.hist,font=("Ubuntu",24,BOLD))
        self.hist.set("HISTORY")
        self.hist_text.pack(pady=10)

        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "SELECT pick,dest,Fare from History"
        cur.execute(queryy)
        history = cur.fetchall()
        for i in history:
            self.pic = StringVar()
            self.pic_text = Label(self.History_Page_gui, textvariable =self.pic,font=("Ubuntu",16,BOLD))
            self.pic.set("Pickup Point :"+i[0])
            self.pic_text.pack()
            self.dess = StringVar()
            self.dess_text = Label(self.History_Page_gui, textvariable =self.dess,font=("Ubuntu",16,BOLD))
            self.dess.set("Destination Point :"+i[1])
            self.dess_text.pack()
            self.far = StringVar()
            self.far_text = Label(self.History_Page_gui, textvariable =self.far,font=("Ubuntu",16,BOLD))
            self.far.set("Fare :"+i[2])
            self.far_text.pack()
        conn.close()
        
        self.back_Button = Button(self.History_Page_gui, text ="Back",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.back_to_user)
        self.back_Button.pack()
    
    def back_to_user(self):

        self.History_Page_gui.destroy()
        self.__init__(self.ans)





    


# ans = ('123\n', 'driver\n', 123, 'mho4ab123\n')
# obj = UserHomePagee(ans)


