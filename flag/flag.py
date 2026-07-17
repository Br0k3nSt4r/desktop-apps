from tkinter import *

#ventana
bandera_noruega= Tk()

#titulo
bandera_noruega.title("N O R W A Y  flag :3")

#tamaño
bandera_noruega.geometry("747x542")

#tamaño fijo
bandera_noruega.resizable(0,0)

#objeto frame rojo
frame1= Frame(bandera_noruega)
frame1.config(bg="red",width=204,height=204)
frame1.place(x=0,y=0)

frame2= Frame(bandera_noruega)
frame2.config(bg="red",width=204,height=204)
frame2.place(x=0,y=339)

frame3= Frame(bandera_noruega)
frame3.config(bg="red",width=408,height=204)
frame3.place(x=340,y=0)

frame4= Frame(bandera_noruega)
frame4.config(bg="red",width=408,height=204)
frame4.place(x=340,y=339)

#objeto frame azul
frame1= Frame(bandera_noruega)
frame1.config(bg="blue",width=65,height=542)
frame1.place(x=240,y=0)

frame2= Frame(bandera_noruega)
frame2.config(bg="blue",width=747,height=65)
frame2.place(x=0,y=240)

#bucle
bandera_noruega.mainloop()

