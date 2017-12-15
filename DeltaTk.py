from tkinter import *
from math import *
import sys

# --- Je creer une premiere fenetre tk --- #
fenetre = Tk()


# --- Je creer une fonction qui récupère les variables et les affiches --- #
def affichevariable():
    A=int(intA.get())
    B=int(intB.get())
    C=int(intC.get())

    delta = (B*B)-4*(A)*(C)    
    deltaResultat= Label(fenetre, text="Delta = "+str(delta))
    deltaResultat.grid(row=6, column=1)

    if A == 0:
        ErreurZero=Label(fenetre, text="Division par 0 impossible, merci de bien vouloir recommencer.")
        ErreurZero.grid(row=7, column=1)
        sys.exit()
        
    if delta > 0:
        x1 = (-B-sqrt(delta))/(2*A)
        x2 = (-B+sqrt(delta))/(2*A)
        resultatfinal=Label(fenetre, text="x1=" + str(x1) +"   x2=" + str(x2) + ".")
        resultatfinal.grid(row=7, column=1)

    if delta == 0:
        x0 = -B/(2*A)
        resultatfinal=Label(fenetre, text="L'unique solution vaut "+ str(x0) +".")
        resultatfinal.grid(row=7, column=1)

    if delta < 0:
        resultatfinal=Label(fenetre, text="Delta < 0, pas de solution", bg="red")
        resultatfinal.grid(row=7, column=1)


# --- Je creer des labels/variables input  --- #
labelTitre = Label(fenetre, text="Calcul Delta", bg="green")
labelTitre.grid(row=0, column=1)


labelA= Label(fenetre, text="A")
labelA.grid(row=1, column=0)

intA=StringVar()
widgetA= Entry(fenetre, textvariable=intA)
widgetA.grid(row=1, column=1)



labelB= Label(fenetre, text="B")
labelB.grid(row=2, column=0)

intB=StringVar()
widgetB= Entry(fenetre, textvariable=intB)
widgetB.grid(row=2, column=1)



labelC= Label(fenetre, text="C")
labelC.grid(row=3, column=0)

intC=StringVar()
widgetC= Entry(fenetre, textvariable=intC)
widgetC.grid(row=3, column=1)


# --- Bouton OK  --- #
buttonOK= Button(fenetre, text="OK", command=affichevariable)
buttonOK.grid(row=4, column=1)


fenetre.mainloop()
