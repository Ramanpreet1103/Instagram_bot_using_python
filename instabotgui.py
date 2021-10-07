from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.font import Font
from tkinter import ttk
design = Tk()

bg = PhotoImage(file="instabot.png")

var = StringVar()
var2 = StringVar()

def func():
    if var.get() !="" and var2.get() =="":
        messagebox.showwarning("warning","Please Enter your password first")

    elif var.get() =="" and var2.get() != "":
        messagebox.showwarning("Warning","Please enter your username first")

    elif var.get() == "" and var2.get() == "":
        messagebox.showwarning("warning","Please enter your id and password first")
    
    else:
        messagebox.showinfo("success","thanks for giving your deatails")

def func4():
    if var.get()!="" and var2.get()!="":
        username = var.get()
        password = var2.get()
        return(password)







    

mylabel = Label(design,image=bg)
mylabel.place(x=0,y=0,relwidth=1,relheight=1)

design.title("Instagram Bot")

design.iconbitmap("bot.ico")

design.minsize(width = 1280,height = 720)
design.maxsize(width = 1280,height = 720)

lbl1 =Label(design,text="username :",bg="#e91e63",font = "comicsans")
lbl1.place(x=700,y=50)

#entry
ent = Entry(design,bg="#6200ea",fg="#000000",textvariable=var)
ent.place(x=830,y=50,width=200,height=30)

#for password

lbl2 =Label(design,text="password :",bg="#e91e63",font = "comicsans")
lbl2.place(x=700,y=120)

#entry
ent2 = Entry(design,bg="#6200ea",fg="#000000",textvariable=var2,show="\u2022",font=("arial",14))
ent2.place(x=830,y=120,width=200,height=30)

#button


# btn = Button(design,text ="SUBMIT",font="arial",bd=3,command=func)
btn = Button(design,text ="SUBMIT",font="arial",bd=3, command=lambda:[func(),func4()])
btn.place(x=780,y=170)

lbl3 = Label(design,text="I N S T A G R A M   B O T ",font="arial",bg="#f12b7e")
lbl3.pack()

lbl4 = Label(text="what you want me to do?",bg="#e91e63",font = "comicsans")
lbl4.place(x=700,y=250)

"""com = ttk.Combobox(design,width=30,height=90)
com ["values"] =["auto comment and like posts","auto message replier to who liked your posts","Both"]
com["state"] = "Read Only"
com.current(0)
com.place(x=980,y=254)"""

Checkbtn1 = IntVar()
checkbtn2 = IntVar()

    



select1 = Checkbutton(design,text = "comment and like posts of hashtag given by me",variable= Checkbtn1,offvalue=0,onvalue=1)
select2 = Checkbutton(design,text = "Reply to all who liked my post",variable=checkbtn2,offvalue=0,onvalue=1 )

select1.place(x=700,y=300)
select2.place(x=1000,y=300)

 

lbl5 = Label(text="Enter hashtag with # at the beggining",bg="#e91e63",font = "comicsans")
lbl5.place(x=700,y=360)
var3 = StringVar()

ent3 = Entry(design,fg="#000000",bg="#6200ea",textvariable=var3)
ent3.place(x=700,y=420)

def func2():
    Checkbtn1.get()
    checkbtn2.get()
    print(Checkbtn1.get())
    print(checkbtn2.get())
    if Checkbtn1.get() == 1 and checkbtn2.get() == 0:
        from instagrambot import openinsta
        openinsta()
    
    if Checkbtn1.get() == 0 and checkbtn2.get() == 1:
        from instagrambotfile2 import InstagramBot
        obj = InstagramBot()
        obj.openAndLogin()
        obj.getWhoLikedPosts()
        obj.sendMessage()




"""def func3():
    if var3.get() == "":
        messagebox.showwarning("WARNING","Please enter hashtag in the entry box")"""

        

btn2 = Button(text="SUBMIT",command=func2)
btn2.place(x=700,y=460)



design.mainloop()
