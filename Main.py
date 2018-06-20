import Problem as p
import pandas as pd

# df = pd.read_csv('./Data/problem1.csv')
# print(df)

s = p.Sudoku('./Data/problem2.csv')
s.show_table()
s.solve()
s.show_table()
s.show_table_cand_size()

