import os
import os.path

# UI文件所在的路径
dirname = './'

# 列出目录下的所有UI文件


def listUiFile():
    List = []
    files = os.listdir(dirname)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            List.append(filename)
    return List


def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'


def runMain():
    List = listUiFile()
    for uifile in List:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(
            pyfile=pyfile, uifile=uifile)
        os.system(cmd)


if __name__ == '__main__':
    runMain()
