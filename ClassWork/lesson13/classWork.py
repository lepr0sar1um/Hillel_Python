import random


class My_15:
    def __init__(self):
        self.my_15 = self._create_start_position()
        self.row, self.col = self._get_empty_cell()

    def __repr__(self):
        return "\n".join(['\t'.join(row) for row in self.my_15])

    def _get_empty_cell(self):
        row = 0
        col = 0
        for row_index, tmp_row in enumerate(self.my_15):
            for col_index, tmp_col in enumerate(tmp_row):
                if tmp_col == '':
                    return row_index, col_index
        return row, col

    def _create_start_position(self):
        my_15 = []
        all_values = [str(i) for i in range(1, 16)] + ['']
        random.shuffle(all_values)
        for row_number in range(4):
            my_15.append(all_values[4 * row_number: 4 * (row_number + 1)])
        return my_15

    def move_down(self):
        if self.row == 3:
            return
        self.my_15[self.row][self.col], self.my_15[self.row + 1][self.col] = self.my_15[self.row + 1], \
                                                                             self.my_15[self.col]

        self.row += 1


my_15 = My_15()
print(my_15)
print()
print(my_15.row, my_15.col)
