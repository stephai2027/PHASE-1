import numpy as np

#Demander la taille des matrices
rows = int(input("Nombre de lignes : "))
cols = int(input("Nombre de colonnes : "))

def saisir_matrice(nom):
    print(f"Entrer les éléments de la matrice {nom} :")
    matrice = []
    try:
        for i in range(rows):
            ligne = input(f"Ligne {i+1} (entiers séparés par des espaces) : ").split()
            matrice.append([float(x) for x in ligne]) 
        return np.array(matrice)
    except ValueError:
        print("veuillez entrer le nombre de caractéres réels requis pour cette matrice")
        
#Saisie des matrices
A = saisir_matrice("A")
B = saisir_matrice("B")


n = input("quelle est l'opération voulez vous effectuer ?(minuscule requise) :")
if (n =='addition'):
    if (A.shape == B.shape):print (A+B)
    else : print("addition impossible")
elif(n == 'soustraction'):
    if (A.shape == B.shape): print(A-B)
    else : print("différence impossible")
elif(n == 'produit matricielle'):
    if (A.shape[1] == B.shape[0]):print(A.dot(B))
    else: print("produit impossible")
elif(n == 'produit step by step'):
    if (A.shape == B.shape):print(A*B)
    else : print("produit impossible")
elif(n == 'division'):
    if (A.shape == B.shape):print(A/B)
    else : print("division impossible")
else : print("opération incorrecte")

