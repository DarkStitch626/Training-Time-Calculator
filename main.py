from Operations import Calculate as cal
from Operations import Controller as con
from Objects import Window as win
import tkinter as tk

def main():
    root = tk.Tk()

    calculate = cal.Calculate()
    controller = con.Controller(calculate)
    window = win.Window(root, controller)

    window.run()

main()