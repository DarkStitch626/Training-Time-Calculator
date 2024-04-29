import tkinter as tk
from tkinter import ttk

class GUI:

    def __init__(self, root):
        self.root = root
        self.frames = {"left_frame": None, "right_frame": None, "submit_frame": None, "answer_frame": None}
        self._construct_window()

    def _construct_window(self):
        self.root.title("Training Time Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self._build_initial_frames()

    def _build_initial_frames(self):
        self.frames[1] = tk.Frame(self.root, width=220, height=400, bg='green')
        self.frames[0] = tk.Frame(self.root, width=380, height=400, bg='red')
        self.frames[2] = tk.Frame(self.root, width=500, height=100,bg='blue')

        self.frames[0].grid(row=0, column=0, sticky="nsew")
        self.frames[1].grid(row=0, column=1, sticky="nsew")
        self.frames[2].grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.frames[0].grid_propagate(False)
        self.frames[1].grid_propagate(False)
        self.frames[2].grid_propagate(False)
        self.frames[2].grid_rowconfigure(0, weight=1)
        self.frames[2].grid_columnconfigure(0, weight=1)
        self.frames[2].grid_columnconfigure(1, weight=0)

    def build_option_frame(self, degree_var, semester_var):
        degree_lbl = tk.Label(self.frames[0], width='20', text="Degree Type")
        semester_lbl = tk.Label(self.frames[0], width='20', text="Semester")
        degree_box = ttk.Combobox(self.frames[0])
        semester_box = ttk.Combobox(self.frames[0])

        degree_box.configure(textvariable=degree_var, state='readonly', height='20')
        degree_box['values'] = ('Undergrad', 'Graduate')

        semester_box.configure(textvariable=semester_var, state='readonly', height='20')
        semester_box['values'] = ('Spring', 'Fall', 'Summer')

        degree_lbl.grid(row=0, column=0, padx=20, pady=10)
        semester_lbl.grid(row=1, column=0, padx=0, pady=10)
        degree_box.grid(row=0, column=1, padx=10, pady=10)
        semester_box.grid(row=1, column=1, padx=10, pady=10)

    def run(self):
        self.root.mainloop()