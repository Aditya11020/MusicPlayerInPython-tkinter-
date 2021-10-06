from tkinter import *
from PIL import Image

root = Tk()
file="E:\Python project\mgif.gif"
info= Image.open(file)
frames = info.n_frames
print(frames)
im = [PhotoImage(file=file,format=f"gif-index{i}")for i in range(frames)]
count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]
    gif_label.config(image=im2)
    count+=1
    if count==frames:
        count=0
    anim=root.after(50,lambda: animation(count))
def stop_animation():
    root.after_cancel(anim)

gif_label = Label(root,image="")
gif_label.pack()

start = Button(root,text="start",command=lambda:animation(count))
start.pack()

stop = Button(root,text="stop",command=stop_animation)
stop.pack()
root.mainloop()
