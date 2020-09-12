import os


def ui_2_py(ui_file_name):
    py_file = ui_file_name.split(".")[0] + ".py"
    cmd = f"pyuic5 -o {py_file} {ui_file_name}"
    os.system(cmd)


if __name__ == "__main__":
    ui_2_py("untitled.ui")
