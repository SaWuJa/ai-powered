from tkinter import *
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()

class Software:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("500x400")
        self.master.resizable(0,0)
        self.master.config(bg = "red")

        self.first_number = IntVar()
        self.second_number = IntVar()

        self.first_number_lbl = Label(self.master, text='First Number', font="Arial 20 bold", bg="red", fg="white")
        self.first_number_lbl.place(x=10, y=50)

        self.first_number_txt = Entry(self.master, textvariable=self.first_number)
        self.first_number_txt.place(x=250, y=50)

        self.second_number_lbl = Label(self.master, text='Second Number', font="Arial 20 bold", bg="red", fg="white")
        self.second_number_lbl.place(x=10, y=150)

        self.second_number_txt = Entry(self.master, textvariable=self.second_number)
        self.second_number_txt.place(x=250, y=150)

        self.add_btn = Button(self.master, text="Add", command=self.addition, bg="white")
        self.add_btn.place(x=50, y=230)

        self.subtract_btn = Button(self.master, text="Subtract", command=self.subtraction, bg="white")
        self.subtract_btn.place(x=150, y=230)

        self.multiply_btn = Button(self.master, text="Multiply", command=self.multiplication, bg="white")
        self.multiply_btn.place(x=250, y=230)

        self.divide_btn = Button(self.master, text="Divide", command=self.division, bg="white")
        self.divide_btn.place(x=350, y=230)

        self.clear_btn = Button(self.master, text="Clear", command=self.clear, bg="white")
        self.clear_btn.place(x=200, y=280)

    def clear(self):
        self.first_number_txt.delete(0, END)
        self.second_number_txt.delete(0, END)

    def calculate(self, operation):
        try:
            first_number = self.first_number.get()
            second_number = self.second_number.get()
            
            if operation == "+":
                total = first_number + second_number
            elif operation == "-":
                total = first_number - second_number
            elif operation == "*":
                total = first_number * second_number
            elif operation == "/":
                if second_number == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                total = first_number / second_number

            result = f"The result of the {operation} is {total}"
            messagebox.showinfo("Result", result)
            engine.say(result)
            engine.runAndWait()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values")

    def addition(self):
        self.calculate("+")

    def subtraction(self):
        self.calculate("-")

    def multiplication(self):
        self.calculate("*")

    def division(self):
        self.calculate("/")


def main():
    top = Tk()
    structure = Software(top)
    top.mainloop()


if __name__ == "__main__":
    main()
