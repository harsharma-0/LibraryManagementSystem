from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter



class LibraryManagementSystem:         #define class
    def __init__(self,root):           #constructor (root is windows name)
        self.root = root                #initialise self
        self.root.title("Library Management System")          #give a titlez
        self.root.geometry("1550x800+0+0")                  # size of the window
        
        # ============================================ Variable ===========================================================
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        
        
        lbltitle=Label(self.root, text = "LIBRARY MANAGEMENT SYSTEM", bg = "powder blue", fg="green", bd=20,relief= RIDGE,font=("times new roman", 50, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12, relief = RIDGE, padx=20, bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        
        # ======================================== Data Frame Left ========================================
        
        DataFrameLeft= LabelFrame(frame,text= "Library Membership Information", bg = "powder blue", fg="green", bd=12,relief= RIDGE,font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblmember=Label(DataFrameLeft,bg= "powder blue", text="Member Type",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)
        
        commember=ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),width=27,textvariable=self.member_var,state="readonly")
        commember["value"]=("Admin Staff","Student","Lecturer")
        commember.current(0)
        commember.grid(row=0,column=1)
        
        lblPNR_NO=Label(DataFrameLeft,bg= "powder blue", text="PRN NO.",font=("arial", 12, "bold"),padx=2,pady=6)
        lblPNR_NO.grid(row=1,column=0,sticky=W)
        txtPNR_NO=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.prn_var,width=29)
        txtPNR_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName", padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code",padx=2,pady=4,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
        
        lblDataBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDataBorrowed.grid(row=3,column=2,sticky=W)
        txtDataBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDataBorrowed.grid(row=3,column=3)
        
        lblDataDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDataDue.grid(row=4,column=2,sticky=W)
        txtDataDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDataDue.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDateOverDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="powder blue")
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)
        
        # ============================================= Data Frame Right ================================================
        
        DataFrameRight= LabelFrame(frame,text= "Book Details", bg = "powder blue", fg="green", bd=12,relief= RIDGE,font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("arial", 12, "bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky=NS)   #ns=north south
        
        # ======================================================== List of books =========================================================
        
        listBooks=['Head Firt Book', 'Learn Python The Hard Way', 'Python Programming', 'Secrete Rahshy', 'Python CookBook', 'Introduction To Machine Learning', 'Machine Tecno', 'My Python', 'Joss Ellif Guru', 'Elite Jungle Python', 'Jungli Python', 'Machine Python', 'Advanced Python', 'Inton Python', 'RedChilli Python', 'Ishq Python','Intro To Java Programming','Intro To Discrete Mathematics','Intro to CPP Programming', 'Learn CPP Programming', 'The Great Gatsby', 'To Kill a Mockingbird', 'Jane Eyre']
        
        # ================================================ Function to automatically fill the columns when you click on the book =======================================
        
        def SelectBook(event=""):
            value = str(listbox.get(listbox.curselection()))
            x = value
            if x == "Head Firt Book":
                self.bookid_var.set("HF235498")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 780")
                
            elif x == "Learn Python The Hard Way":
                self.bookid_var.set("GH39852")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 899")
                
            elif x == "Python Programming":
                self.bookid_var.set("FY326468")
                self.booktitle_var.set("Python")
                self.author_var.set("Paul Berry")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 950")
                
            elif x == "Secrete Rahshy":
                self.bookid_var.set("TH637482")
                self.booktitle_var.set("Novel")
                self.author_var.set("Tykon Methew")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 650")
                
            elif x == "Python CookBook":
                self.bookid_var.set("RF425489")
                self.booktitle_var.set("Python Book")
                self.author_var.set("Tykon Methew")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 750")
                
            elif x == "Introduction To Machine Learning":
                self.bookid_var.set("RF425489")
                self.booktitle_var.set("Python Book")
                self.author_var.set("Tykon Methew")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 750")

            elif x == "Machine Tecno":
                self.bookid_var.set("EF486439")
                self.booktitle_var.set("Machine Learning")
                self.author_var.set("Tykon Methew")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 599")
                
            elif x == "My Python":
                self.bookid_var.set("UH872365")
                self.booktitle_var.set("Python Learning")
                self.author_var.set("Jeff Methew")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 899")
                
            elif x == "Joss Ellif Guru":
                self.bookid_var.set("WG38752")
                self.booktitle_var.set("Novel")
                self.author_var.set("Jeff Chaos")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 589")
                
            elif x == "Elite Jungle Python":
                self.bookid_var.set("TH83209")
                self.booktitle_var.set("Python")
                self.author_var.set("Hao Chaos")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 799")
                
            elif x == "Jungli Python":
                self.bookid_var.set("ZS32765")
                self.booktitle_var.set("Python")
                self.author_var.set("Theon Hao")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 784")
                
            elif x == "Machine Python":
                self.bookid_var.set("AH26342")
                self.booktitle_var.set("Learn Python")
                self.author_var.set("Brian Peter")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 799")
                
            elif x == "Advanced Python":
                self.bookid_var.set("SF78362")
                self.booktitle_var.set("Python")
                self.author_var.set("Brian J Peter")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 999")
                
            elif x == "Inton Python":
                self.bookid_var.set("DH38469")
                self.booktitle_var.set("Python")
                self.author_var.set("William Shekspear")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 479")
                
            elif x == "RedChilli Python":
                self.bookid_var.set("WGS72864")
                self.booktitle_var.set("Python")
                self.author_var.set("William Shekspear 2")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 40")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 569")
                
            elif x == "Ishq Python":
                self.bookid_var.set("AD64874")
                self.booktitle_var.set("Python")
                self.author_var.set("William D Cok")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 70")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 869")
                
            elif x == "Intro To Java Programming":
                self.bookid_var.set("HJ732864")
                self.booktitle_var.set("JAVA Programming")
                self.author_var.set("Jeff De Cok")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 999")
                
            elif x == "Intro To Discrete Mathematics":
                self.bookid_var.set("RD382746")
                self.booktitle_var.set("Mathematics")
                self.author_var.set("Pearson")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 799")
                
            elif x == "Intro to CPP Programming":
                self.bookid_var.set("ER475398")
                self.booktitle_var.set("CPP Programming")
                self.author_var.set("Laylord")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 70")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 799")
                
            elif x == "Learn CPP Programming":
                self.bookid_var.set("TUH7788")
                self.booktitle_var.set("CPP Programming")
                self.author_var.set("Thomas")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 70")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 999")
                
            elif x == "The Great Gatsby":
                self.bookid_var.set("HG64392")
                self.booktitle_var.set("Novel")
                self.author_var.set("F. Scott Fitzgerald")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 350")
                
            elif x == "To Kill a Mockingbird":
                self.bookid_var.set("SD836592")
                self.booktitle_var.set("Novel")
                self.author_var.set("Harper Lee")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 299")
                
            elif x == "Jane Eyre":
                self.bookid_var.set("AD873652")
                self.booktitle_var.set("Novel")
                self.author_var.set("Charlotte Brontë")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 499")

                
        
        listbox = Listbox(DataFrameRight, font=("arial", 12, "bold"),width=20,height=16)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)
        
        for item in listBooks:
            listbox.insert(END,item)
        
        # ======================================== Buttons Frame =======================================================
        frame=Frame(self.root,bd=12, relief = RIDGE, padx=20, bg="powder blue")
        frame.place(x=0,y=530,width=1530,height=70)
        
        btnAddData=Button(frame ,command=self.add_data, text="Add Data", font=("arial", 12, "bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(frame , command=self.showData, text="Show Data", font=("arial", 12, "bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(frame , command=self.update, text="Update", font=("arial", 12, "bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(frame , command=self.delete, text="Delete", font=("arial", 12, "bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(frame , command=self.reset, text="Reset", font=("arial", 12, "bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(frame , command=self.iExit, text="Exit", font=("arial", 12, "bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        
        # ======================================== Information Frame =======================================================
        frameDetails=Frame(self.root,bd=12, relief = RIDGE, padx=20, bg="powder blue")
        frameDetails.place(x=0,y=590,width=1530,height=210)
        
        Table_frame=Frame(frameDetails,bd=6, relief = RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table= ttk.Treeview(Table_frame,column=("membertype","prnno","id","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("id", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100 )
        self.library_table.column("prnno",width=100 )
        self.library_table.column("id", width=100)
        self.library_table.column("firstname",width=100 )
        self.library_table.column("lastname",width=100 )
        self.library_table.column("address1",width=100 )
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle",width=100 )
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Harsh@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO library VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
        ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been added successfully.")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Harsh@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set membertype=%s,id=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,author=%s,dateborrowed=%s,datedue=%s,days=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where prnno=%s",(
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
        ))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Harsh@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
        
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No.:\t\t"+ self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No.:\t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No.:\t\t"+ self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due:\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Days On Book:\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"Date Over Due:\t\t"+ self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Final Price:\t\t"+ self.finalprice_var.get()+"\n")
        
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
        
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit ?")
        if iExit>0:
            self.root.destroy()
            return
        
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the Member.")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Harsh@123",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where prnno = %s"
            Value=(self.prn_var.get(),)
            my_cursor.execute(query,Value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member has been deleted.")
        

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()