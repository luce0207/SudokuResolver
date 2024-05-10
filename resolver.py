import copy


def solve_sudoku(grille: list):
    solution = copy.deepcopy(grille)
    if estValide(solution, 0):
        return solution
    else:
        return None


def occurrencesSurLigne(chiffre, grille, ligne):
    nb_occ = 0
    for j in grille[ligne]:
        if j == chiffre:
            nb_occ += 1
    return nb_occ


def occurrencesSurColonne(chiffre, grille, colonne):
    nb_occ = 0
    for i in range(9):
        if grille[i][colonne] == chiffre:
            nb_occ += 1
    return nb_occ


def occurrencesSurBloc(chiffre, grille, ligne, colonne):
    nb_occ = 0
    ligneBloc = ligne - (ligne % 3)
    colonneBloc = colonne - (colonne % 3)
    for i in range(ligneBloc, ligneBloc + 3):
        for j in range(colonneBloc, colonneBloc + 3):
            if grille[i][j] == chiffre:
                nb_occ += 1
    return nb_occ


def estValide(grille, position) -> bool:
    if position == 81:
        return True
    ligne = position // 9
    colonne = position % 9
    if grille[ligne][colonne] != 0:  # check Validity of this element
        chiffre = grille[ligne][colonne]
        return estValide(grille, position + 1) \
            and occurrencesSurLigne(chiffre, grille, ligne) == 1 \
            and occurrencesSurColonne(chiffre, grille, colonne) == 1 \
            and occurrencesSurBloc(chiffre, grille, ligne, colonne) == 1
    for chiffre in range(1, 10):
        if occurrencesSurLigne(chiffre, grille, ligne) == 0 \
                and occurrencesSurColonne(chiffre, grille, colonne) == 0 \
                and occurrencesSurBloc(chiffre, grille, ligne, colonne) == 0:
            grille[ligne][colonne] = chiffre
            if estValide(grille, position + 1):
                return True
            grille[ligne][colonne] = 0
    return False
