from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
import tkinter
import mysql.connector




class LibraryMangementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x800")
        
        #=============Variable==================
        
        self.member=StringVar()
        self.prn=StringVar()
        self.id=StringVar()
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.adress1=StringVar()
        self.adress2=StringVar()
        self.postcode=StringVar()
        self.mobile=StringVar()
        self.bookid=StringVar()
        self.booktittle=StringVar()
        self.author=StringVar()
        self.dateborrowed=StringVar()
        self.datedue=StringVar()
        self.daysonbook=StringVar()
        self.latefine=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()
    
    
    #=======================================================================================================================

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Library Management System",
                         fg="maroon", bg="powder blue", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ==================DATA FRAME==================
        DataFrame = Frame(self.root, bd=20, relief=RIDGE,bg="powder blue")
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                   font=("times new roman", 12, "bold"), text="Library Members")
        DataFrameLeft.place(x=0, y=5, width=910, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                    font=("times new roman", 12, "bold"), text="Book Details")
        DataFrameRight.place(x=930, y=5, width=530, height=350)

        # ================Buttons Frame===================

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE,
                            padx=20, bg="powder blue")
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        # ================Details Frame===================

        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE, padx=2)
        DetailsFrame.place(x=0, y=600, width=1530, height=190)
        
        
        

    # ================Data Frame Left===================
    
    

        lblMember = Label(DataFrameLeft,  font=(
            "arial", 12, "bold"),text="Member", padx=2)
        lblMember.grid(row=0, column=0)

        comMember = ttk.Combobox(
            DataFrameLeft, state="readonly", font=("arial", 12, "bold"),textvariable=self.member, width=33)
        comMember["values"] = ("Admin", "Student", "Teacher")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPrn = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Reg Number ", padx=2)
        lblPrn.grid(row=1, column=0, sticky=W)
        txtPrn = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.prn, width=35)
        txtPrn.grid(row=1, column=1)

        lblIdNo = Label(DataFrameLeft, font=("arial", 12, "bold"),
                        text="Id Number ", padx=2, pady=4)
        lblIdNo.grid(row=2, column=0, sticky=W)
        txtIdNo = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.id, width=35)
        txtIdNo.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="First Name ", padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.firstname, width=35)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=(
            "arial", 12, "bold"),text="Last Name ", padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.lastname , width=35)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Address1", padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.adress1, width=35)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Address2 ", padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.adress2, width=35)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Post Code ", padx=2, pady=4)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.postcode, width=35)
        txtPostCode.grid(row=7, column=1)

        lblMobileNo = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Mobile ", padx=2, pady=6)
        lblMobileNo.grid(row=8, column=0, sticky=W)
        txtMobileNo = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.mobile, width=35)
        txtMobileNo.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Book Id ", padx=2)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.bookid, width=35)
        txtBookId.grid(row=0, column=3)

        lblBookTittle = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Book Tittle ", padx=2, pady=6)
        lblBookTittle.grid(row=1, column=2, sticky=W)
        txtBookTittle = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.booktittle, width=35)
        txtBookTittle.grid(row=1, column=3)

        lblAuthorName = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Author ", padx=2, pady=6)
        lblAuthorName.grid(row=2, column=2, sticky=W)
        txtAuthorName = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.author, width=35)
        txtAuthorName.grid(row=2, column=3)

        lblDateOfBorrowed = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Date Borrowed ", padx=2, pady=6)
        lblDateOfBorrowed.grid(row=3, column=2, sticky=W)
        txtDateOfBorrowed = Entry(
            DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dateborrowed, width=35)
        txtDateOfBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=(
            "arial", 12, "bold"),text="Date Due ", padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.datedue, width=35)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Days On Book ", padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.daysonbook, width=35)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Late Return Fine", padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(
            DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.latefine, width=35)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, font=(
            "arial", 12, "bold"),text="Date Over Due ", padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.dateoverdue, width=35)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Actual Price ", padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"),textvariable=self.finalprice, width=35)
        txtActualPrice.grid(row=8, column=3)
        
        

        # =================Data Frame Right===========================
        
        

        self.txtBox = Text(DataFrameRight, font=("arial",13,"bold"), width=32, height=16)
        self.txtBox.grid(row=0, column=2,padx=2)
        
        listScrollBar = Scrollbar(DataFrameRight)    
        listScrollBar.grid(row=0,column=1,sticky="ns")

        listBooks = ["Web Development", "Python", "Machine Learning", "Deep Learning", 
                    "Ethical Hacking", "Java", "C/C++", "JavaScript",
                    "The Richest Engineer","Software Engineering","Python Advance",
                    "Statics","Let's Code","Crack Code","The Adavnce Machine Learning",
            "Artificial Intelligence","Big Data","Probability","Data Science","HTML","CSS","The Ghost"]
        
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.dateborrowed.set(d1)
            self.datedue.set(d3)
            self.daysonbook.set(15)
            self.latefine.set(50)
            self.dateoverdue.set("NO")
            
            if (x=="Web Development"):
                self.bookid.set(1123)
                self.booktittle.set("Make Web")
                self.author.set("James")
                self.finalprice.set(890)
                
                
                
            elif (x=="Python"):
                self.bookid.set(1124)
                self.booktittle.set("To build an AI")
                self.author.set("Andy Smith")
                self.finalprice.set(670)
                
                
                
            elif (x=="Machine Learning"):
                self.bookid.set(1125)
                self.booktittle.set("Human and Machine")
                self.author.set("JJ Thomson")
                self.finalprice.set(550)
                
            elif (x=="Deep Learning"):
                self.bookid.set(1126)
                self.booktittle.set("To build an AI")
                self.author.set("Kris Starlet")
                self.finalprice.set(400)
                
            elif (x=="Ethical Hacking"):
                self.bookid.set(1127)
                self.booktittle.set("Hack the Code")
                self.author.set("Downey A")
                self.finalprice.set(720)
                
            elif (x=="Java"):
                self.bookid.set(11281)
                self.booktittle.set("Java Core")
                self.author.set("Mathew")
                self.finalprice.set(989)
                
            elif (x=="C/C++"):
                self.bookid.set(11249)
                self.booktittle.set("Basic Computer Language")
                self.author.set("MK Jordan")
                self.finalprice.set(1050)
                
            elif (x=="JavaScript"):
                self.bookid.set(42347)
                self.booktittle.set("Java Script")
                self.author.set("ST Clerk")
                self.finalprice.set(1670)
                
            elif (x=="The Richest Engineer"):
                self.bookid.set(85846)
                self.booktittle.set("To become a rich coder")
                self.author.set("Albert Rey")
                self.finalprice.set(850)
                
            elif (x=="Software Engineering"):
                self.bookid.set(93646)
                self.booktittle.set("System Software ")
                self.author.set("Frankin Steve")
                self.finalprice.set(2340)
                
            elif (x=="Python Advance"):
                self.bookid.set(65837)
                self.booktittle.set("Python Programming")
                self.author.set("Ronny Bitz")
                self.finalprice.set(170)
                
            elif (x=="Statics"):
                self.bookid.set(47576)
                self.booktittle.set("Statics")
                self.author.set("Sweezy Smith")
                self.finalprice.set(600)
                
            elif (x=="Let's Code"):
                self.bookid.set(38723)
                self.booktittle.set("Solve the code")
                self.author.set("Deniel Paul")
                self.finalprice.set(730)
                
            elif (x=="Crack Code"):
                self.bookid.set(67473)
                self.booktittle.set("Learn Coding easily")
                self.author.set("Caten George")
                self.finalprice.set(1240)
                
            elif (x=="The Adavnce Machine Learning"):
                self.bookid.set(12378)
                self.booktittle.set("Machine Learning")
                self.author.set("Robert Alex")
                self.finalprice.set(1770)
                
            elif (x=="Airtificial Intelligence"):
                self.bookid.set(19723)
                self.booktittle.set("How to make human robot")
                self.author.set("Andrew Paul")
                self.finalprice.set(610)
                
            elif (x=="Big Data"):
                self.bookid.set(23789)
                self.booktittle.set("Large Data")
                self.author.set("Rushkin Bond")
                self.finalprice.set(2149)
                
            elif (x=="Probability"):
                self.bookid.set(65789)
                self.booktittle.set("advance maths")
                self.author.set("Preeti Shenoy")
                self.finalprice.set(950)
                
            elif (x=="Data Science"):
                self.bookid.set(45856)
                self.booktittle.set("To Grow Business")
                self.author.set("Shasi Tharoor")
                self.finalprice.set(2550)
                
            elif (x=="HTML"):
                self.bookid.set(86342)
                self.booktittle.set("Structure of web")
                self.author.set("Roger Faligot")
                self.finalprice.set(640)
                
            elif (x=="CSS"):
                self.bookid.set(16487)
                self.booktittle.set("Beauty of Website")
                self.author.set("Usha Uthup")
                self.finalprice.set(570)
                
            else:
                self.bookid.set(364087)
                self.booktittle.set("The Ghost")
                self.author.set("Richa Misra")
                self.finalprice.set(780)
                    
        
           
        listBox =Listbox(DataFrameRight,font=("arial" ,12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook) 
        listBox.grid(row=0,column=0,padx=2)
        
        listScrollBar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        

        # =================Buttons===========================

        btnAddData = Button(ButtonFrame,command=self.Add_data, text="Add Data", bg="Blue", fg="white", font=(
            "arial", 13, "bold"), width=23, padx=2, pady=6)
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(ButtonFrame,command=self.show_data, text="Show Data", bg="blue", fg="white", font=(
            "arial", 13, "bold"), width=23, padx=2, pady=6)
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(ButtonFrame,command=self.update, text="Update", bg="blue", fg="white", font=(
            "arial", 13, "bold"), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(ButtonFrame,command=self.delete, text="Delete", bg="blue", fg="white", font=(
            "arial", 13, "bold"), width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(ButtonFrame, command=self.clear, text="Clear", bg="blue", fg="white", font=(
            "arial", 13, "bold"), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(ButtonFrame,command=self.exit, text="Exit", bg="blue", fg="white", font=(
            "arial", 13, "bold"), width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)
        
        
        
        #======================Table of Information Frame===================
        #======================scrollbar===============
        
        Table_frame= Frame(DetailsFrame,bd=6, relief= RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=2,width=1470,height=150)
        
        

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table = ttk.Treeview(Table_frame,column=("membertype","prn","idno","firstname","lastname",
                                           "adress1","adress2","postcode","mobile","bookid","booktittle","author","dateborrowed",
                                           "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member ")
        self.library_table.heading("prn",text="Reg Number")
        self.library_table.heading("idno",text="Id Number")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Adress1")
        self.library_table.heading("adress2",text="Adress2")
        self.library_table.heading("postcode",text="Post Code")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktittle",text="Book Tittle")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Actual Price") 

        self.library_table["show"]="headings"

        self.library_table.column("membertype",width=100)
        self.library_table.column("prn",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postcode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktittle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100) 

        self.library_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
    
    def Add_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            
                                                                                                             self.member.get(),
                                                                                                             self.prn.get(),
                                                                                                             self.id.get(),
                                                                                                             self.firstname.get(),
                                                                                                             self.lastname.get(),
                                                                                                             self.adress1.get(),
                                                                                                             self.adress2.get(),
                                                                                                             self.postcode.get(),
                                                                                                             self.mobile.get(),
                                                                                                             self.bookid.get(),
                                                                                                             self.booktittle.get(),
                                                                                                             self.author.get(),
                                                                                                             self.dateborrowed.get(),
                                                                                                             self.datedue.get(),
                                                                                                             self.daysonbook.get(),
                                                                                                             self.latefine.get(),
                                                                                                             self.dateoverdue.get(),
                                                                                                             self.finalprice.get() 
                                                                                                               ))
        
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member has been inserted successfully")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)

                conn.commit()
            conn.close()
            
    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row=content["values"]

        self.member.set(row[0]),
        self.prn.set(row[1]),
        self.id.set(row[2]),
            
        self.firstname.set(row[3]),
        self.lastname.set(row[4]),
        self.adress1.set(row[5]),
        self.adress2.set(row[6]),
        self.postcode.set(row[7]),
        self.mobile.set(row[8]),
        self.bookid.set(row[9]),
        self.booktittle.set(row[10]),
        self.author.set(row[11]),
        self.dateborrowed.set(row[12]),
        self.datedue.set(row[13]),
        self.daysonbook.set(row[14]),
        self.latefine.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])
        
    def show_data(self):
        self.txtBox.insert(END,"Member\t\t " + self.member.get() + "\n")
        self.txtBox.insert(END,"Reg Number\t\t " + self.prn.get() + "\n")
        self.txtBox.insert(END,"Id Number\t\t " + self.id.get() + "\n")
        self.txtBox.insert(END,"First Name\t\t " + self.firstname.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t " + self.lastname.get() + "\n")
        self.txtBox.insert(END,"Adress1\t\t " + self.adress1.get() + "\n")
        self.txtBox.insert(END,"Adress2\t\t " + self.adress2.get() + "\n")
        self.txtBox.insert(END,"Post Code\t\t " + self.postcode.get() + "\n")
        self.txtBox.insert(END,"Moblie\t\t " + self.mobile.get() + "\n")
        self.txtBox.insert(END,"Book Id\t\t " + self.bookid.get() + "\n")
        self.txtBox.insert(END,"Book Tittle\t\t " + self.booktittle.get() + "\n")
        self.txtBox.insert(END,"Author\t\t " + self.author.get() + "\n")
        self.txtBox.insert(END,"Date of Borrowed\t\t " + self.dateborrowed.get() + "\n")
        self.txtBox.insert(END,"Date Due\t\t " + self.datedue.get() + "\n")
        self.txtBox.insert(END,"Days on Book\t\t " + self.daysonbook.get() + "\n")
        self.txtBox.insert(END,"Late Return Fine\t\t " + self.latefine.get() + "\n")
        self.txtBox.insert(END,"Date Over Due\t\t " + self.dateoverdue.get() + "\n")
        self.txtBox.insert(END,"Actual Price\t\t " + self.finalprice.get() + "\n")
        
        
    def clear(self):
        self.member.set(""),
        self.prn.set(""),
        self.id.set(""),
        self.firstname.set(""),
        self.lastname.set(""),
        self.adress1.set(""),
        self.adress2.set(""),
        self.postcode.set(""),
        self.mobile.set(""),
        self.bookid.set(""),
        self.booktittle.set(""),
        self.author.set(""),
        self.dateborrowed.set(""),
        self.datedue.set(""),
        self.daysonbook.set(""),
        self.latefine.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set("") 
        
        self.txtBox.delete("1.0",END)
        
    def delete(self):
        if self.prn.get()=="" or self.id.get()=="":
            messagebox.showerror("Error","Select the member")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="librarydata")
            my_cursor=conn.cursor()
            query="DELETE FROM library WHERE ID= %d"
            value=(self.prn.get())
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            
            messagebox.showinfo("Success","Member has been deleted")
            
    
    def update(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE library SET Member=%s, ID =%d,FirstName=%s,LAstName=%s,Adress1=%s,Adress2=%s,PostCode=%d,Mobile=%d,Book_Id=%d,Book_Tittle=%s,Author=%s,Date_Borrowed=%s,Date_Due=%s,Days_On_Book=%d,Late_Return_fee=%f,DateOverDue=%s,Final_Price=%f WHERE PRN_No=%d"(
                                                                            self.member.get(),
                                                                            self.id.get(),
                                                                            self.firstname.get(),
                                                                            self.lastname.get(),
                                                                            self.adress1.get(),
                                                                            self.adress2.get(),
                                                                            self.postcode.get(),
                                                                            self.mobile.get(),
                                                                            self.bookid.get(),
                                                                            self.booktittle.get(),
                                                                            self.author.get(),
                                                                            self.dateborrowed.get(),
                                                                            self.datedue.get(),
                                                                            self.daysonbook.get(),
                                                                            self.latefine.get(),
                                                                            self.dateoverdue.get(),
                                                                            self.finalprice.get(),
                                                                            self.prn.get()
                                                                               ))
        
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

        messagebox.showinfo("Success", "Data has been updated successfully")
    
    def exit(self):
        res=messagebox.askquestion('Exit Application', 'Do you really want to exit')
        if res == 'yes' :
            root.destroy()
        else :
            messagebox.showinfo('Return', 'Returning to main application')





if __name__ == "__main__":
    root = Tk()
    obj = LibraryMangementSystem(root)
    root.mainloop()


    