import tkinter.messagebox
from tkinter.ttk import *
from tkinter import *
from time import strftime


main = Tk()
main.geometry("400x400")
main.title("welcome")


def left_side():
    """Left """
    global left_entry, right_entry, answer_label, integer_combo
    left_entry.get()


def right_side():
    """Right"""
    global left_entry, right_entry, answer_label, integer_combo
    right_entry.get()

def combo_calc():
    global left_entry, right_entry, answer_label, integer_combo

    if integer_combo.get() == "+":
        answer_label['text'] = str(int(left_entry.get()) + int(right_entry.get()))
    elif integer_combo.get() == "-":
        answer_label['text'] = str(int(left_entry.get()) - int(right_entry.get()))
    elif integer_combo.get() == "*":
        answer_label['text'] = str(int(left_entry.get()) * int(right_entry.get()))
    elif integer_combo.get() == "/":
        answer_label['text'] = str(int(left_entry.get()) / int(right_entry.get()))


def time():
    czas = strftime('%H:%M:%S %p')
    zegar.config(text=czas)
    zegar.after(1000, time)

def button_clicked():
    text= Label(main, text="This button has been clicked!")
    text.pack()

def exit1():
    exit()


def openfile():
    okno=tkinter.Tk()
    okno.title("kalkulator")
    okno.geometry("500x100")
    global left_entry, right_entry, answer_label, integer_combo
    integer_options = ["+", "-", "*", "/"]
    integer_combo = Combobox(okno,
                             values=integer_options)
    integer_combo.set("+")
    integer_combo.grid(row=0, column=1)
    left_entry = Entry(okno)
    left_entry.grid(row=0, column=0)
    right_entry = Entry(okno)
    right_entry.grid(row=0, column=2)
    calc_button = Button(okno, text='Calculate', command=combo_calc, background="red",foreground="blue")
    calc_button.grid(row=1, column=1)
    equals_label = Label(okno, text="=")
    equals_label.grid(row=0, column=3)
    answer_label = Label(okno)
    answer_label.grid(row=0, column=4)

def adt():
    tkinter.messagebox.showinfo("Autor", "Kacper Kulaszewicz")


def przycisk():
    if zegar.cget('background') == 'black':
        zegar.config(background='blue')
    elif zegar.cget('background') == 'blue':
        zegar.config(background='black')


menu=Menu(main)
main.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Open", command=openfile)
subm1.add_command(label="Exit",command=exit1)
subm1.add_command(label="test",command=exit1)


subm2=Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About",command=adt)


"""button_one = Button(main, text="zakoncz program", fg="red", command=exit1)
button_one.place(x=0,y=0)"""


zegar = Label(main,
            font=('times', 50, 'bold'),
            background="black",
            foreground='white')


zegar.pack()
time()


button_two = Button(main,
                    text="click me",
                    fg="red", bg="black",
                    padx=10,
                    pady=10,
                    font=("Times",30),
                    command=przycisk)
button_two.pack(padx=50, pady=50)


"""logo = PhotoImage(file='./kk.png')
updated_logo = logo.subsample(4,4)
image_label = Label(main, image=updated_logo)
image_label.pack()"""




main.mainloop()
