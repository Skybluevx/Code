import os
import os.path


def ui_2_py(ui_file_name):
    file_names = os.listdir("./")

    if ui_file_name not in file_names:
        print("文件名错误或文件不存在，请重新检查！")
        return

    abs_ui_file_path = os.path.abspath(ui_file_name)
    py_file = ui_file_name.split(".")[0] + ".py"
    cmd = f"pyuic5 -o {py_file} {ui_file_name}"
    os.system(cmd)


if __name__ == "__main__":
    ui_2_py("untitled.ui")
