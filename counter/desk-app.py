from tkinter import *
from tkinter import messagebox

#ventana
ventana_principal= Tk()

#titulo
ventana_principal.title("Counter Test")

#tamaño
ventana_principal.geometry("500x500")

#color
ventana_principal.config(bg="black")

#tamaño fijo
ventana_principal.resizable(0,0)

#-------------------
#frame de data input
#-------------------
frame_input= Frame(ventana_principal)
frame_input.config(bg="gray",width=480,height=240)
frame_input.place(x=10,y=10)

#-------------------
#frame de data work
#-------------------
frame_work= Frame(ventana_principal)
frame_work.config(bg="white",width=480,height=120)
frame_work.place(x=10,y=260)

#--------------------
#frame de data answer
#--------------------
frame_answer= Frame(ventana_principal)
frame_answer.config(bg="gray",width=480,height=100)
frame_answer.place(x=10,y=390)

#bucle
ventana_principal.mainloop()
