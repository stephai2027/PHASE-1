#Importation du module tkinter pour créer l'interface graphique
import tkinter as tk

#Fonction pour évaluer l'expression mathématique
def calculer():
    try:
        resultat = eval(ecran.get())  # Évalue le texte saisi dans le champ d'entrée
        ecran.delete(0, tk.END)       # Efface le contenu actuel
        ecran.insert(0, str(resultat))  # Affiche le résultat
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Erreur")     # Affiche "Erreur" en cas de syntaxe incorrecte

#Fonction pour ajouter un chiffre ou un opérateur au champ d'entrée
def ajouter(val):
    ecran.insert(tk.END, val)

#Fonction pour effacer complètement le champ d'entrée
def effacer():
    ecran.delete(0, tk.END)

#Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")  # Titre de la fenêtre

#Champ d'affichage (Entry)
ecran = tk.Entry(fenetre, width=25, font=('Arial', 16), bd=5, justify='right')
ecran.grid(row=0, column=0, columnspan=4)  # Placement sur 4 colonnes

#Liste des boutons sous forme de tuples : (texte, ligne, colonne)
boutons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

#Création dynamique des boutons
for (texte, ligne, col) in boutons:
    if texte == '=':
        # Bouton égal (=) déclenche le calcul
        tk.Button(fenetre, text=texte, width=5, height=2, command=calculer).grid(row=ligne, column=col)
    else:
        # Autres boutons : chiffres ou opérateurs
        tk.Button(fenetre, text=texte, width=5, height=2, command=lambda t=texte: ajouter(t)).grid(row=ligne, column=col)


#Bouton pour effacer tout (C)
tk.Button(fenetre, text='C', command=effacer).grid(row=5, column=0, columnspan=4, sticky='we')

#Boucle principale de l'application (lancement)
fenetre.mainloop()