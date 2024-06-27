from tkinter import*
from customtkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import webbrowser

class Developer:
    def __init__(self, root,main_root):
        self.root = root
        self.main_root = main_root
        self.root.geometry("1360x688+0+0")
        self.root.title("Face Recoginiton System")
        self.root.state('zoomed')

        #background image
        img4=Image.open(r"Used Pictures\developerW.png")
        img4=img4.resize((1400,700),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        label4=Label(self.root,image=self.photoimg4)
        label4.place(x=0,y=0,width=1400,height=700)

        #1st image
        img3=Image.open(r"Used Pictures\firstImg.png")
        img3=img3.resize((1400,100),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        label3=Label(label4,image=self.photoimg3)
        label3.place(x=0,y=0,width=1400,height=100)

        

        #text
        about=Label(label4,text='About Developers',font=('Arial',20,),fg='black',bg='white',anchor='center')
        about.place(x=-2,y=100,width=1400,height=42)

        back_button=CTkButton(about,command=self.back_button,width=83,height=42,text='Back',font=('times new roman',15,'bold'),fg_color='black',corner_radius=8,bg_color='white',text_color='white',hover_color='gray')
        back_button.place(x=-2,y=-2)

        

        # main frame
        std_frame=Frame(label4,bd=2,bg='white')
        std_frame.place(x=420,y=195,width=600,height=450)

        img7=Image.open(r"Used Pictures\developerE.png")
        img7=img7.resize((600,450),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        label7=Label(std_frame,image=self.photoimg7)
        label7.place(x=-2,y=-2,width=600,height=450)


        rajani=Label(label7,text='Nikhil Sachan',font=('Arial',10,),fg='black',bg='white')
        rajani.place(x=15,y=50,width=250,height=50)

        meezan=Label(label7,text='Meezan Khan',font=('Arial',10,),fg='black',bg='white')
        meezan.place(x=15,y=125,width=250,height=50)

        nikhil=Label(label7,text='Rajani Ranjan Jha',font=('Arial',10,),fg='black',bg='white')
        nikhil.place(x=15,y=200,width=250,height=50)

        shishir=Label(label7,text='Rohan Kumar',font=('Arial',10,),fg='black',bg='white')
        shishir.place(x=15,y=275,width=250,height=50)

        rohan=Label(label7,text='Shishir Ranjan',font=('Arial',10,),fg='black',bg='white')
        rohan.place(x=15,y=350,width=250,height=50)

        # rajani_E=Label(std_frame,text='rajani_2312res829@iitp.ac.in',font=('Arial',10,),fg='black')
        # rajani_E.place(x=320,y=50,width=250,height=50)

        # meezan_E=Label(std_frame,text='meezan_2312res829@iitp.ac.in',font=('Arial',10,),fg='black')
        # meezan_E.place(x=320,y=125,width=250,height=50)

        # nikhil_E=Label(std_frame,text='nikhil_2312res829@iitp.ac.in',font=('Arial',10,),fg='black')
        # nikhil_E.place(x=320,y=200,width=250,height=50)

        # shishir_E=Label(std_frame,text='shishir_2312res829@iitp.ac.in',font=('Arial',10,),fg='black')
        # shishir_E.place(x=320,y=275,width=250,height=50)

        # rohan_E=Label(std_frame,text='rohan_2312res829@iitp.ac.in',font=('Arial',10,),fg='black')
        # rohan_E.place(x=320,y=350,width=250,height=50)

        # Function to open mail client
        def open_mail(email):
            webbrowser.open(f"mailto:{email}")

        # Creating email labels
        emails = [
            ("nikhil_2312res935@iitp.ac.in", 50),
            ("meezan_2312res380@iitp.ac.in", 125),
            ("rajani_2312res829@iitp.ac.in", 200),
            ("rohan_2312res839@iitp.ac.in", 275),
            ("shishir_2312res600@iitp.ac.in", 350),
        ]

        for email, y_position in emails:
            email_label = Label(label7, text=email, font=('Arial', 10,'bold'), fg='blue', cursor="hand2")
            email_label.place(x=335, y=y_position, width=250, height=50)
            email_label.bind("<Button-1>", lambda e, email=email: open_mail(email))
        
    #_____________back button_________
    def back_button(self):
        self.root.destroy()
        self.main_root.deiconify()

if __name__ == "__main__":
    root = Tk()
    obj2 = Developer(root,root)
    root.mainloop()