from tkinter import*
class calculator:
    def __init__(self,root):
        self.root=root
        root.title("calculator")
        root.geometry("400x600")
        root.config(bg="red")
        frame=Frame(bg="black",width=350,height=550)
        frame.place(x=25,y=30)

        def show(value):
            equation = entry.get() + value
            entry.delete(0, END)
            entry.insert(0, equation)

        def clear():
            entry.delete(0, END)

        def evaluate():
                exp = entry.get()
                res = eval(exp)
                entry.delete(0, END)
                entry.insert(0, res)



        addbut=Button(frame,text="+",font=("arial",15,"bold"),bd=10,command=lambda:show("+"),width=5,height=0)
        addbut.place(x=250,y=240)
        subbut = Button(frame, text="-",font=("arial",15,"bold"), bd=10, command=lambda:show("-"), width=5, height=0)
        subbut.place(x=250, y=300)
        mulbut = Button(frame, text="*", font=("arial", 15,"bold"), bd=10, command=lambda:show("*"), width=5, height=0)
        mulbut.place(x=250, y=360)
        divbut = Button(frame, text="/", font=("arial", 15,"bold"), bd=10, command=lambda:show("/"), width=5, height=0)
        divbut.place(x=250, y=420)
        eqbut = Button(frame, text="=", font=("arial", 15, "bold"), bd=10, command=evaluate, width=5, height=0)
        eqbut.place(x=250, y=480)
        clear = Button(frame, text="C", font=("arial", 15, "bold"), bd=10, command=clear, width=3, height=0)
        clear.place(x=10, y=240)
        seven = Button(frame, text="7", font=("arial", 15, "bold"), bd=10,  width=3, height=0,command=lambda:show("7"))
        seven.place(x=10, y=300)
        four = Button(frame, text="4", font=("arial", 15, "bold"), bd=10,  width=3, height=0,command=lambda:show("4"))
        four.place(x=10, y=360)
        one = Button(frame, text="1", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("1"))
        one.place(x=10, y=420)
        zerozero = Button(frame, text="00", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("00"))
        zerozero.place(x=10, y=480)
        modulo = Button(frame, text="%", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("%"))
        modulo.place(x=80, y=240)
        eight = Button(frame, text="8", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("8"))
        eight.place(x=80, y=300)
        five = Button(frame, text="5", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("5"))
        five.place(x=80, y=360)
        two = Button(frame, text="2", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("2"))
        two.place(x=80, y=420)
        zero = Button(frame, text="0", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("0"))
        zero.place(x=80, y=480)
        nine = Button(frame, text="9", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("9"))
        nine.place(x=150, y=300)
        six = Button(frame, text="6", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("6"))
        six.place(x=150, y=360)
        three = Button(frame, text="3", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("3"))
        three.place(x=150, y=420)
        dot= Button(frame, text=".", font=("arial", 15, "bold"), bd=10, width=3, height=0,command=lambda:show("."))
        dot.place(x=150, y=480)
        ans = Frame(frame, bd=10, width=350, height=215)
        ans.place(x=0, y=10)
        entry = Entry(frame, width=30,font=("arial",30))
        entry.place(x=90,y=150)

if __name__=="__main__":
    root=Tk()
    project=calculator(root)
    root.mainloop()


