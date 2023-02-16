#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     08/02/2023
# Copyright:   (c) Administrateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

''' Appli de calculs de matrice'''

from tkinter import *
from random import *

from calcul_matrice import *
#import calcul_matrice

'''Appli en tk inter qui permet de faire des opé sur matrice'''

#recupere matrice a
def recup_matricea() :
    matricea = [] #matrice temp
    idx = 0
    for i in input_matricea.get("1.0", END).splitlines() : # recup la saisie
        if i != '' :
            matricea.append([])
            for j in i.split(",") :
                if j.lstrip("-").isnumeric() :
                    matricea[idx].append(int(j))
            idx += 1
    return matricea

#recupere matrice b
def recup_matriceb() :
    matriceb = [] #matrice temp
    idx = 0
    for i in input_matriceb.get("1.0", END).splitlines() : # recup la saisie
        if i != '' :
            matriceb.append([])
            for j in i.split(",") :
                if j.lstrip("-").isnumeric() :
                    matriceb[idx].append(int(j))
            idx += 1
    return matriceb

def vider():
    text_result.delete('1.0', END)

def result_addition() :
    '''pour obtenir le résultat de mon addition'''
    matricea = recup_matricea()
    matriceb = recup_matriceb()
    matrice = add_matrice(matricea, matriceb)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


def result_multiplication() :
    '''pour obtenir le résultat de mon multi'''
    matricea = recup_matricea()
    matriceb = recup_matriceb()
    matrice = multi_matrice(matricea, matriceb)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

def result_deter_a() :
    '''Pour Obternir le determinant de A'''
    matricea = recup_matricea()
    determinant = determinant_matrice(matricea)
    text_result.insert(END, determinant)

def result_deter_b() :
    '''Pour Obternir le determinant de B'''
    matriceb = recup_matriceb()
    determinant = determinant_matrice(matriceb)
    text_result.insert(END, determinant)

def result_multi_a_scalaire() :
    '''Pour multiplier A par scalaire'''
    matricea = recup_matricea()
    scalaire = int(input_scalaire.get())
    matrice = multiplication_matrice_scalaire(matricea, scalaire)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")
    

def result_transpo_a() :
    ''' calcul de transpo A '''
    matricea = recup_matricea()
    matrice = transpo_matrice(matricea)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

def result_transpo_b() :
    '''calcul transpo B'''
    matriceb = recup_matriceb()
    matrice = transpo_matrice(matriceb)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


def result_inversion_a() :
    '''inversion de a'''
    matricea = recup_matricea()
    matrice = inversion_matrice(matricea)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

def result_inversion_b() :
    '''inversion de a'''
    matriceb = recup_matriceb()
    matrice = inversion_matrice(matriceb)
    text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


#Création de la fenetre principale (master)
Master = Tk() # !!!! au maj on est en objet
Master.resizable(False, False)
Master.geometry("1200x1200")
Master.title("Matrice")

#cadre pour les 2 matrice
Matrice = Frame(Master, bg = "green", width = 1100, height = 150, borderwidth = 3, relief = "solid")
Matrice.pack(side = TOP, padx = 0, pady = 0)
Matrice.propagate(False) # si on veut dimensionner la fenetre

#cadre matrice A
Matricea = Frame(Matrice, bg = "black", width = 240, height = 100)
Matricea.pack(side = LEFT, padx = 50, pady = 10)
Matricea.propagate(False)

#cadre matrice B
Matriceb = Frame(Matrice, bg = "black", width = 240, height = 100)
Matriceb.pack(side = LEFT, padx = 50, pady = 10)
Matriceb.propagate(False)

#cadre Scalaire
Scalaire = Frame(Matrice, bg = "black", width = 240, height = 100)
Scalaire.pack(side = LEFT, padx = 50, pady = 10)
Scalaire.propagate(False)

#cadre calculs
Calcul = Frame(Master, bg = "blue", width = 1100, height = 150, borderwidth = 3, relief = "solid")
Calcul.pack(side = TOP, padx = 0, pady = 30)
Calcul.propagate(False) # si on veut dimensionner la fenetre

#cadre résultats
Cares = Frame(Master, bg = "red", width = 1100, height = 150, borderwidth = 3, relief = "solid")
Cares.pack(side = TOP, padx = 0, pady = 5)
Cares.propagate(False) # si on veut dimensionner la fenetre

text_result = Text(Cares, width = 280, height = 200, bg ="white")
text_result.pack(side = LEFT, padx = 10, pady = 10)

#widget addition
BoutonAddition = Button(Calcul, text = "Addition A + B", command = result_addition)
BoutonAddition.pack(side = LEFT, padx = 45, pady = 0)

#widget multiplication A*B
BoutonMultik = Button(Calcul, text = "Multiplication A x B", command = result_multiplication)
BoutonMultik.pack(side = LEFT, padx = 45, pady = 0)

#widget multiplication *K
BoutonMultik1 = Button(Calcul, text = "Multiplication A x k", command = result_multi_a_scalaire)
BoutonMultik1.pack(side = LEFT, padx = 45, pady = 0)

#widget Determinant A
BoutonDetera = Button(Calcul, text = "Determinant A", command = result_deter_a)
BoutonDetera.pack(side = LEFT, padx = 45, pady = 0)

#widget transposition A
BoutonTransA = Button(Calcul, text = "Transposition A", command = result_transpo_a)
BoutonTransA.pack(side = LEFT, padx = 45, pady = 0)

#widget inverse A
BoutonInvA = Button(Calcul, text = "inverse A", command = result_inversion_a)
BoutonInvA.pack(side = LEFT, padx = 45, pady = 0)

#cadre de frappe matrice a
input_matricea = Text(Matricea, width=200, height=140, bg = "white")
input_matricea.pack(padx=10, pady=10)

#cadre de frappe matrice b
input_matriceb = Text(Matriceb, width=200, height=140, bg = "white")
input_matriceb.pack(padx=10, pady=10)

#cadre de frappe pr le scalaire
input_scalaire = Entry(Scalaire, bg = "white")
input_scalaire.pack( padx=10, pady=15)

#bouton pour vider la fenetre resultat
Boutonvide = Button(Scalaire, text="Vider", command=vider)
Boutonvide.pack(padx=10, pady=15)

Master.mainloop()




