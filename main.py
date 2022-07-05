from zipfile import ZipFile
import os


class Epub:
    def __init__(self, filename=None, filepath=None):
        if filename is None:
            self.filename = 'untitled.epub'
        elif filename.endswith('.epub'):
            self.filename = filename
        else:
            self.filename = filename

        self.filepath = filepath if filepath else os.getcwd()
    
    @classmethod
    def create(self, filepath=None):
        epub = ZipFile(f'{self.filepath}//{self.filename}', 'w')

        if filepath is None:
            pass
        else:
            # 如果filepath不为空，获取其中的所有文件，将其写入到epub文档中
            pass


if __name__ == "__main__":
    epub = Epub('Test')
    epub.create()
