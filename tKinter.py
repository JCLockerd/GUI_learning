import tkinter  # Imports tkinter library
root = tkinter.Tk()  # Creates a 'window'
root.title("First App")
root.geometry("500x300")
my_lable = tkinter.Label(root)
my_lable.config(text="Hey there!", fg="pink")
my_lable.grid()

root.mainloop()  # Starts GUI learning
