from tkinter import Button, Tk, Toplevel, Canvas, Entry, filedialog, messagebox
from PIL import Image, ImageTk
from pypresence import Presence
from os import path as ospath, system
from time import time, sleep
from threading import Thread
from json import load, dump


__author__="4lxprime"
__filename__="launcher.py"
__project__="Project GalaxieFN"


def stop():
    root.destroy()
    exit(0)

def startG():
    conf_file=open('config.json')
    p=load(conf_file)
    if p['path']=='' or ospath.exists(p):
        messagebox.showinfo(title="Fichiers non trouvés", message="Vous devez d'abbord parametrer les fichiers du jeux ou verifier qu'ils soient bien parametrer.")
    else:
        system(f"start {p}/start.bat")
        

## uncomment if you would to active discord rpc
#rpc_id=1029738684330819665
#RPC=Presence(rpc_id)
#RPC.connect()
#start=int(time())

#def DRPC():
#    while 1:
#        RPC.update(
#            start=start,
#            buttons=[{"label": "Discord GalaxieFN", "url": "https://giscord.gg/A9uMJJCY"}],
#            state="GalaxieFN Launcher",
#            large_image="galaxiefn"
#        )

#tRpc=Thread(target=DRPC)
#tRpc.setDaemon(True)
#tRpc.start()

root=Tk()

root.geometry("1000x500")
root.minsize(1000, 500)
root.maxsize(1000, 500)
root.title("  GalaxieFN Launcher")
root.iconbitmap(f"{ospath.dirname(ospath.realpath(__file__))}/assets/logo.ico") # if you would compile with nuitka, remove assets/

class param():
    def __init__(self):
        self.top=Toplevel(root)
        self.top.geometry("800x500")
        self.top.minsize(800, 500)
        self.top.maxsize(800, 500)
        self.top.title(f"  GalaxieFn Parameters")
        self.top.iconbitmap(f"{ospath.dirname(ospath.realpath(__file__))}/assets/logo.ico") # if you would compile with nuitka, remove assets/
        
        with open("config.json", "w") as f:
            f.write('{"path": "", "username": "GalaxieFNuser"}')
        self.conf_file=open("config.json")
        self.config=load(self.conf_file)
        
        self.PBackImg=ImageTk.PhotoImage(
            Image.open(
                f"{ospath.dirname(ospath.realpath(__file__))}/assets/back.jpg" # if you would compile with nuitka, remove assets/
                ).resize
            (
                (1000, 500)
            )
        )


        self.Pcanvas=Canvas(self.top, 
            bg="#23272e", 
            width=1000,
            height=500
        )

        self.Pcanvas.pack(expand=True, fill="both")

        self.Pbg=self.Pcanvas.create_image(0, 0, image=BackImg, anchor="nw")

        self.Ptop=self.Pcanvas.create_rectangle(
            0, -250, 
            self.top.maxsize()[0], 100,
            outline="black", 
            fill="#1c1c1c"
        )
        
        self.PTt=self.Pcanvas.create_text(
            self.top.winfo_width()/2, 50, 
            text="GalaxieFN Launcher", 
            font=('Helvetica 30 bold'), 
            fill="white"
        )
        
        self.UsrT=self.Pcanvas.create_text(
            (self.top.winfo_width()/2)-150, (self.top.winfo_height()/2), 
            text="Username: ", 
            font=("Helvetica 20 bold"),
            fill="white"
        )
        
        self.UsrE=Entry(self.top,
            font=("Arial", 20), 
            relief="flat", 
            borderwidth=0, 
            bg="#1e2227", 
            width=15, 
            highlightthickness=1, 
            highlightbackground='black', 
            fg="white"
        )
        
        self.UsrE.insert(0, self.config['username'])
        
        self.Pcanvas.create_window(
            (self.top.winfo_width()/2)+50, self.top.winfo_height()/2,
            window=self.UsrE
        )
        
        
        
        self.FileT=self.Pcanvas.create_text(
            (self.top.winfo_width()/2)-150, (self.top.winfo_height()/2)+50, 
            text="Game path: ", 
            font=("Helvetica 20 bold"),
            fill="white"
        )
        
        self.FileE=Entry(self.top,
            font=("Arial", 20), 
            relief="flat", 
            borderwidth=0, 
            bg="#1e2227", 
            width=15, 
            highlightthickness=1, 
            highlightbackground='black', 
            fg="white"
        )
        
        self.Pcanvas.create_window(
            (self.top.winfo_width()/2)+200, (self.top.winfo_height()/2)+50, 
            window=Button(self.top, 
                font=("Arial", 15), 
                relief="flat", 
                borderwidth=0, 
                bg="#1a1d21", 
                width=3, 
                height=1, 
                highlightthickness=1, 
                highlightbackground='black', 
                fg="white", 
                text="...",
                command=lambda : self.FileE.insert(0, filedialog.askdirectory(title="GalaxieFN Path"))
            )
        )
        
        self.FileE.insert(0, self.config['path'])
        
        self.Pcanvas.create_window(
            (self.top.winfo_width()/2)+50, (self.top.winfo_height()/2)+50,
            window=self.FileE
        )
        
        self.validB=self.Pcanvas.create_window(
            self.top.winfo_width()/2, 
            (self.top.winfo_height()/2)+200, 
            window=Button(self.top, 
                font=("Arial", 15), 
                relief="flat", 
                borderwidth=0, 
                bg="#1e2227", 
                width=7, 
                highlightthickness=1, 
                highlightbackground='black', 
                fg="white", 
                text="Valid",
                command=self.saveBis
            )
        )
        
        self.top.bind('<Return>', self.save)
    
    def save(self, x):
        self.config['username']=self.UsrE.get()
        self.config['path']=self.FileE.get()
        dump(self.config, open("config.json", "w"))
    
    def saveBis(self):
        self.config['username']=self.UsrE.get()
        self.config['path']=self.FileE.get()
        dump(self.config, open("config.json", "w"))

BackImg=ImageTk.PhotoImage(
    Image.open(
        f"{ospath.dirname(ospath.realpath(__file__))}/assets/back.jpg" # if you would compile with nuitka, remove assets/
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
        f"{ospath.dirname(ospath.realpath(__file__))}/assets/logo.png" # if you would compile with nuitka, remove assets/
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
        text="Play",
        command=startG
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
    60, 
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
        text="Param", 
        command=param
    ),
    state="normal"
)

root.protocol("WM_DELETE_WINDOW", stop)
root.mainloop()

# nocturno > cosmos
# ez