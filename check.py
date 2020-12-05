
from tkinter import* 
from PIL import Image,ImageTk 
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename 
import tkinter as tk 

root = Tk() # Create main tkinter window
root.title("image edit")
root.geometry('1000x600+500+100')
root.resizable(False,False)


Tk().withdraw()
filepath = askopenfilename()
img = Image.open(filepath)
tk_im = ImageTk.PhotoImage(img)


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)


xi=img.size[0]
yi=img.size[1]
wi=img.size[0]
hi=img.size[1]


def grow():
    global img
    global my_label
    global xi
    global yi
    global wi 
    global hi 
    i=0
    while i<2:
        resized_img = img.resize((xi, yi),resample=Image.NEAREST)
        tk_im=ImageTk.PhotoImage(resized_img)
        my_label.configure(width=wi,height=hi,image=tk_im)
        my_label.image=tk_im
        xi+=1
        yi+=1
        i+=1 
        wi+=1
        hi+=1
   

def shrink():
    global my_label
    global img
    global xi
    global yi
    global wi 
    global hi 
    i=0
    while i<2:
        resized_img = img.resize((xi, yi),resample=Image.NEAREST)
        tk_im=ImageTk.PhotoImage(resized_img)
        my_label.configure(width=wi,height=hi,image=tk_im)
        my_label.image=tk_im
        xi-=1
        yi-=1
        i+=1 
        wi-=1
        hi-=1



my_label=Label(root,image=tk_im)  
my_label.image=tk_im
my_label.pack()



grow_button=Button(root,text="grow",command=grow)
grow_button.pack()

shrink_button=Button(root,text="shrink",command=shrink)
shrink_button.pack()
        
my_label.bind("<Button-1>",drag_start)
my_label.bind('<B1-Motion>',drag_motion)

grow_button.bind("<Button-1>",drag_start)
grow_button.bind('<B1-Motion>',drag_motion)

shrink_button.bind("<Button-1>",drag_start)
shrink_button.bind('<B1-Motion>',drag_motion)

root.mainloop() 
