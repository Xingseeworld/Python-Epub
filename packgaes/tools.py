from error import *
import os.path as op
from os import getcwd


class Tools:
    def file_create(self):
        pass

    @file_create
    @classmethod
    def ifFilepath(self, filepath, new=False):

        # 判断filepath是否存在，以及路径是否正确
        # 不判断传入的路径是否存在
        if filepath is None:
            return getcwd()

        elif not op.isdir(filepath):
            raise PathError(
                f'" {filepath} " is not a legal path')

        # 判断是相对还是绝对路径
        if op.isabs(filepath):
            return filepath

        elif op.isabs(op.abspath(filepath)):
            return op.abspath(filepath)


if __name__ == "__main__":
    print(Tools.ifFilepath('file.exe'))
