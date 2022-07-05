from error import *


class AddBasicFile:

    def writeBasicFile(self, epub):
        epub.writestr('mimetype', f'../templates/mimetype')
        epub.writestr('META-INF/container.xml', f'../templates/container.xml')

    @classmethod
    def create(self, epub=None, output=False):
        if epub is None:
            raise EpubError
        else:
            self.writeBasicFile(epub)

        if output == False:
            print("基础文件已写入")


if __name__ == "__main__":
    add = AddBasicFile()
