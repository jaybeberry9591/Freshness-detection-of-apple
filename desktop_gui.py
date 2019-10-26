import os
import tkinter
import tkinter.filedialog
import subprocess
import random
import time
from tkinter.font import Font
from tkinter import *
from tkinter import messagebox
import Object_detection_webcam_pattern as bots
from datetime import datetime
import shutil
import threading


top = Tk()

#root = tkinter.Tk()

C = Canvas(top, bg="#B2FF66", height=500, width=800)
filename = PhotoImage(file = "Ap.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

top.title("FRUIT'S FRESHNESS DETECTION")

def storage():
       tp = Toplevel()
       C = Canvas(tp, bg="pink", height=500, width=800)
       filename = PhotoImage(file="about.png")
       background_label = Label(tp, image=filename)
       background_label.place(x=0, y=0, relwidth=1, relheight=1)
       C.pack()
       tp.title("FRUIT'S FRESHNESS DETECTION")
       tp.resizable(width=False, height=False)
       b1 = Button(tp, text="Video1 of Existing System", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1, width=22,command=video1)
       b1_window = C.create_window(330, 155, anchor='nw', window=b1)
       b1.config(font=('helvetica', 15, 'bold italic'))
       b2 = Button(tp, text="Video2 of Existing System ", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1, width=22, command=video2)
       b2_window = C.create_window(330, 225, anchor='nw', window=b2)
       b2.config(font=('helvetica', 15, 'bold italic'))

       tp.mainloop()
def run():
    #(python Object_detection_webcam.py)
   # exec(open(r"C:\tensorflow1\models\research\object_detection\python Object_detection_webcam.py").read())
    # command="python Object_detection_webcam.py"
    # os.system(command)
    subprocess.call('python Object_detection_webcam_pattern.py', shell=True)
def set_environment():
   #exec(open(r"conda activate tensorflow1").read())
   # command = "conda activate tensorflow1"
   #os.system(command)
   subprocess.call('conda activate tensorflow1', shell=True)
def set_path1():
   # command="set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim"
   # os.system(command)
   subprocess.call('set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim', shell=True)
def set_path2():
    #command="set PATH=%PATH%;PYTHONPATH"
    #os.system(command)
    subprocess.call('set PATH=%PATH%;PYTHONPATH', shell=True)
def set_directoy():
    #command="cd C:/tensorflow1/models/research/object_detection"
    #os.system(command)
    subprocess.call('cd C:/tensorflow1/models/research/object_detection', shell=True)



def start():
    tp = Toplevel()
    C = Canvas(tp, bg="pink", height=500, width=800)
    filename = PhotoImage(file="about.png")
    background_label = Label(tp, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    tp.title("FRUIT'S FRESHNESS DETECTION")
    tp.resizable(width=False, height=False)
    b1 = Button(tp, text="SET ENVIRONMENT", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1, width=22, command=set_environment)
    b1_window = C.create_window(330, 115, anchor='nw', window=b1)
    b1.config(font=('helvetica', 15, 'bold italic'))
    b2 = Button(tp, text="SET PATH1", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1, width=22, command=set_path1)
    b2_window = C.create_window(330, 185, anchor='nw', window=b2)
    b2.config(font=('helvetica', 15, 'bold italic'))

    b3 = Button(tp, text="SET PATH2", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1,
                width=22, command=set_path2)
    b3_window = C.create_window(330, 255, anchor='nw', window=b3)
    b3.config(font=('helvetica', 15, 'bold italic'))

    b4 = Button(tp, text="SET DIRECTORY", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1,
                width=22, command=set_directoy)
    b4_window = C.create_window(330, 325, anchor='nw', window=b4)
    b4.config(font=('helvetica', 15, 'bold italic'))

    b5= Button(tp, text="RUN", bg="#ef7564", fg="#132519", anchor='w', relief=RAISED, height=1,
                width=22, command=run)
    b5_window = C.create_window(330, 395, anchor='nw', window=b5)
    b5.config(font=('helvetica', 15, 'bold italic'))
    tp.mainloop()


def settings():
       tp = Toplevel()
       C = Canvas(tp, bg="#93be89", height=500, width=800)
       filename = PhotoImage(file="Ap.png")
       background_label = Label(tp, image=filename)
       background_label.place(x=0, y=0, relwidth=1, relheight=1)
       C.pack()
       tp.title("FRUITS FRESHNESS DETECTION")
       tp.resizable(width=False, height=False)
       b1 = Button(tp, text="  ADD PHOTO", bg="#93be89", fg="#132519", anchor='w', relief=RAISED, height=1, width=15)
       b1_window = C.create_window(330, 115, anchor='nw', window=b1)
       b1.config(font=('helvetica', 15, 'bold'))

       b2 = Button(tp, text="REMOVE PHOTO", bg="#93be89", fg="#132519", anchor='w', relief=RAISED,
                height=1, width=15)
       b2_window = C.create_window(330, 185, anchor='nw', window=b2)
       b2.config(font=('helvetica', 15, 'bold italic'))




       tp.mainloop()


def close_window():
    top.destroy()


def new_window():
    tp = Toplevel()
    C = Canvas(tp, bg="pink", height=500, width=800)
    filename = PhotoImage(file="about.png")
    background_label = Label(tp, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    tp.title("FRUITS FRESHNESS DETECTION")
    tp.resizable(width=False, height=False)
    one = Label(tp, text="ABOUT", bg="#93be89", fg="white", anchor='w')
    one_window = C.create_window(0, 0, anchor='nw', window=one)
    one.config(font=("Bold", 20))
    tp.mainloop()

def start_submit_thread():
    global submit_thread
    submit_thread = threading.Thread(target=video1)
    submit_thread.daemon = True
    #progressbar.start()
    submit_thread.start()
    top.after(20, check_submit_thread)

def check_submit_thread():
    if submit_thread.is_alive():
        top.after(20, check_submit_thread)
    else:
        print('exited')
	
def video1():
    bots.temp()
def video2():
    os.system("E:\Gui\z2.mp4")
def open_window():
    tp=Toplevel()
    C = Canvas(tp, bg="pink", height=500, width=800)
    filename = PhotoImage(file="about.png")
    background_label = Label(tp, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    tp.title("FRUITS FRESHNESS DETECTION")
    tp.resizable(width=False, height=False)
    one = Label(tp, text="ABOUT", bg="#93be89", fg="white", anchor='w')
    one_window = C.create_window(0, 0, anchor='nw', window=one)
    one.config(font=("Bold", 20))



    S = Scrollbar(one)
    T = Text(one, height=300, width=400,bg="#ACBB78",fg="black")
    T.config(font=("Bold", 13))
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """
    Grading of fruits is performed primarily by visual inspec-tion using size as a particular quality  attribute.
    With aim to minimize human labor and increase the accuracy image processing is introduced.Image  processing 
    offers solution for automated  fruit  size  grading  to  provide  accurate,reliable, consistent and 
    quantitative information  apart from handling large volumes,which may not be achieved by employing 
    human graders.
    
    Fruit nondestructive detection is the process of detecting fruits inside and outside quality without any
    damage,us-ing some detecting technology to make evaluation accord-ing  some standard  rules.  Nowadays,the
    quality of  fruit shape,default,color and size and so on  can not evaluatedon line by the traditional 
    methods. With the development of  image  processing  technology  and  computer  software and hardware,
    it becomes more attractive to detect fruit quality by using vision detecting technology.
    
    At present,most existing  fruit quality  detecting  and  grading  system have  the  disadvantage  of  low 
    efficiency,low  speed  of grading, high cost and complexity. So it is significant to develop high speed
    and low cost fruit size detecting and grading system we  are  going to  sort  the  fruits  according to 
    freshness  and  quality  by  image  processing.The  entire system  is  designed over  Python  to  inspect
    the  color. """
    T.insert(END, quote)

   # center(tp)
    tp.mainloop()


one=Label(top,text="FRUITS FRESHNESS DETECTION",bg="#73a767",fg="#132519",anchor='w')
one_window=C.create_window(80,5,anchor='nw',window=one)
one.config(font=("Bold",30))


b1=Button(top,text="        START",bg="#93be89",fg="#132519",anchor='w', relief=RAISED, height =1, width =15, command=start_submit_thread)
b1_window=C.create_window(330,135,anchor='nw',window=b1)
b1.config(font=('helvetica',15, 'bold italic'))


b2=Button(top,text="       ABOUT",bg="#93be89",fg="#132519",anchor='w', relief=RAISED,command=open_window, height =1, width =15)
b2_window=C.create_window(330,205,anchor='nw',window=b2)
b2.config(font=('helvetica', 15, 'bold italic'))


b3=Button(top,text="     PREVIEW",bg="#93be89",fg="#132519",anchor='w', relief=RAISED, height =1, width =15,command=storage)
b3_window=C.create_window(330,275,anchor='nw',window=b3)
b3.config(font=('helvetica', 15, 'bold italic'))


#b4=Button(top,text="      SETTINGS",bg="#93be89",fg="#132519",anchor='w', relief=RAISED, height =1, width =15,command=settings)
#b4_window=C.create_window(330,355,anchor='nw',window=b4)
#b4.config(font=('helvetica', 15, 'bold italic'))


b5=Button(top,text="          EXIT",bg="#93be89",fg="#132519",anchor='w', relief=RAISED, height =1, width =15,command=close_window)
b5_window=C.create_window(330,345,anchor='nw',window=b5)
b5.config(font=('helvetica', 15, 'bold italic'))
top.mainloop()