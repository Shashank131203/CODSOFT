from tkinter import *
from tkinter import messagebox

# Functions
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", 'Please enter your task.')

def deleteTask():
    lb.delete(ANCHOR)

# Body
body = Tk()
body.geometry('500x500+500+200')
body.title('To-Do List')
body.config(bg='#C6B3EF')

# Frame
frame = Frame(body)
frame.pack(pady=20)

lb = Listbox(
    frame,
    width=30,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#040404',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    bg='#F1EAF1',
    activestyle='none'
)
lb.pack(side=LEFT, fill=BOTH)
lb.pack(padx=10,pady=10)

task_list = [
    "Drink Water",
    "Stretching",
    "Go to Gym",
    "Study",
    "Work on Internship",
    "Take a nap",
    "Play Outdoor Games"
]
for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side= RIGHT, fill= BOTH)

lb.config(yscrollcommand= sb.set)
sb.config(command=lb.yview)

my_entry=Entry(
    body,
    font=('times',24)
)
my_entry.pack(pady=20)

button_frame = Frame(body)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text="Add Task",
    font=('times 16'),
    bg='#6807FD',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text="Delete Task",
    font=('times 16'),
    bg='#6807FD',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


body.mainloop()