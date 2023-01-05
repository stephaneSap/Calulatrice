from tkinter import *
import math
import tkinter.messagebox


root = Tk()
root.title("Calculatrice scientifique")
root.configure(background="powder blue")
root.geometry("480x390+0+0")
root.resizable(width=False, height=False)

calculator = Frame(root)
calculator.grid()
#----entre des information---
txtDisplay = Entry(calculator, font=( "arial", 10, "bold"), bg="powder blue", bd=30, width=60, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#---la logique---
class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.oper = ""
        self.result = False
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum ==".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()

        else:
            self.total = float(txtDisplay.get())
    def valid_function(self):
        if self.oper == "add":
             self.total += self.current
        if self.oper == "sub":
             self.total -= self.current
        if self.oper == "mul":
             self.total *= self.current
        if self.oper == "div":
             self.total /= self.current
        if self.oper == "mod":
             self.total %= self.current

        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operator(self, oper):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
            self.check_sum = True
            self.oper = oper
            self.result = False
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
added_value = Calculator()

#-----buttons----
numberstd = "789456123"
btn = []
i = 0
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calculator, width=5, height=2, font=("arial", 10, "bold"), bd=4, text=numberstd[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = numberstd[i]: added_value.numberEnter(x)
        i+=1

btnClear = Button(calculator, text=chr(67), width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=0, pady=1)
btnAllclear = Button(calculator, text=chr(67)+chr(69), width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=1, pady=1)
btnsq = Button(calculator, text=chr(8730), width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=2, pady=1)
btnAdd = Button(calculator, text="+", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command=lambda: added_value.operator("add")).grid(row=1, column=3, pady=1)
btnSub = Button(calculator, text="-", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command=lambda: added_value.operator("sub")).grid(row=2, column=3, pady=1)
btnMul = Button(calculator, text="*", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command=lambda: added_value.operator("mul")).grid(row=3, column=3, pady=1)
btnDiv = Button(calculator, text=chr(247), width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command=lambda: added_value.operator("div")).grid(row=4, column=3, pady=1)

btnZero = Button(calculator, text="0", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command= lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
btnPoint = Button(calculator, text=".", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command= lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
btnPM = Button(calculator, text=chr(177), width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=5, column=2, pady=1)
btnEqual = Button(calculator, text="=", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue", command = added_value.sum_of_total).grid(row=5, column=3, pady=1)
 #----scientifique-----
btnpi = Button(calculator, text="π", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=4, pady=1)
btnCos = Button(calculator, text="Cos", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=5, pady=1)
btnSin = Button(calculator, text="Sin", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=6, pady=1)
btnTan = Button(calculator, text="Tan ", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=1, column=7, pady=1)

#-- prochain row

btn2pi = Button(calculator, text="2π", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=2, column=4, pady=1)
btnCoh = Button(calculator, text="Coh", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=2, column=5, pady=1)
btnSinh = Button(calculator, text="Sinh", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=2, column=6, pady=1)
btnTanh = Button(calculator, text="Tanh", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=2 , column=7,pady=1)


# ---- next row
btnlog = Button(calculator, text="log", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=3, column=4, pady=1)
btnExp = Button(calculator, text="exp", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=3, column=5, pady=1)
btnMod = Button(calculator, text="%", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=3, column=6, pady=1)
btnE= Button(calculator, text="e", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=3, column=7, pady=1)

#---next row
btnlog2 = Button(calculator, text="log2", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=4, column=4, pady=1)
btnDeg = Button(calculator, text="deg", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=4, column=5, pady=1)
btnaCosh= Button(calculator, text="aCosh", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=4, column=6, pady=1)
btnaSinh = Button(calculator, text="aSinh", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=4, column=7, pady=1)

#----next row---
btnLn = Button(calculator, text="ln", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=5, column=4, pady=1)
btnlog10 = Button(calculator, text="π", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=5, column=5, pady=1)
btnExpm1 = Button(calculator, text="1/x", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=5, column=6, pady=1)
btnGamma = Button(calculator, text="lgamma", width=5, height=2, font=("arial", 10, "bold"), bd=4, bg="powder blue").grid(row=5, column=7, pady=1)


TextDisplay = Label(calculator, text="calculatrice scientifique", font=("arial", 20, "bold"), justify=CENTER)
TextDisplay.grid(row=0, column=4, columnspan=4)
#------menu---

def quit():
    quit =  tkinter.messagebox.askyesno("calculatrice scientifique", "etez vous pret a quitter?")
    if quit > 0:
        root.destroy()
        return

def scientifique() :
    root.geometry("940x400+0+0")
    root.resizable(width=False, height=False)

def standard():
    root.geometry("480x560+0+0")
    root.resizable(width=False, height=False)

menubar = Menu(calculator)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Fichier", menu=filemenu)
filemenu.add_command(label="standard", command=standard)
filemenu.add_command(label="scientifique", command=scientifique)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=quit)

editmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Editer", menu=editmenu)
editmenu.add_command(label="Couper")
editmenu.add_command(label="copier")
editmenu.add_separator()
editmenu.add_command(label="Coller")
root.config(menu=menubar)
root.mainloop()