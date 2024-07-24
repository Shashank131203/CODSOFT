import tkinter
from tkinter import *

calci = Tk()
calci.title("Calculator")
calci.geometry("570x600+100+200")
calci.resizable(False,False)
calci.configure(bg="#464849")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

label_result = Label(calci,width=25,height=2,text="",font=("Helvetica",30))
label_result.pack()

Button(calci,text="C",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(calci,text="/",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("/")).place(x=150,y=100)
Button(calci,text="%",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("%")).place(x=290,y=100)
Button(calci,text="*",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("*")).place(x=430,y=100)

Button(calci,text="7",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("7")).place(x=10,y=200)
Button(calci,text="8",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("8")).place(x=150,y=200)
Button(calci,text="9",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("9")).place(x=290,y=200)
Button(calci,text="-",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("-")).place(x=430,y=200)

Button(calci,text="4",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("4")).place(x=10,y=300)
Button(calci,text="5",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("5")).place(x=150,y=300)
Button(calci,text="6",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("6")).place(x=290,y=300)
Button(calci,text="+",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("+")).place(x=430,y=300)

Button(calci,text="1",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("1")).place(x=10,y=400)
Button(calci,text="2",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("2")).place(x=150,y=400)
Button(calci,text="3",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("3")).place(x=290,y=400)
Button(calci,text="0",width=11,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show("0")).place(x=10,y=500)

Button(calci,text=".",width=5,height=1,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#0A0A0A",command=lambda:show(".")).place(x=290,y=500)
Button(calci,text="=",width=5,height=3,font=("Helvetica",30,"bold"), bd=1,fg="#fff",bg="#FA6A06",command=lambda:calculate()).place(x=430,y=400)


calci.mainloop()