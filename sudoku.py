import tkinter as tk
from tkinter.font import Font
from tkinter.messagebox import *
from resolver import solve_sudoku


class Sudoku(object):
    def __init__(self):
        self.window = None
        self.cases = None

    def display_window(self):
        self.__create_window()
        self.__create_header()
        self.__create_grid()
        self.__create_footer()

        self.set_default()
        self.window.mainloop()

    def __create_window(self):
        self.window = tk.Tk()
        self.window.title("Résolveur sudoku")

    def __create_header(self):
        instruction1 = tk.Label(self.window, text="Reportez les chiffres de votre sudoku dans la grille ci-dessous,")
        instruction1.grid(row=0)
        instruction2 = tk.Label(self.window, text="puis cliquez sur 'Résoudre'.")
        instruction2.grid(row=1)
        espace = tk.Label(self.window, text="")
        espace.grid(row=2)

    def __create_grid(self):
        self.cases = []
        grid_frame = tk.Frame(self.window, bd=1, relief=tk.SOLID)
        grid_frame.grid(row=3)
        for bloc_line_index in range(3):
            bloc_line_frame = tk.Frame(grid_frame)
            bloc_line_frame.grid(row=bloc_line_index, column=0)
            self.cases.append([])
            self.cases.append([])
            self.cases.append([])
            for bloc_column_index in range(3):
                bloc_column_frame = tk.Frame(bloc_line_frame, bd=1, relief=tk.SOLID)
                bloc_column_frame.grid(row=0, column=bloc_column_index)
                for i in range(3):
                    for j in range(3):
                        entry = tk.Entry(bloc_column_frame, width=2)
                        entry.grid(row=i, column=j)
                        self.cases[bloc_line_index * 3 + i].append(entry)

    def __create_footer(self):
        espace2 = tk.Label(self.window, text="")
        espace2.grid(row=4)

        button_frame = tk.Frame(self.window)
        button_frame.grid(row=5)

        solve_button = tk.Button(button_frame, text="Résoudre", command=self.__display_solution)
        solve_button.grid(row=0, column=0, padx=20)

        reset_button = tk.Button(button_frame, text="Nouvelle grille", command=self.__reset_sudoku)
        reset_button.grid(row=0, column=1, padx=20)

        fill_default_button = tk.Button(button_frame, text="Grille exemple", command=self.set_default)
        fill_default_button.grid(row=0, column=2, padx=20)

    def __display_solution(self):
        grille = self.__extract_values()
        solution = solve_sudoku(grille)
        self.__fill_solution(grille, solution)

    def __fill_solution(self, grille, solution):
        if solution:
            self.__fill(solution)
            for row_index in range(9):
                for col_index in range(9):
                    if grille[row_index][col_index] != 0:
                        self.cases[row_index][col_index].config(font=Font(weight="bold"))
        else:
            showerror(title="Grille invalide", message="Aucune solution n'a été trouvée pour votre sudoku")

    def __extract_values(self):
        grille = []
        for row_index in range(9):
            row = []
            for col_index in range(9):
                value = self.cases[row_index][col_index].get()
                if value.isdigit():
                    row.append(int(value))
                    self.cases[row_index][col_index].config(font=Font(weight="bold"))
                else:
                    row.append(0)
            grille.append(row)
        return grille

    def set_default(self):
        entries = [[0, 1, 0, 2, 3, 4, 0, 0, 0],
                   [3, 0, 0, 5, 0, 6, 0, 1, 0],
                   [7, 0, 0, 8, 0, 0, 6, 0, 2],
                   [2, 0, 9, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 0, 0, 0, 0, 4],
                   [0, 7, 0, 0, 0, 0, 3, 0, 9],
                   [4, 0, 6, 0, 0, 2, 0, 0, 7],
                   [0, 5, 0, 1, 0, 8, 0, 0, 3],
                   [0, 0, 0, 4, 9, 7, 0, 8, 0]]
        self.__fill(entries)

    def __reset_sudoku(self):
        self.__fill()

    def __fill(self, entries=None):
        for row in range(9):
            for col in range(9):
                self.cases[row][col].delete(0, tk.END)
                if entries is None:
                    self.cases[row][col].insert(0, "")
                else:
                    self.cases[row][col].insert(entries[row][col], entries[row][col] if entries[row][col] != 0 else "")
                self.cases[row][col].config(font=Font(weight="normal"))