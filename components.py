# from tkinter import *
# class App:
#   def __init__(self, master):
#     frame = Frame(master)
#     frame.pack()
#     self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
#     self.button.pack(side=LEFT)
#     self.slogan = Button(frame, text="Hello", command=self.write_slogan)
#     self.slogan.pack(side=LEFT)

#   def write_slogan(self):
#     print ("Tkinter is easy to use!")

# root = Tk()
# app = App(root)
# root.mainloop()

# --------------------------------------------------------------------------------------------------------

# import tkinter as tk

# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)

# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()

# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()

# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------------------------------------------------------
# from sys import version_info
# if version_info.major == 2:
#     import Tkinter as tk
# elif version_info.major == 3:
#     import tkinter as tk

# from functools import partial


# app = tk.Tk()
# labelExample = tk.Button(app, text="0")

# def change_label_number(num):
#     counter = int(str(labelExample['text']))
#     counter += num
#     labelExample.config(text=str(counter))

# buttonExample = tk.Button(app, text="Increase", width=30,
#                           command=partial(change_label_number, 2))

# buttonExample.pack()
# labelExample.pack()
# app.mainloop()

# ------------------------------------------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.overrideredirect(1)
root.bind("<Escape>", exit)  # Press <ESC> to exit
root.geometry("500x500+100+100")
for r in range(10):
   for c in range(5):
      Label(root, text='Row%s / Column%s'%(r,c),bd=1, relief=GROOVE ).grid(row=r,column=c, padx=2, pady=2)
root.mainloop()