from tkinter import *
from PIL import Image, ImageTk
import os

def stop():
    root.destroy()
    exit(0)

root=Tk()

root.geometry("1000x500")
root.minsize(1000, 500)
root.title("  GalaxieFN Launcher")

canvas=Canvas(root, 
    bg="#23272e", 
    width=1000,
    height=500
)

top=canvas.create_rectangle(
    0, 0, 
    root.maxsize()[0], 100,
    outline="black", 
    fill="#1c1c1c"
)

root.update()

LogoImg=ImageTk.PhotoImage(
    Image.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/assets/logo.png"
        ).resize
    (
        (80, 80)
    )
)

LogoBut=Button(root, 
    font=("Arial", 20), 
    image=LogoImg, 
    relief="flat", 
    borderwidth=0, 
    bg="#1c1c1c", 
    activebackground="#1c1c1c"
)

canvas.create_window(80, 50, 
    window=LogoBut
)

Tt=canvas.create_text(root.winfo_width()/2, 50, 
    text="GalaxieFN Launcher", 
    font=('Helvetica 30 bold'), 
    fill="white"
)

cred=canvas.create_window(
    root.winfo_width()-60, root.winfo_height()-30, 
    window=Button(root, 
        font=("Arial", 15), 
        relief="flat", 
        borderwidth=0, 
        bg="#1e2227", 
        width=7, 
        highlightthickness=1, 
        highlightbackground='black', 
        fg="white", 
        text="Credits"
    )
)

canvas.pack(expand=True, fill="both")
root.protocol("WM_DELETE_WINDOW", stop)
root.mainloop()