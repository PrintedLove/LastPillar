import tkinter

root = tkinter.Tk()
root.geometry("400x200")
root.title("Test")
label = tkinter.Label(root, text = "test text")
font = ("Times New Roman", 20)
label.place(x = 80, y = 20)
root.mainloop()