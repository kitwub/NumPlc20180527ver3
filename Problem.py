class Sudoku:
    # test constant
    __zerosTable = [[i * 10 + j for j in range(1, 10)] for i in range(1, 10)]

    # fields
    __update_set = {}

    def __init__(self, input_num=__zerosTable):
        # pass
        self.table = input_num
        self.candidates = [[{i for i in range(1, 10, 1)}] * 9] * 9

    def show_table(self):
        # print(self.table)
        print('')
        for elm_row in self.table:
            for elm in elm_row:
                if elm == 0:
                    print('  ', end='')
                else:
                    print(str(elm) + ' ', end='')
            else:
                print('')
        print('')

    def solve(self):
        pass

    def __update_cand(self, tuple_rc):
        self.__update_cand_column(tuple_rc)
        self.__update_cand_row(tuple_rc)
        self.__update_cand_square(tuple_rc)

    def __update_cand_column(self, tuple_rc):

        pass

    def __update_cand_row(self, tuple_rc):
        pass

    def __update_cand_square(self, tuple_rc):
        pass
