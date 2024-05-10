import copy


def solve_sudoku(grille: list):
    solution = copy.deepcopy(grille)
    if estValide(solution, 0):
        return solution
    else:
        return None


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


def estValide(grille, position):
    if position == 81:
        return True
    ligne = position // 9
    colonne = position % 9
    if grille[ligne][colonne] != 0:
        return estValide(grille, position + 1)
    for chiffre in range(1, 10):
        if (absentSurLigne(chiffre, grille, ligne)
                and absentSurColonne(chiffre, grille, colonne)
                and absentSurBloc(chiffre, grille, ligne, colonne)):
            grille[ligne][colonne] = chiffre
            if estValide(grille, position + 1):
                return True
            grille[ligne][colonne] = 0
    return False