from abc import ABC
from glob import glob
import os


class SearchImageModel(ABC):

    @classmethod
    def find(cls, path):
        if os.path.exists(path):
            print("folder is found")
            path_list = list(glob(os.path.join(path, "*.jpg")))
            path_list += list(glob(os.path.join(path, "*.png")))
            print(path_list)
            return path_list
        else:
            print("ERROR")
            return None
