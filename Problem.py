# coding: utf-8
# Your code here!
import pandas as pd


class Sudoku:
    table = [[i * 10 + j for j in range(1, 10)] for i in range(1, 10)]

    # test constant
    __zeros_table = [[i * 10 + j for j in range(1, 10)] for i in range(1, 10)]

    # fields
    # __update_set = {}
    __update_tuples = []

    def __init__(self, init_value):
        # self.table = input_value
        table = self.__zeros_table
        df = pd.read_csv(init_value)

        ctr = 0
        for elm in df.values.flatten():
            row = ctr // 9
            clm = ctr % 9

            if elm != 0:
                # self.__update_tuples.append((elm,row,clm))
                self.__append_update_tuple((elm, row, clm))

            self.table[row][clm] = elm

            ctr += 1

        # self.__candidates = [[{i for i in range(1, 10, 1)}] * 9] * 9
        self.__candidates = [[{i for i in range(1, 10, 1)} for i in range(1, 10)] for j in range(1, 10)]

    def debug(self):
        print('debug start')

        # self.show_table()
        print(self.__candidates)

        print('debug end')

    def show_table(self):
        # print(self.table)
        print('')
        # print('-' * ((9+2)*2-1))
        ctr_row = 0
        for elm_row in self.table:
            if ctr_row % 3 == 0:
                print('-' * ((9 + 2) * 2 - 1))

            ctr_clm = 0

            for elm in elm_row:
                if ctr_clm == 3 or ctr_clm == 6:
                    print('| ', end='')
                if elm == 0:
                    print('  ', end='')
                else:
                    print(str(elm) + ' ', end='')
                ctr_clm += 1
            else:
                print('')

            ctr_row += 1

        print('-' * ((9 + 2) * 2 - 1))
        print('')

    def show_table_cand_size(self):
        # print(self.table)
        print('')
        # print('-' * ((9+2)*2-1))
        ctr_row = 0
        for elm_row in self.table:
            if ctr_row % 3 == 0:
                print('-' * ((9 + 2) * 2 - 1))

            ctr_clm = 0

            for elm in elm_row:
                if ctr_clm == 3 or ctr_clm == 6:
                    print('| ', end='')

                if elm == 0:
                    # print('  ', end='')
                    print(str(len(self.__candidates[ctr_row][ctr_clm])) + ' ', end='')
                else:
                    # print(str(elm) + ' ', end='')
                    print(str(len(self.__candidates[ctr_row][ctr_clm])) + ' ', end='')
                ctr_clm += 1

            else:
                print('')

            ctr_row += 1

        print('-' * ((9 + 2) * 2 - 1))
        print('')

    def solve(self):
        ctr_for_avoid_inifite_loop = 0
        while self.__update_tuples:

            ctr_for_avoid_inifite_loop += 1
            if ctr_for_avoid_inifite_loop > 100:
                print('infinite loop')
                exit()

            self.__update_cand(self.__update_tuples.pop(0))
        else:
            print('No candidate is left.')

    def __append_update_tuple(self, update_tuple):
        self.__update_tuples.append(update_tuple)

    def __update_cand(self, tuple_val_row_clm):
        self.__update_cand_single(tuple_val_row_clm)
        self.__update_cand_column(tuple_val_row_clm)
        self.__update_cand_row(tuple_val_row_clm)
        self.__update_cand_square(tuple_val_row_clm)

    def __update_cand_single(self, in_tuple):
        self.__candidates[in_tuple[1]][in_tuple[2]].clear()
        # self.__exclude_cand(in_tuple)

    def __update_cand_column(self, in_tuple):
        for row in range(0, 9, 1):
            # print('row:{0}'.format(row))
            if row != in_tuple[1]:
                self.__exclude_cand((in_tuple[0], row, in_tuple[2]))
        pass

    def __update_cand_row(self, in_tuple):
        for clm in range(0, 9, 1):
            # print('clm:{0}'.format(clm))
            if clm != in_tuple[2]:
                self.__exclude_cand((in_tuple[0], in_tuple[1], clm))
        pass

    def __update_cand_square(self, in_tuple):
        for row in range(0, 9, 1):
            for clm in range(0, 9, 1):

                if (row // 3 == in_tuple[1] // 3) and (clm // 3 == in_tuple[2] // 3):
                    if not ((row == in_tuple[1]) or (clm == in_tuple[2])):
                        self.__exclude_cand((in_tuple[0], row, clm))
        pass

    def __exclude_cand(self, in_tuple):
        if len(self.__candidates[in_tuple[1]][in_tuple[2]]) == 0:
            pass

        print('excule:', end='')
        print(self.__candidates[in_tuple[1]][in_tuple[2]], end='')
        print(in_tuple)

        if in_tuple[0] in self.__candidates[in_tuple[1]][in_tuple[2]]:
            self.__candidates[in_tuple[1]][in_tuple[2]].remove(in_tuple[0])

            print('result:', end='')
            print(self.__candidates[in_tuple[1]][in_tuple[2]])

            self.__is_last_cand_and_append_updates(in_tuple[1:3])

    def __is_last_cand_and_append_updates(self, in_tuple_rc):
        # print('last?',end='')
        # print(in_tuple_rc)

        num_cand = len(self.__candidates[in_tuple_rc[0]][in_tuple_rc[1]])
        if num_cand == 1:
            determined_val = self.__candidates[in_tuple_rc[0]][in_tuple_rc[1]].pop()
            self.table[in_tuple_rc[0]][in_tuple_rc[1]] = determined_val
            self.__append_update_tuple((determined_val, in_tuple_rc[0], in_tuple_rc[1]))

            print(str(determined_val) + str(in_tuple_rc))
            self.show_table()

        elif num_cand == 0:
            pass
