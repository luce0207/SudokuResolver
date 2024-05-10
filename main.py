import tkinter as tk    # Bibliothèque qui permettra de créer l'ihm du programme
from tkinter.font import Font   # Module permettant d'afficher du texte en gras dans l'ihm
from PIL import ImageTk, Image   # Modules permettant d'afficher des images danns l'ihm
from tkinter.messagebox import *


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
    for j in grille[ligne]:
        if j == chiffre:
            return False
    return True



def absentSurColonne(chiffre, grille, colonne):
    for i in range(9):
        if grille[i][colonne] == chiffre:
            return False
    return True



def absentSurBloc(chiffre, grille, ligne, colonne):
    ligneBloc = ligne - (ligne % 3)
    colonneBloc = colonne - (colonne % 3)
    for i in range(ligneBloc, ligneBloc + 3):
        for j in range(colonneBloc, colonneBloc + 3):
            if grille[i][j] == chiffre:
                return False
    return True



def is_valid(grille, position):
    if position == 81:
        return True
    ligne = position // 9
    colonne = position % 9
    if grille[ligne][colonne] != 0:
        return is_valid(grille, position+1)
    for chiffre in range(1,10):
        if (absentSurLigne(chiffre, grille, ligne) and absentSurColonne(chiffre, grille, colonne) and absentSurBloc(chiffre, grille, ligne, colonne)):
            grille[ligne][colonne] = chiffre
            if is_valid(grille, position+1):
                return True
            grille[ligne][colonne] = 0
    return False



def solve_sudoku(grille):
    if is_valid(grille, 0):
        return grille
    else:
        return None



def display_solution():
    # On récupère les chiffres saisis par l'utilisateur:
    grille = []
    for row_index in range(9):
        row = []
        for col_index in range(9):
            value = cases[row_index][col_index].get()
            if value.isdigit():
                row.append(int(value))
                cases[row_index][col_index].config(font=Font(weight="bold"))
            else:
                row.append(0)
        grille.append(row)

    # On résout le sudoku de l'utilisateur:
    solution = solve_sudoku(grille)

    # Si une solution est trouvée, on l'affiche dans la grille remplie par l'utilisateur:
    if solution:
        for row in range(9):
            for col in range(9):
                cases[row][col].delete(0, tk.END)
                cases[row][col].insert(0, solution[row][col])
    else:
        showerror(title="Grille invalide", message="Aucune solution n'a été trouvée pour votre sudoku")


def set_default():
    entries = [[0, 1, 0, 2, 3, 4, 0, 0, 0],
               [3, 0, 0, 5, 0, 6, 0, 1, 0],
               [7, 0, 0, 8, 0, 0, 6, 0, 2],
               [2, 0, 9, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 0, 0, 0, 0, 4],
               [0, 7, 0, 0, 0, 0, 3, 0, 9],
               [4, 0, 6, 0, 0, 2, 0, 0, 7],
               [0, 5, 0, 1, 0, 8, 0, 0, 3],
               [0, 0, 0, 4, 9, 7, 0, 8, 0]]
    for row in range(9):
        for col in range(9):
            cases[row][col].delete(0, tk.END)
            cases[row][col].insert(entries[row][col], entries[row][col] if entries[row][col] != 0 else "")


def reset_sudoku():
    for row in range(9):
        for col in range(9):
            cases[row][col].delete(0, tk.END)
            cases[row][col].insert(0, "")
            cases[row][col].config(font=Font(weight="normal"))


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
cases =[]
grid_frame = tk.Frame(window, bd=1, relief=tk.SOLID)
grid_frame.grid(row=3, column=0, padx=60)
for bloc_line_index in range(3):
    bloc_line_frame = tk.Frame(grid_frame)
    bloc_line_frame.grid(row=bloc_line_index, column=0)
    cases.append([])
    cases.append([])
    cases.append([])
    for bloc_column_index in range(3):
        bloc_column_frame = tk.Frame(bloc_line_frame, bd=1, relief=tk.SOLID)
        bloc_column_frame.grid(row=0, column=bloc_column_index)
        for i in range(3):
            for j in range(3):
                entry = tk.Entry(bloc_column_frame, width=2)
                entry.grid(row=i, column=j)
                cases[bloc_line_index*3+i].append(entry)


#Création du cadre (invisible) des boutons pour les juxstaposer:
button_frame = tk.Frame(window)
button_frame.grid(row=13, column=0, columnspan=3, pady=(10, 0))


# Création du bouton d'affichage de la solution:
solve_button = tk.Button(button_frame, text="Résoudre", command=display_solution)
solve_button.grid(row=13, column=0, padx=20)


# Création du bouton de réinitialisation:
image = Image.open("reset.png")
image = image.resize((25, 25), Image.Resampling.LANCZOS)
img_retaillee = ImageTk.PhotoImage(image)
reset_button = tk.Button(button_frame, image=img_retaillee, command=reset_sudoku)
reset_button.grid(row=13, column=1, padx=20)

set_default()

# Lancement de l'ihm:
window.mainloop()