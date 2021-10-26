from tkinter import *
from tkinter import ttk

def button_input(char): #input character into entry 
    entry.insert('end', char) 

def evaluate_expression(expression): #do math
    exp_str = expression.get()
    result = eval(exp_str)
    return entry.delete(0,'end'), entry.insert(0,result)

def del_entry(): #delete the last character in entry
    entry.delete(entry.index("end") - 1)
    
def clear_entry(): #clear entire entry 
    entry.delete(0,"end")

root = Tk()
root.title("Python.tk Calculator")
root.geometry("400x500")
root.configure(bg='lightgray')

#instancing user entry box, StringVar makes contents callable outside the widget. 
expression = StringVar(root)
entry = ttk.Entry(root, textvariable=expression, width=60)
entry.grid(columnspan=4, row=0, padx=5,pady=5) #grid has to be handled on a separate line, or else it will return NoneType. This edit was made in github online. 

#set of number input buttons, click support only. 
n1 = ttk.Button(root, text='1', command=lambda:button_input("1") ).grid(column=0,row=2,padx=5,pady=5)
n2 = ttk.Button(root, text='2', command=lambda:button_input("2") ).grid(column=1,row=2,padx=5,pady=5)
n3 = ttk.Button(root, text='3', command=lambda:button_input("3") ).grid(column=2,row=2,padx=5,pady=5)
n4 = ttk.Button(root, text='4', command=lambda:button_input("4") ).grid(column=0,row=3,padx=5,pady=5)
n5 = ttk.Button(root, text='5', command=lambda:button_input("5") ).grid(column=1,row=3,padx=5,pady=5)
n6 = ttk.Button(root, text='6', command=lambda:button_input("6") ).grid(column=2,row=3,padx=5,pady=5)
n7 = ttk.Button(root, text='7', command=lambda:button_input("7") ).grid(column=0,row=4,padx=5,pady=5)
n8 = ttk.Button(root, text='8', command=lambda:button_input("8") ).grid(column=1,row=4,padx=5,pady=5)
n9 = ttk.Button(root, text='9', command=lambda:button_input("9") ).grid(column=2,row=4,padx=5,pady=5)
n0 = ttk.Button(root, text='0', command=lambda:button_input("0") ).grid(column=1,row=5,padx=5,pady=5)

#set of operator buttons, click support only
plus = ttk.Button(root, text="+", command=lambda:button_input("+")).grid(column=0, row=1,padx=5,pady=5)
minus = ttk.Button(root, text="-", command=lambda:button_input("-")).grid(column=1, row=1,padx=5,pady=5)
multiply = ttk.Button(root, text="x", command=lambda:button_input("*")).grid(column=2, row=1,padx=5,pady=5)
divide = ttk.Button(root, text="%", command=lambda:button_input("/")).grid(column=3, row=1,padx=5,pady=5)
decimal = ttk.Button(root, text=".", command=lambda:button_input(".")).grid(column=2,row=5, padx=5,pady=5)
L_par = ttk.Button(root, text ='(', command=lambda:button_input("(")).grid(column=3,row=3, padx=5, pady=5)
R_par = ttk.Button(root, text =')', command=lambda:button_input(")")).grid(column=3,row=4, padx=5, pady=5)

equation = ttk.Button(root, text="=", command=lambda:evaluate_expression(expression)).grid(columnspan=1, column=3, row=2,padx=5,pady=5)


#set of text editing buttons, click support only. 
delete = ttk.Button(root, text="del", command=lambda:del_entry()).grid(columnspan=1, column=0, row=5)
clear = ttk.Button(root, text="C", command=lambda:clear_entry()).grid(columnspan=1, column=3, row=5)

root.mainloop()
