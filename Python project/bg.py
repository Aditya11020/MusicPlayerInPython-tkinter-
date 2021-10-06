from tkinter import *
from PIL import ImageTk

master = Tk()

#width, height = Image.open(image.png).size

canvas = Canvas(master, width=900, height=563)
canvas.pack()

image = ImageTk.PhotoImage(file="image.png")
canvas.create_image(0, 0, image=image, anchor=NW)

canvas_id = canvas.create_text(10, 10,fill="white",anchor="nw",)
canvas.itemconfig(canvas_id, text="this is the text "*300, width=780)
canvas.itemconfig(canvas_id, font=("courier", 12))

canvas.insert(canvas_id, 12, "new ")

#canvas.create_text(2, 2, text="Python")

mainloop()