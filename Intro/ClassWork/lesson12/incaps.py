class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self._get_w_h()

    def _get_w_h(self):  # '_' means internal method (not for user)
        self.w = self.x1 - self.x0
        self.h = self.y1 - self.y0

    def get_area(self):
        return self.w * self.h

    def __str__(self):  # shows class as a string
        return f"(x0={self.x0} y0={self.y0}); (x1={self.x1} y1={self.y1})"

    def __repr__(self):  # shows class as a string in some object
        return f"{self.x0, self.y1, self.x1, self.y1}"

    def __add__(self, other):
        return Bbox(min(self.x0, other.x0),
                    min(self.y0, other.y0),
                    max(self.x1, other.x1),
                    max(self.y1, other.y1))


# bbox_1 = Bbox(0, 0, 2, 3)
# bbox_2 = Bbox(1, 2, 3, 4)
# print(bbox_1.w, bbox_1.h)
# print(bbox_1.get_area())
# print(bbox_1)
# bbox_list = [bbox_1, bbox_2]
# print(bbox_list)
# print("----")
#
# bbox_3 = bbox_1 + bbox_2
# print(bbox_3)

import os


class PathInfo:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.folders = []
        self._get_list_dit()

    def _get_list_dit(self):
        path_list_dir = os.listdir(self.path)
        for item in path_list_dir:
            path_item = os.path.join(self.path, item)
            if os.path.isfile(path_item):
                self.files.append(item)
            else:
                self.folders.append(item)

    def show_files(self):
        return self.files

    def show_folders(self):
        return self.folders

    def __repr__(self):
        return f"Files: {self.files}\n Folders: {self.folders}"


path = os.curdir
path_info = PathInfo(path)
print(path_info)

print(path_info.files)
