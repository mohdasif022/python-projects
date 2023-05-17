from tkinter import *

main=Tk()
main.geometry("1000x500")
main.title("CoffeeBar")
main.resizable(False,False)


def Reset():
    entry_mocha.delete(0,END)
    entry_capp.delete(0,END)
    entry_amer.delete(0,END)
    entry_dop.delete(0,END)
    entry_cort.delete(0,END)
    entry_mac.delete(0,END)
    entry_red.delete(0,END)

def Total():
    try:a1=int(mocha.get())
    except:a1=0

    try:a2 = int(capp.get())
    except:a2=0

    try:a3=int(amer.get())
    except:a3=0

    try:a4=int(dop.get())
    except:a4=0

    try:a5=int(cort.get())
    except:a5=0

    try:a6=int(mac.get())
    except:a6=0

    try:a7=int(red.get())
    except:a7=0

    #set price
    p1=350*a1
    p2=450*a2
    p3=500*a3
    p4=300*a4
    p5=550*a5
    p6=400*a6
    p7=530*a7

    lbl_total= Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total= Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost =p1+p2+p3+p4+p5+p6+p7
    
    string_bill="Rs",str('%.2f' %totalcost)
    Total_bill.set(string_bill)




Label(text="CoffeeBar",bg="grey3",fg="white",font=("calibri",33,"bold"),width="300",height="2").pack()

#Menu Card
f= Frame(main,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="~Menu~",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Mocha.......Rs 350",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cappuccino.......Rs 450",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Americano.......Rs 500",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Doppio.......Rs 300",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cortado.......Rs 550",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Macchiato.......Rs 400",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Red Eye.......Rs 530",fg="black",bg="lightgreen").place(x=10,y=260)

#BIll
f2 =Frame(main,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill = Label(f2,text="Bill",font=("Gabriola",20,"bold"),bg="lightyellow")
Bill.place(x=120,y=10)

#Order Entry

f1= Frame(main,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

mocha=StringVar()   
capp=StringVar()
amer=StringVar()
dop=StringVar()
cort=StringVar()
mac=StringVar()
red=StringVar()
Total_bill=StringVar()

#Label
lbl_mocha = Label(f1,font=("arai",20,"bold"),text="Mocha",width=12,fg="maroon")
lbl_capp = Label(f1,font=("arai",20,"bold"),text="Cappuccino",width=12,fg="maroon")
lbl_amer = Label(f1,font=("arai",20,"bold"),text="Americano",width=12,fg="maroon")
lbl_dop = Label(f1,font=("arai",20,"bold"),text="Doppio",width=12,fg="maroon")
lbl_cort = Label(f1,font=("arai",20,"bold"),text="Cortado",width=12,fg="maroon")
lbl_mac = Label(f1,font=("arai",20,"bold"),text="Macchiato",width=12,fg="maroon")
lbl_red = Label(f1,font=("arai",20,"bold"),text="Red Eye",width=12,fg="maroon")
lbl_mocha.grid(row=1,column=0)
lbl_capp.grid(row=2,column=0)
lbl_amer.grid(row=3,column=0)
lbl_dop.grid(row=4,column=0)
lbl_cort.grid(row=5,column=0)
lbl_mac.grid(row=6,column=0)
lbl_red.grid(row=7,column=0)


#Entry
entry_mocha = Entry(f1,font=("arai",20,"bold"),textvariable=mocha,bd=6,width=8,bg="honeydew")
entry_capp = Entry(f1,font=("arai",20,"bold"),textvariable=capp,bd=6,width=8,bg="honeydew")
entry_amer = Entry(f1,font=("arai",20,"bold"),textvariable=amer,bd=6,width=8,bg="honeydew")
entry_dop = Entry(f1,font=("arai",20,"bold"),textvariable=dop,bd=6,width=8,bg="honeydew")
entry_cort = Entry(f1,font=("arai",20,"bold"),textvariable=cort,bd=6,width=8,bg="honeydew")
entry_mac = Entry(f1,font=("arai",20,"bold"),textvariable=mac,bd=6,width=8,bg="honeydew")
entry_red = Entry(f1,font=("arai",20,"bold"),textvariable=red,bd=6,width=8,bg="honeydew")
entry_mocha.grid(row=1,column=1)
entry_capp.grid(row=2,column=1)
entry_amer.grid(row=3,column=1)
entry_dop.grid(row=4,column=1)
entry_cort.grid(row=5,column=1)
entry_mac.grid(row=6,column=1)
entry_red.grid(row=7,column=1)

#Buttons
btn_reset = Button(f1,bd=5,fg="black",bg="red",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total = Button(f1,bd=5,fg="black",bg="green",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)








main.mainloop()

