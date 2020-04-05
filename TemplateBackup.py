import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from random import randint
import pandas as pd

LARGE_FONT= ("Verdana", 12)
#-----Light theam--------#
background_color , foreground_color = '#ffffff' , '#232324' 
#-----dark theam--------#
# background_color, foreground_color = '#3b3a3a' , '#ffffff'
random_no = randint(1000000000,9000000000)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit) # Press <ESC> to exit
        # self.overrideredirect(1)
        self.geometry("%dx%d+0+0"%(self.width,self.height))
        self.title("Visual Studio Code 2020")
        self.iconbitmap('app_icon.ico')

        #-------------------Menu---------------------------------#
        menu = Menu(self)
        self.config(menu=menu)  
        filemenu = Menu(menu) 
        menu.add_cascade(label='File', menu=filemenu) 
        filemenu.add_command(label='New') 
        filemenu.config(bg=background_color, fg=foreground_color)
        filemenu.add_command(label='Home Page', command=lambda: self.show_frame(HomePage)) 
        filemenu.add_command(label='One Page', command=lambda: self.show_frame(PageOne)) 
        filemenu.add_command(label='Two Page', command=lambda: self.show_frame(PageTwo)) 
        filemenu.add_command(label='Open...') 
        filemenu.add_separator() 
        filemenu.add_command(label='Exit', command=self.quit) 
        
        helpmenu = Menu(menu)
        helpmenu.config(bg=background_color, fg=foreground_color)
        menu.add_cascade(label='Help', menu=helpmenu) 
        helpmenu.add_command(label='About') 

        settingsmenu = Menu(menu) 
        settingsmenu.config(bg=background_color, fg=foreground_color)
        menu.add_cascade(label='Settings', menu=settingsmenu) 
        settingsmenu.add_command(label='Theams') 
        #-------------------End Menu-----------------------------#

        container.pack(side="top", fill="both", expand = True)
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

#--------------------------------- Start HomePage ----------------------------------------#
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit) # Press <ESC> to exit

        app_body = Frame(self, bd=0, relief=GROOVE, bg=background_color, padx=10, pady=10)
        app_body.place(x=0, y=0, width=self.width, height=self.width)
        
        label = tk.Label(app_body, bg=background_color, fg=foreground_color, text="Home Page!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
                
#--------------------------------- End HomePage ----------------------------------------#

#--------------------------------- Start Page One ----------------------------------------#
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit) # Press <ESC> to exit

        app_body = Frame(self, bd=0, relief=GROOVE, bg=background_color, padx=10, pady=10)
        app_body.place(x=0, y=0, width=self.width, height=self.width)
        
        label = tk.Label(app_body, bg=background_color, fg=foreground_color, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)        
#--------------------------------- End Page One ----------------------------------------#


#--------------------------------- Start Page Two ----------------------------------------#
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bind("<Escape>", exit) # Press <ESC> to exit

        app_body = Frame(self, bd=0, relief=GROOVE, bg=background_color, padx=10, pady=10)
        app_body.place(x=0, y=0, width=self.width, height=self.width)
        
        label = tk.Label(app_body, bg=background_color, fg=foreground_color, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
#--------------------------------- End Page Two ----------------------------------------#

app = SeaofBTCapp()
app.mainloop()
