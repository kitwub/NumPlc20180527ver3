import Problem as p
import pandas as pd

df = pd.read_csv('./Data/problem1.csv')
print(df)

s = p.Sudoku()
s.show_table()

