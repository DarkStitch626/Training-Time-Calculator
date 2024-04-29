import tkinter as tk
from GUIs import GUI
from info import Info

def build_semester(info, root, degree_var = None, semester_var = None):
    if degree_var and semester_var:
        info.set_semester(degree_var, semester_var, root)

def main():
    root = tk.Tk()
    gui = GUI(root)

    info = Info()

    degree_var = tk.StringVar()
    semester_var = tk.StringVar()
    semester_var.trace_add('write', build_semester(info, root, degree_var.get(), semester_var.get()))
    gui.build_option_frame(degree_var, semester_var)
    gui.run()

main()