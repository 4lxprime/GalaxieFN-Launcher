from tkinter import *
from PIL import Image, ImageTk
from pypresence import Presence
import os
import time
import threading


__author__="4lxprime"
__filename__="launcher.py"
__project__="Project GalaxieFN"


def stop():
    root.destroy()
    exit(0)

def RPC():
    try:
        start=int(time.time())
        rpc_id=1029738684330819665
        RPC=Presence(rpc_id)
        RPC.connect()
        RPC.update(
            start=start,
            buttons=[
                {"label": "Discord GalaxieFN", "url": "https://giscord.gg/A9uMJJCY"}
            ],
            large_image="logo",
            state="GalaxieFN Launcher")
        while 1:
            time.sleep(15)
    except: 
        pass

tRpc=threading.Thread(target=RPC)
tRpc.setDaemon(True)
tRpc.start()

root=Tk()

root.geometry("1000x500")
root.minsize(1000, 500)
root.maxsize(1000, 500)
root.title("  GalaxieFN Launcher")
root.iconbitmap(f"{os.path.dirname(os.path.realpath(__file__))}/assets/logo.ico")

class param():
    def __init__(self):
        self.top=Toplevel(root)
        self.top.geometry("800x500")
        self.top.minsize(800, 500)
        self.top.maxsize(800, 500)
        self.top.title(f"  GalaxieFn Parameters")
        self.top.iconbitmap(f"{os.path.dirname(os.path.realpath(__file__))}/assets/logo.ico")

BackImg=ImageTk.PhotoImage(
    Image.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/assets/back.jpg"
        ).resize
    (
        (1000, 500)
    )
)


canvas=Canvas(root, 
    bg="#23272e", 
    width=1000,
    height=500
)

canvas.pack(expand=True, fill="both")

bg=canvas.create_image(0, 0, image=BackImg, anchor="nw")

top=canvas.create_rectangle(
    0, -250, 
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

# canvas.create_window(80, 50, 
#     window=LogoBut
# )

Tt=canvas.create_text(
    root.winfo_width()/2, 50, 
    text="GalaxieFN Launcher", 
    font=('Helvetica 30 bold'), 
    fill="white"
)

PlayBut=canvas.create_window(
    root.winfo_width()/2, 
    root.winfo_height()/2,
    window=Button(
        font=('Helvetica 25 bold'), 
        relief="flat", 
        borderwidth=0, 
        bg="#1e2227", 
        width=10, 
        highlightthickness=1, 
        highlightbackground='black', 
        fg="white", 
        text="Play"
    )
)

cred=canvas.create_window(
    root.winfo_width()-60, 
    root.winfo_height()-30, 
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

paramB=canvas.create_window(
    root.winfo_width()-60, 
    50, 
    window=Button(root, 
        font=("Arial", 15), 
        relief="flat", 
        borderwidth=0, 
        bg="#1e2227", 
        width=7, 
        highlightthickness=1, 
        highlightbackground='black', 
        fg="white", 
        text="Param", 
        command=param
    ),
    state="normal"
)

root.protocol("WM_DELETE_WINDOW", stop)
root.mainloop()