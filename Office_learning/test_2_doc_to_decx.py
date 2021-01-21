"""
    将 doc 文件转换为 docx 文件
"""
import os
from win32com import client


def doc_docx():
    pass


def docx_doc():
    file_path = r"E:\QQ\我的数据\1372755472\FileRecv"
    files = []
    for file in os.listdir(file_path):
        if file.endswith(".docx"):
            files.append(file_path + file)

    word = client.gencache.EnsureDispatch("Word.Application")
    for file in files:
        file_path, file_ext = os.path.splitext(file)
        docx = word.Documents.Open(file)
        docx.ActiveDocument.SaveAs(file_path + ".doc")
        docx.ActiveDocument.close()
        word.Quit()
    
    print("保存完成！")


def main():
    docx_doc()


if __name__ == '__main__':
    main()
