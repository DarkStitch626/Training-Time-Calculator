import tkinter as tk
from tkinter import ttk
import Semester as s

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Training Time Calculator")
        self.root.geometry("600x400")
        self.left_frame = tk.Frame(self.root)
        self.right_frame = tk.Frame(self.root)
        self.textboxes = {}
        self.lbls = []
        self.semester_var = tk.StringVar(self.root)
        self.degree_box = ttk.Combobox(self.left_frame)
        self.semester_box = ttk.Combobox(self.left_frame)

        self.create_dropdowns()
        

    def create_dropdowns(self):
        self.left_frame.pack(side="left", fill="y", expand=False, padx=10, pady=20)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=20)

        degree_lbl = tk.Label(self.left_frame, width='20', text="Degree Type")
        degree_lbl.grid(row=0, column=0, padx=0, pady=10)

        self.degree_box.configure(state='readonly', height='20')
        self.degree_box['values'] = ('Undergraduate', 'Graduate')
        self.degree_box.grid(row=0, column=1, padx=10, pady=10)

        semester_lbl = tk.Label(self.left_frame, width='20', text="Semester")
        semester_lbl.grid(row=1, column=0, padx=0, pady=10)

        self.semester_box.configure(textvariable=self.semester_var, state='readonly', height='20')
        self.semester_box['values'] = ('Spring', 'Fall', 'Summer')
        self.semester_box.grid(row=1, column=1, padx=10, pady=10)
        self.semester_var.trace_add('write', self.create_textboxes)

    def create_textboxes(self, *args):
        number = 7 if self.semester_box.get() == 'Summer' else 5
        
        if number == 7:
            terms = ["Term 1", "Term 2", "Term 3", "Term 4", "Term 10", "Term 90", "Term 96"]
        else:
            terms = ["Term 1", "Term 2", "Term 3", "Term 91", "Term 92"]
        
        for textbox in self.textboxes.values():
            textbox.destroy()
        for lbl in self.lbls:
            lbl.destroy()
        self.textboxes = {}
        self.lbls = []

        # Create an Entry for each term
        for i, term in enumerate(terms):
            term_number = term.split()[-1]  # This gets the number after "Term"
            self.lbls.append(tk.Label(self.right_frame, text=f"Term {term_number}"))
            self.lbls[i].grid(row=i, column=0, padx=10, pady=5)
            self.textboxes[term_number] = tk.Entry(self.right_frame)
            self.textboxes[term_number].grid(row=i, column=1, padx=10, pady=5)

    def run(self):
        self.root.mainloop()

gui = GUI()
gui.run()