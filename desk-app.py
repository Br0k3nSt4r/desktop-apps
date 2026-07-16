from tkinter import *

#ventana
ventana_principal= Tk()

#titulo
ventana_principal.title("Sistemas Guanena")

#tamaño
ventana_principal.geometry("500x500")

#color
ventana_principal.config(bg="purple")

#tamaño fijo
ventana_principal.resizable(0,0)

#objeto frame
frame1= Frame(ventana_principal)
frame1.config(bg="green",width=480,height=240)
frame1.place(x=10,y=10)

#imagen del frame
escudo= PhotoImage(file="img/escudoColegio.png")
lb_escudo= Label(frame1, image=escudo)
lb_escudo.place(x=10,y=20)

#bucle
ventana_principal.mainloop()


