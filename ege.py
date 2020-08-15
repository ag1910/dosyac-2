from tkinter import *
from tkinter import messagebox

def hesapla(): 

    veri1 =kutu.get()
    veri1 = str(veri1)
    veri = kutu1.get()
    veri = str(veri)
    var = messagebox.showinfo("Uyarı" , "Girdiğiniz üsteki değer dosyanının adı altaki değerde onun uzantısıdır.")
    f = open(veri1+"."+veri, "x")
    exec(f)

anapencere = Tk()
anapencere.geometry("600x600+100+100")
anapencere['bg']='green'
anapencere.title("Hesap Mak. V0.1 Beta")




kutu = Entry(anapencere)

kutu.pack()
kutu1 = Entry(anapencere)
kutu1.pack()

buton = Button(anapencere)
buton.config(text = "Oluştur!", font = "bold 8",fg = "green", command = hesapla)
buton.pack()

mainloop()