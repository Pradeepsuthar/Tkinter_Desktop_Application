import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from random import randint
import pandas as pd
from datetime import date
from dbConfig import *

# ----------- Global variables --------------------------------------#
LARGE_FONT = ("Verdana", 12)
#-----Light theam--------#
background_color, foreground_color = '#ffffff', '#232324'
#-----dark theam--------#
# background_color, foreground_color = '#3b3a3a' , '#ffffff'
random_no = randint(1000000000, 9000000000)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit)  # Press <ESC> to exit
        # self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.width, self.height))
        self.title("Visual Studio Code 2020")
        self.iconbitmap('app_icon.ico')

        # ----------------- Variables -----------------------------#
        today = date.today()
        self.FinancialYear_date_var = StringVar()
        FinancialYear_date = today.strftime("%d-%m-%Y")
        self.FinancialYear_date_var.set(FinancialYear_date)
        
        self.booking_date_var = StringVar()
        Booking_date = today.strftime("%d-%m-%Y")
        self.booking_date_var.set(Booking_date)

        self.CompanyName = StringVar()
        self.CompanyAddress = StringVar() 
        self.pincode = StringVar()
        self.CompanyPhoneNo = StringVar()
        self.OwnerMobileNo = StringVar()
        self.faxNo = StringVar()
        self.OwnerEmail = StringVar()
        self.websiteLink = StringVar()

        #-------------------Menu---------------------------------#
        menu = Menu(self)
        self.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.config(bg=background_color, fg=foreground_color)
        filemenu.add_command(
            label='Home Page', command=lambda: self.show_frame(HomePage))
        filemenu.add_command(
            label='One Page', command=lambda: self.show_frame(PageOne))
        filemenu.add_command(
            label='Two Page', command=lambda: self.show_frame(PageTwo))
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.quit)

        featuresmenu = Menu(menu)
        featuresmenu.config(bg=background_color, fg=foreground_color)
        menu.add_cascade(label='All Features', menu=featuresmenu)
        featuresmenu.add_command(label='Create Company', command=self.createCompany)

        helpmenu = Menu(menu)
        helpmenu.config(bg=background_color, fg=foreground_color)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')

        settingsmenu = Menu(menu)
        settingsmenu.config(bg=background_color, fg=foreground_color)
        menu.add_cascade(label='Settings', menu=settingsmenu)
        settingsmenu.add_command(label='Light Theams')
        #-------------------End Menu-----------------------------#

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    def createCompany(self):
        self.window = Toplevel(self)
        self.window.title('Company Creation')
        self.window.geometry("1000x500+200+100")  
        self.window.config(bg=background_color)
        self.window.iconbitmap('app_icon.ico')
        self.window.resizable(0,0)
       
        #---- Create company form----------#
        # ----------------- Main Frame ------------------------------- #
        win = Frame(self.window, bd=0, relief=GROOVE, bg=background_color, padx=0, pady=10)
        win.place(x=0, y=0, width=1000, height=500) 

        # ------------------------ LabelFrames -------------------------------- #
        Label_Frame1 = LabelFrame(win, text="Primary Mailing Details", font=('Verdana',10,'bold'), fg=foreground_color, bg=background_color, padx=20, pady=20, bd=0, relief=SUNKEN)
        Label_Frame1.place(x=20, y=0, relwidth=1)

        Label_Frame2 = LabelFrame(win, text="Contact Details", font=('Verdana',10,'bold'), fg=foreground_color, bg=background_color, padx=20, pady=20, bd=0, relief=SUNKEN)
        Label_Frame2.place(x=20, y=200, relwidth=1)
        
        Label_Frame3 = LabelFrame(win, text="Books and Financial Year Details", font=('Verdana',10,'bold'), fg=foreground_color, bg=background_color, padx=20, pady=20, bd=0, relief=SUNKEN)
        Label_Frame3.place(x=500, y=0, relwidth=1)
        
        Label_Frame4 = LabelFrame(win, text="To Save the Details Click SAVE Button", font=('Verdana',10), fg=foreground_color, bg=background_color, padx=20, pady=0, bd=0, relief=SUNKEN)
        Label_Frame4.place(x=20, y=400, relwidth=1)

        # -----------------------------------------------------Labels ---------------------------------------------- #
        # ------------------------------ Labels on Label_Frame1 ----------------------------------#
        Label(Label_Frame1, text="Mailing  Name", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=0, sticky=W, padx=3, pady=2)
        Label(Label_Frame1, text="Address", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=1, sticky=W, padx=3, pady=2)
        Label(Label_Frame1, text="Country", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=2, sticky=W, padx=3, pady=2)
        Label(Label_Frame1, text="State", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=3, sticky=W, padx=3, pady=2)
        Label(Label_Frame1, text="Pincode", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=4, sticky=W, padx=3, pady=2)
        
         # ------------------------------ Labels on Label_Frame2 ----------------------------------#
        Label(Label_Frame2, text="Phone No.", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=0, sticky=W, padx=3, pady=2)
        Label(Label_Frame2, text="Mobile No.", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=1, sticky=W, padx=3, pady=2)
        Label(Label_Frame2, text="FAX No.", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=2, sticky=W, padx=3, pady=2)
        Label(Label_Frame2, text="E-mail Address", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=3, sticky=W, padx=3, pady=2)
        Label(Label_Frame2, text="Website", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=4, sticky=W, padx=3, pady=2)

         # ------------------------------ Labels on Label_Frame3 ----------------------------------#
        Label(Label_Frame3, text="Financial year begins from", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=0, sticky=W, padx=3, pady=2)
        Label(Label_Frame3, text="Book beginning from", bg=background_color, fg=foreground_color, font=('Verdana',10)).grid(row=1, sticky=W, padx=3, pady=2)

        # ----------------------------------------------------- Text Filed ---------------------------------------------- #
        # ------------------------------ Text Filed on Label_Frame1 ----------------------------------#
        CompanyName = Entry(Label_Frame1, width=40, textvariable=self.CompanyName, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=0, column=1, padx=2, pady=2)
        CompanyAddress = Entry(Label_Frame1, width=40, textvariable=self.CompanyAddress, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=1, column=1, padx=2, pady=2)
        Countries = ["India","USA","UK"]
        self.CountriesVar = StringVar(Label_Frame1)
        self.CountriesVar.set(Countries[0]) # default value
        OptionMenu(Label_Frame1, self.CountriesVar, *Countries).grid(row=2, column=1, sticky=W, padx=2, pady=2)
        States = ["Rajasthan","Dehli","Mumbai"]
        self.StatesVar = StringVar(Label_Frame1)
        self.StatesVar.set(States[0]) # default value
        OptionMenu(Label_Frame1, self.StatesVar, *States).grid(row=3, column=1, sticky=W, padx=2, pady=2)
        pincode = Entry(Label_Frame1, width=40, textvariable=self.pincode, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=4, column=1, padx=2, pady=2)
        
        # ------------------------------ Text Filed on Label_Frame2 ----------------------------------#
        CompanyPhoneNo = Entry(Label_Frame2, width=40, textvariable=self.CompanyPhoneNo, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=0, column=1, padx=2, pady=2)
        OwnerMobileNo = Entry(Label_Frame2, width=40, textvariable=self.OwnerMobileNo, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=1, column=1, padx=2, pady=2)
        faxNo = Entry(Label_Frame2, width=40, textvariable=self.faxNo, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=2, column=1, padx=2, pady=2)
        OwnerEmail = Entry(Label_Frame2, width=40, textvariable=self.OwnerEmail, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=3, column=1, padx=2, pady=2)
        websiteLink = Entry(Label_Frame2, width=40, textvariable=self.websiteLink, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10)).grid(row=4, column=1, padx=2, pady=2)

        # ------------------------------ Text Filed on Label_Frame3 ----------------------------------#
        Entry(Label_Frame3, width=30, textvariable=self.FinancialYear_date_var, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10), state='disabled').grid(row=0, column=1, padx=2, pady=2)
        Entry(Label_Frame3, width=30, textvariable=self.booking_date_var, bd=1, relief=SUNKEN, bg='gainsboro', font=('Verdana',10), state='disabled').grid(row=1, column=1, padx=2, pady=2)


        # ------------------------------ Buttons on Label_Frame4 ----------------------------------#
        Button(Label_Frame4, text="Save", width=15, bg=background_color, fg=foreground_color, bd=1, relief=GROOVE, command=self.saveCompany).grid(row=0, column=0, padx=2, pady=20)
        Button(Label_Frame4, text="Close", width=15, bg=background_color, fg=foreground_color, bd=1, relief=GROOVE, command=self.window.destroy).grid(row=0, column=1, padx=2, pady=20)

    def saveCompany(self):
        c_name = self.CompanyName.get()
        c_address = self.CompanyAddress.get()
        pincode = self.pincode.get()
        phone_no = self.CompanyPhoneNo.get()
        mobile_no = self.OwnerMobileNo.get()
        fx_no = self.faxNo.get()
        email = self.OwnerEmail.get()
        countory = self.CountriesVar.get()
        state = self.StatesVar.get()
        website_link = self.websiteLink.get()
        FinancialYear_date_var = self.FinancialYear_date_var.get()
        booking_date_var = self.booking_date_var.get()
        if  c_name != '' and c_address != '' and pincode != '' and phone_no != '' and mobile_no != '' and fx_no != '' and email != '' and countory != '' and state != '' and website_link != '' and FinancialYear_date_var != '' and booking_date_var != '':
            print("Comapny Name :",c_name)
            print("Comapny Address :",c_address)
            print("Comapny Pincode :",pincode)
            print("Comapny Phone :",phone_no)
            print("Comapny Mobile :",mobile_no)
            print("Comapny FAX No. :",fx_no)
            print("Comapny Email :",email)
            print("Comapny Website :",website_link)
            print("Comapny Countory :",countory)
            print("Comapny State :",state)
            print("Comapny FinancialYear_date_var :",FinancialYear_date_var)
            print("Comapny booking_date_var :",booking_date_var)
            print("Saved Company Data in Database")
            messagebox.showinfo("Successfull Insert","Record inserted.")
            self.window.destroy()
        else:
            messagebox.showinfo("Field Insert","Record not inserted.")
        
#--------------------------------- Start HomePage ----------------------------------------#
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit)  # Press <ESC> to exit

        app_body = Frame(self, bd=0, relief=GROOVE,
                         bg=background_color, padx=10, pady=10)
        app_body.place(x=0, y=0, width=self.width, height=self.width)

        label = tk.Label(app_body, bg=background_color,
                         fg=foreground_color, text="Home Page!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
#--------------------------------- End HomePage ----------------------------------------#

#--------------------------------- Start Page One ----------------------------------------#
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit)  # Press <ESC> to exit

        app_body = Frame(self, bd=0, relief=GROOVE,
                         bg=background_color, padx=10, pady=10)
        app_body.place(x=0, y=0, width=self.width, height=self.width)

        label = tk.Label(app_body, bg=background_color,
                         fg=foreground_color, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
#--------------------------------- End Page One ----------------------------------------#


#--------------------------------- Start Page Two ----------------------------------------#
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit)  # Press <ESC> to exit

        app_body = Frame(self, bd=0, relief=GROOVE,
                         bg=background_color, padx=10, pady=10)
        app_body.place(x=0, y=0, width=self.width, height=self.width)

        label = tk.Label(app_body, bg=background_color,
                         fg=foreground_color, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
#--------------------------------- End Page Two ----------------------------------------#


app = SeaofBTCapp()
app.mainloop()
