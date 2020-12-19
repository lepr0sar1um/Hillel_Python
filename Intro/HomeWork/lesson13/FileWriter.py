import random
import string

import pandas as pd


class FileWriter:
    def __init__(self, file_name_path: str, file_data=None):
        self.file_name_path = file_name_path
        self.mode = self.file_name_path.rsplit(".")[-1]
        if not file_data:
            if self.mode == "txt":
                self.file_data = self.__random_string()
            elif self.mode == "json":
                self.file_data = self.__random_dict()
            elif self.mode == "csv":
                self.file_data = self.__random_list()
            else:
                raise Exception("Unsupported file format!")
        else:
            self.file_data = file_data
        print(self.file_data)

    def __random_string(self, min_length=100, max_length=1000, for_dict=False):
        if for_dict:
            return ''.join(random.choice(string.ascii_lowercase) for _ in
                           range(random.randint(max_length, max_length)))
        else:
            return ''.join(random.choice(string.ascii_lowercase + ' ' + ',' + '.' + string.ascii_uppercase) for _ in
                           range(random.randint(min_length, max_length)))

    def __random_dict(self):
        return {self.__random_string(min_length=5, max_length=5, for_dict=True): random.randint(-100, 100) for _ in
                range(5, 20)}

    def __random_list(self, rows=5, cols=5):
        return [[random.randint(0, 1) for i in range(cols)] for j in range(rows)]

    def write(self):
        mode = self.mode
        if mode == "txt":
            data = pd.Series(self.file_data)
            data.to_csv(path_or_buf=self.file_name_path, sep=' ', index=False, header=False)
        elif mode == "json":
            data = pd.Series(self.file_data)
            data.to_json(path_or_buf=self.file_name_path)
        elif mode == "csv":
            data = pd.DataFrame(self.file_data)
            data.to_csv(path_or_buf=self.file_name_path, sep=',', index=False, header=False)
