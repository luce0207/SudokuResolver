import tkinter as tk    # Bibliothèque qui permettra de créer l'ihm du programme
from tkinter.font import Font   # Module permettant d'afficher du texte en gras dans l'ihm
from PIL import ImageTk, Image   # Modules permettant d'afficher des images danns l'ihm


grille_test = [[0, 1, 0, 2, 3, 4, 0, 0, 0],
               [3, 0, 0, 5, 0, 6, 0, 1, 0],
               [7, 0, 0, 8, 0, 0, 6, 0, 2],
               [2, 0, 9, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 0, 0, 0, 0, 4],
               [0, 7, 0, 0, 0, 0, 3, 0, 9],
               [4, 0, 6, 0, 0, 2, 0, 0, 7],
               [0, 5, 0, 1, 0, 8, 0, 0, 3],
               [0, 0, 0, 4, 9, 7, 0, 8, 0]]



def absentSurLigne(chiffre, grille, ligne):
    """
    :param chiffre: chiffre entre 1 et 9 dont on on cherche à vérifier l'absence sur une ligne de la grille
    :param grille: grille que l'on veut résoudre
    :param ligne: ligne sur laquelle on cherche à vérifier l'absence du chiffre
    :return: booléen vérifiant l'absence du chiffre sur la ligne
    """
    for j in grille[ligne]:
        if j == chiffre:
            return False
    return True



def absentSurColonne(chiffre, grille, colonne):
    """
        :param chiffre: chiffre entre 1 et 9 dont on on cherche à vérifier l'absence sur une colonne de la grille
        :param grille: grille que l'on veut résoudre
        :param colonne: colonne sur laquelle on cherche à vérifier l'absence du chiffre
        :return: booléen vérifiant l'absence du chiffre sur la colonne
    """
    for i in range(9):
        if grille[i][colonne] == chiffre:
            return False
    return True



def absentSurBloc(chiffre, grille, ligne, colonne):
    """
        :param chiffre: chiffre entre 1 et 9 dont on on cherche à vérifier l'absence sur un bloc de la grille
        :param grille: grille que l'on veut résoudre
        :param ligne: ligne appartenant au bloc
        :param colonne: colonne appartenant au bloc
        :return: booléen vérifiant l'absence du chiffre sur le bloc
    """
    ligneBloc = ligne - (ligne % 3)
    colonneBloc = colonne - (colonne % 3)
    for i in range(ligneBloc, ligneBloc + 3):
        for j in range(colonneBloc, colonneBloc + 3):
            if grille[i][j] == chiffre:
                return False
    return True



def estValide(grille, position):
    """
    :param grille: grille que l'on veut résoudre
    :param position: numéro de la case à partir duquel on cherche à vérifier si la grille est valide, il sert d'itérateur pour parcourir la grille
    :return: booloéen indiquant si la grille est valide à partir de la position donnée
    """
    if position == 81: # Les indices vont de 0 à 80 mais pour prendre en compte la case 80, il faut aller jusqu'à 81
        return True
    ligne = position // 9
    colonne = position % 9
    if grille[ligne][colonne] != 0:
        return estValide(grille, position+1)
    for chiffre in range(1,10):
        if (absentSurLigne(chiffre, grille, ligne) and absentSurColonne(chiffre, grille, colonne) and absentSurBloc(chiffre, grille, ligne, colonne)):
            grille[ligne][colonne] = chiffre
            if estValide(grille, position+1):
                return True
            grille[ligne][colonne] = 0
    return False



def resoudre_sudoku(grille):
    """
    :param grille: grille que l'on veut résoudre
    :return: grille complétée si une solution valide est trouvée, None sinon
    """
    if estValide(grille, 0):
        return grille
    else:
        return None



def ihm_sudoku():
    """
    :return: affichage de la grille résolue si une solution valide est trouvée
    """
    # On récupère les chiffres saisis par l'utilisateur:
    grille = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            if value.isdigit():
                row.append(int(value))
                entries[i][j].config(font=Font(weight="bold"))
            else:
                row.append(0)
        grille.append(row)

    # On résout le sudoku de l'utilisateur:
    solution = resoudre_sudoku(grille)

    # Si une solution est trouvée, on l'affiche dans la grille remplie par l'utilisateur:
    if solution:
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(solution[i][j]))
    else:
        print("Aucune solution trouvée.")


def reset_sudoku():
    """
    :return: grille réinitialisée, vide
    """
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, "")


# Création de la fenêtre d'affichage:
window = tk.Tk()
window.title("Résolveur sudoku")


# Affichage des instructions dans l'ihm:
instruction1 = tk.Label(window, text="Reportez les chiffres de votre sudoku dans la grille ci-dessous,")
instruction1.grid(row=0, columnspan=9)
instruction2 = tk.Label(window, text="puis cliquez sur 'Résoudre'.")
instruction2.grid(row=1, columnspan=9)
espace = tk.Label(window, text="")
espace.grid(row=2, columnspan=9)
espace2 = tk.Label(window, text="")
espace2.grid(row=12, columnspan=9)


# Création de la grille à remplir:
grid_frame = tk.Frame(window, bd=1, relief=tk.SOLID)
grid_frame.grid(row=3, column=0, padx=60)
panels = []
for i in range(3):
    blocs = []
    for j in range(3):
        panel = tk.PanedWindow(grid_frame)
        panel.grid(row=i+3, column=j, padx=3, pady=3)
        entries = []
        for r in range(3):
            row = []
            for c in range(3):
                entry = tk.Entry(panel, width=2)
                entry.grid(row=r, column=c)
                row.append(entry)
            entries.append(row)
        blocs.append(panel)
    panels.append(blocs)


"""
# Création des cases d'entrée formant la grille:
entries = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(window, width=2)
        entry.grid(row=i+3, column=j)
        row.append(entry)
    entries.append(row)
"""

#Création du cadre (invisible) des boutons pour les juxstaposer:
button_frame = tk.Frame(window)
button_frame.grid(row=13, column=0, columnspan=3, pady=(10, 0))


# Création du bouton d'affichage de la solution:
solve_button = tk.Button(button_frame, text="Résoudre", command=ihm_sudoku)
solve_button.grid(row=13, column=0, padx=20)


# Création du bouton de réinitialisation:
image = Image.open("reset.png")
image = image.resize((25, 25), Image.Resampling.LANCZOS)
img_retaillee = ImageTk.PhotoImage(image)
reset_button = tk.Button(button_frame, image=img_retaillee, command=reset_sudoku)
reset_button.grid(row=13, column=1, padx=20)


# Lancement de l'ihm:
window.mainloop()