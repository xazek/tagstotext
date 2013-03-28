from Tkinter import *
from ttk import *
import string


app = Tk()
app.title("TagsToText")
app.geometry('900x600+200+200')
app.resizable(0, 0)

def action():
    print "action"
    
menubar = Menu(app)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=action)
filemenu.add_command(label="Save as XML", command=action)
filemenu.add_command(label="Save as PDF", command=action)
filemenu.add_command(label="Save as HTML", command=action)
filemenu.add_command(label="Open XML", command=action)
filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=action)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)


s = Scrollbar(app)
T = Text(app)

T.focus_set()
s.pack(side=LEFT, fill=Y)
T.pack(side=LEFT, fill=Y)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)

app.mainloop()
