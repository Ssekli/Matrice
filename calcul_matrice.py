#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     10/02/2023
# Copyright:   (c) Administrateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#verif même matrice
def verif_matrice(matrice, matrice1) :
    ''' Return True si matrices sont de meme dimensions'''
    if len(matrice) == len(matrice1) and len(matrice[0]) ==  len(matrice1[0]) :
        return True
    else :
        return False

def add_matrice(matrice, matrice1) :
    '''On additionne les valeurs de chaque matrice'''
    matrice_somme = []
    if verif_matrice(matrice, matrice1) == False :
        print("impossible d'additionner")
    else :
        for i in range (len(matrice)) :
            tmp = [] #obligé de créer un temporaire et dajouter ds le temp
            for j in range(len(matrice[i])) :
                tmp.append(matrice[i][j] + matrice1[i][j])
            matrice_somme.append(tmp) #ajouter le temp à somme va créer matrice
        return matrice_somme #si ps de temp va tout ajouter dans i


def multiplication_matrice_scalaire(matrice, scalaire) :
    '''On demande un nombre puis on le multiplie à la matrice'''
    matrice_mult = []
    for i in range (len(matrice)) :
        tmp = []
        for j in range(len(matrice[i])) :
            tmp.append(matrice[i][j]*int(scalaire))
        matrice_mult.append(tmp)
    return matrice_mult

def transpo_matrice(matrice) :
    matrice_transpo = []
    ''' ici on va faire transposition de matrice. Ligne deviennent collonnes'''
    for i in range (len(matrice[0])) : #on veut transformer ligne en colonne
        tmp = []  #dc on boucle sur longueur de colonne
        for j in range(len(matrice)) :
            tmp.append(matrice[j][i])
        matrice_transpo.append(tmp)
    return matrice_transpo


def verif_multipliable(matrice, matrice1) :
    ''' On ne peut que multiplier si longueur == colonne pour les 2 matrices'''
    if len(matrice[0]) == len(matrice1) :
        return True
    else :
        return False


#multiplication de matrice
def multi_matrice(matrice, matrice1) :
    matric_multi = []
    '''multiplication d'une matrice a par matrice b'''
    if verif_multipliable(matrice, matrice1) :
        for i in range(len(matrice)) :
            tmp = []
            for j in range(len(matrice1[0])) :
                tmp1 = 0
                for k in range(len(matrice[0])) :
                    tmp1 += (matrice[i][k])*(matrice1[k][j])
                tmp.append(tmp1)
            matric_multi.append(tmp)
    return matric_multi


#derminant d'une matrice
def determinant_matrice(matrice) :
    '''Permet de calculer le derteminant (sur [[a, b][c, d]  = ad - bc.
    Pr une matrice carré)'''
    determinant = (matrice[0][0])*(matrice[1][1]) - (matrice[0][1])*(matrice[1][0])
    return determinant

def inversion_matrice(matrice) :
    det = determinant_matrice(matrice)
    if det !=0 :
        tmp = matrice[0][0]
        matrice[0][0] = matrice[1][1]
        matrice[1][1] = tmp

        matrice[0][1] *= -1
        matrice[1][0] *= -1

        mati = []
        for ligne in matrice :
            matj = []
            for element in ligne :
                matj.append(element *(1/det))
            mati.append(matj)
        return mati
    else :
        print("opé impossible")
        return none