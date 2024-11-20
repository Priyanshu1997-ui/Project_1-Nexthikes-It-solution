from tkinter import *
import tkinter as tk
root = Tk()
Val = ""    # By using it we ensure that it starts as an empty string, ready to accept new input.
def btnClick(number):    #when user click any button the btn click function append the coresponding character to current mathematical expression   
    global Val            # stored the mathematical expression 
    Val = Val + str(number)   # it can convert value into the string and store it into the val.
    data.set(Val)

def clear():
    global Val
    Val = ""                    # Reset the input expression
    data.set("")                

def btnequal():
    global Val
    try:
        result = str(eval(Val))  # Evaluate the expression stored in Val
        data.set(result)         # Display the result
        Val = result             # Update Val to the result for further calculations
    except Exception:
        data.set("error")        # Display "error" for invalid expressions
        Val = ""

def back():
    global Val
    Val = Val[:-1]         #[-1] means remove only one character at a time.
    data.set(Val) 
  

equation = tk.StringVar()         

root.title("Priyanshu's Calculator") # calculator header 
root.geometry("361x455") # calculator frame size

data = StringVar()

#this display variable is responsible to show the number that we are selecting on the calculator and it is also showing the final result
# here we have used multiple paramters to fix its look and feel. since we are using 'Entry' function here it is taking and showing the results and the inputs on the screen
display = Entry(root, textvariable=data, bd=29, justify="right", bg="powder blue", font=("Ariel", 20))
display.grid(row=0, columnspan=4)

# this piece of code is used to create the buttons like 7,8,9,+ of the calculator in which 
# btn7 is the name of the button no.7, text="7" shows the no.7 on the button
# Command is used for the no/character on click of the button.
#Lambda is an argument,without using it we can not call the no./character .

btn7 = Button(root, text="7", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text="+", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('+'))
btn_add.grid(row=1, column=3)

btn4 = Button(root, text="4", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(6))
btn6.grid(row=2, column=2)
btn_multiply = Button(root, text="*", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('*'))
btn_multiply.grid(row=2, column=3)

btn1 = Button(root, text="1", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(3))
btn3.grid(row=3, column=2)
btn_substraction = Button(root, text="-", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('-'))
btn_substraction.grid(row=3, column=3)

btn_decimal = Button(root, text=".", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda:btnClick('.'))
btn_decimal.grid(row=4, column=0)
btn_div = Button(root, text="/", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('/'))
btn_div.grid(row=4, column=1)
btn0 = Button(root, text="0", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(0))
btn0.grid(row=4, column=2)

#Here we use command=btnequal function which is responsible for evaluating the mathematical expression entered by the user (stored in the global variable Val).
#Once the expression is evaluated, btnequal updates the data variable with the result, which is shown on the calculator display.
btn_equal = Button(root, text="=", font=("Ariel", 12, "bold"), bg="green",bd=12, height=2, width=6, command=btnequal)
btn_equal.grid(row=4, column=3)

# command=clear is used to resets the global variable Val, which holds the current mathematical expression, to an empty string ("").
btnC = Button(root, text="C", font=("Ariel", 12, "bold"),bg="red",bd=12, height=2, width=15, command=clear)
btnC.grid(row=5, column=0,columnspan=2)

btn_back = Button(root, text='←', font=("Ariel", 12, "bold"),bg="grey",bd=12, height=2, width=15, command=back)
btn_back.grid(row=5, column=2,columnspan=2)

#it starts the event loop, which is responsible for running the graphical user interface (GUI) application and keeping it responsive.
root.mainloop()
