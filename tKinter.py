import tkinter  # Imports tkinter library
root = tkinter.Tk()  # Creates a 'window'
root.title("First App")
root.geometry("500x300")

my_lable = tkinter.Label(root)
my_lable.config(text="uwu!", fg="#FFA490", bg="#C4EFF8")
my_lable.grid()

my_lable2 = tkinter.Label(root)
my_lable2.config(text="UWU?", fg="#C9F8C4")
my_lable2.grid()

root.mainloop()  # Starts GUI learning
