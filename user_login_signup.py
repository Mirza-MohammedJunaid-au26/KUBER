from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from PIL import Image,ImageTk
from UserHomePage import UserHomePagee
import mysql.connector

class USER_LS:

    def __init__(self):

        # GUI
        self.gui = Tk()
        self.gui.title("KUBER")
        self.gui.geometry("500x500")

        # Logo
        self.canvas = Canvas(self.gui, width = 300, height = 300)      
        self.canvas.pack(pady=(20,0),padx=(90,0))     
        self.img= (Image.open("./images/big_user.png"))
        resized_image= self.img.resize((180,180), Image.ANTIALIAS)
        new_user_image= ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(20,20, anchor=NW, image=new_user_image)
        label = Label(image=new_user_image)
        label.image = new_user_image

        self.home()

        # MAIN
        #self.gui.mainloop()

    def home(self):

        #LOGIN
        self.LOGIN_Button = Button(self.gui, text ="LOGIN",justify=CENTER,font=("Ubuntu",18,BOLD),bg="#000",fg="#ffc000",relief=RAISED,command=self.gui_delete_login)
        self.LOGIN_Button.pack(pady= 8)
        self.LOGIN_Button.place(x=200,y=250)
        
        #SIGNUP
        self.SIGNUP_Button = Button(self.gui, text ="SIGNUP",justify=CENTER,font=("Ubuntu",18,BOLD),bg="#000",fg="#ffc000",relief=RAISED,command=self.gui_delete_signup)
        self.SIGNUP_Button.pack(pady= 8)
        self.SIGNUP_Button.place(x=193,y=300)

    
    def gui_delete_login(self):
        self.gui.destroy()
        self.Login_gui()

    def gui_delete_signup(self):
        self.gui.destroy()
        self.Signup_gui()


    def Login_gui(self):

         # GUI
        self.login_gui = Tk()
        self.login_gui.title("KUBER")
        self.login_gui.geometry("530x530")

        # Logo
        self.canvas = Canvas(self.login_gui, width = 300, height = 300)      
        self.canvas.pack(pady=(20,0),padx=(90,0))     
        self.img= (Image.open("./images/big_user.png"))
        resized_image= self.img.resize((180,180), Image.ANTIALIAS)
        new_user_image= ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(20,20, anchor=NW, image=new_user_image)
        label = Label(image=new_user_image)
        label.image = new_user_image

        self.User_Login()

    def User_Login(self):

        # Email ID
        self.e_mail = StringVar()
        self.label = Label(self.login_gui, textvariable = self.e_mail,font=("Ubuntu",16,BOLD))
        self.e_mail.set("G-Mail :")
        self.label.pack()
        self.label.place(x=65,y=250)
        self.email_text = Text(self.login_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.email_text.pack()
        self.email_text.place(x=65,y=280)
        
        # Password
        self.pswd = StringVar()
        self.pswd_label = Label(self.login_gui, textvariable =self.pswd,font=("Ubuntu",16,BOLD))
        self.pswd.set("Password :")
        self.pswd_label.pack()
        self.pswd_label.place(x=65,y=320)
        self.pswd_text = Text(self.login_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.pswd_text.pack()
        self.pswd_text.place(x=65,y=350)

        # Submit
        self.submit_Button = Button(self.login_gui, text ="LOGIN",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.Login_Check)
        self.submit_Button.pack()
        self.submit_Button.place(x=210,y=410)

        # Login
        self.log_Button = Button(self.login_gui, text ="SIGNUP",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.login_to_signup)
        self.log_Button.pack(side=LEFT)
        self.log_Button.place(x=85,y=460)
        
        # back
        self.back_Button = Button(self.login_gui, text ="BACK",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.login_to_back)
        self.back_Button.pack(side=RIGHT)
        self.back_Button.place(x=315,y=460)
    
    
    def Login_Check(self):
        
        global ans

        e_mail =  self.email_text.get(1.0,END)
        pswd =  self.pswd_text.get(1.0,END)
        # Database Connection
        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        try:
            cur = conn.cursor()
            # q = "SELECT * FROM User where gmail = %s"%(e_maill)
            q = "SELECT password,Name,Mob FROM User where gmail = %s;"
            val = (e_mail,)
            cur.execute(q,val)
            ans = cur.fetchone()
            # conn.commit()
        except Exception as err:
            print("Exception",err)
        finally:
            conn.close()

        if ans[0] == pswd:       
            self.Send_To_UserHome(ans)


    def Signup_gui(self):    

          # GUI
        self.signup_gui = Tk()
        self.signup_gui.title("KUBER")
        self.signup_gui.geometry("500x600")

        # Logo
        self.canvas = Canvas(self.signup_gui, width = 300, height = 300)      
        self.canvas.pack(pady=(20,0),padx=(90,0))     
        self.img= (Image.open("./images/big_user.png"))
        resized_image= self.img.resize((180,180), Image.ANTIALIAS)
        new_user_image= ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(20,20, anchor=NW, image=new_user_image)
        label = Label(image=new_user_image)
        label.image = new_user_image

        self.User_SignUp()



    def User_SignUp(self):
       
        # Name
        self.name = StringVar()
        self.name_label = Label(self.signup_gui, textvariable = self.name,font=("Ubuntu",16,BOLD))
        self.name.set("Name :")
        self.name_label.pack()
        self.name_label.place(x=65,y=220)
        self.name_text = Text(self.signup_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.name_text.pack()
        self.name_text.place(x=65,y=250)
        
         # Name
        self.mob = IntVar()
        self.mob_label = Label(self.signup_gui, textvariable = self.mob,font=("Ubuntu",16,BOLD))
        self.mob.set("Mobile No :")
        self.mob_label.pack()
        self.mob_label.place(x=65,y=290)
        self.mob_text = Text(self.signup_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.mob_text.pack()
        self.mob_text.place(x=65,y=320)

        # Email ID
        self.e_mail = StringVar()
        self.email_label = Label(self.signup_gui, textvariable = self.e_mail,font=("Ubuntu",16,BOLD))
        self.e_mail.set("G-Mail :")
        self.email_label.pack()
        self.email_label.place(x=65,y=360)
        self.text = Text(self.signup_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.text.pack()
        self.text.place(x=65,y=390)
        
        # Password
        self.pswd = StringVar()
        self.pswd_label = Label(self.signup_gui, textvariable =self.pswd,font=("Ubuntu",16,BOLD))
        self.pswd.set("Password :")
        self.pswd_label.pack()
        self.pswd_label.place(x=65,y=430)
        self.pswd_text = Text(self.signup_gui,font=("Ubuntu",16),height = 1.2, width = 30,pady=3,padx=5)
        self.pswd_text.pack()
        self.pswd_text.place(x=65,y=460)

        # Submit
        self.submit_Button = Button(self.signup_gui, text ="Submit",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.fetch_SignUp_Value)
        self.submit_Button.pack()
        self.submit_Button.place(x=200,y=510)
        
        # Login
        self.log_Button = Button(self.signup_gui, text ="LOGIN",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.signup_to_login)
        self.log_Button.pack(side=LEFT)
        self.log_Button.place(x=85,y=550)
        
        # back
        self.back_Button = Button(self.signup_gui, text ="BACK",justify=CENTER,font=("Ubuntu",16,BOLD),relief=RAISED,bg="#000",fg="#ffc000",command=self.signup_to_back)
        self.back_Button.place(x=315,y=550)
    

    def fetch_SignUp_Value(self):

        name = self.name_text.get(1.0,END)
        mob =  self.mob_text.get(1.0,END)
        new_mob = int(mob)
        e_mail =  self.text.get(1.0,END)
        pswd =  self.pswd_text.get(1.0,END)
        # Database Connection
        conn = mysql.connector.connect(host="localhost",user="spidy",passwd="123",database="KUBER")
        cur = conn.cursor()
        queryy = "Insert Into User (Name,Mob,gmail,password) values (%s,%s,%s,%s)"
        val = (name,new_mob,e_mail,pswd)
        cur.execute(queryy,val)
        conn.commit()
        conn.close()
        print(cur)

        self.signup_to_login()




    def login_to_signup(self):
        
        self.login_gui.destroy()
        self.Signup_gui()
    
    def login_to_back(self):
        
        self.login_gui.destroy()
        self.__init__()

    def signup_to_login(self):

        self.signup_gui.destroy()
        self.Login_gui()

    def signup_to_back(self):

        self.signup_gui.destroy()
        self.__init__()

    def Send_To_UserHome(self,ans):
        self.login_gui.destroy()
        obj = UserHomePagee(ans)