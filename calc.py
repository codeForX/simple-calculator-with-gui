from tkinter import *


total = 0
limit = 99999999999999

def main():
    root = Tk()
    root.title('simple calc')
    display = Entry(root, width=35, borderwidth=5)
    display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:displayNum(1 ,display))
    button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:displayNum(2,display))
    button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:displayNum(3,display))
    button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:displayNum(4,display))
    button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:displayNum(5,display))
    button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:displayNum(6,display))
    button_7 = Button(root, text='7', padx=40, pady=20, command=lambda:displayNum(7,display))
    button_8 = Button(root, text='8', padx=40, pady=20, command=lambda:displayNum(8,display))
    button_9 = Button(root, text='9', padx=40, pady=20, command=lambda:displayNum(9,display))
    button_0 = Button(root, text='0', padx=40, pady=20, command=lambda:displayNum(0,display))
    clear = Button(root, text='clear', padx=80, pady=20, command=lambda:operations('c',display))
    plus = Button(root, text='+', padx=40, pady=20,command=lambda:operations('+',display))
    equal = Button(root, text='=', padx=90, pady=20,command=lambda:operations('=',display))

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_0.grid(row=4, column=0)
    clear.grid(row=4, column=1, columnspan=2)

    plus.grid(row=5, column=0)
    equal.grid(row=5, column=1, columnspan=2)
    root.mainloop()


def displayNum(num ,display):
   number = str(display.get()) + str(num)
   clearDisplay(display)
   display.insert(0, number)


def operations(operation, display):
    global total
    if operation == 'c':
        total = 0
        clearDisplay(display)
    elif operation == '=':
        if total == 0:
            clearDisplay(display)
            return
        total = total + int(display.get())
        clearDisplay(display)
        display.insert(0, total)
        total = 0

    elif operation == '+':
        total = total + int(display.get())
        clearDisplay(display)



def clearDisplay(display):
    display.delete(0, END)

main()
