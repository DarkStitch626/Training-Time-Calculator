import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frames = {"left_frame": None, "right_frame": None, "submit_frame": None, "answer_frame": None}
        self.values = []

        self.controller.set_degree_var(tk.StringVar())
        self.controller.set_semester_var(tk.StringVar())
        self.controller.set_credits(self.values)

        self._construct_window()

    def _construct_window(self):
        self.root.title("Training Time Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self._build_initial_frames()

    def _build_initial_frames(self):
        self.frames[0] = tk.Frame(self.root, width=380, height=400, bg='red')
        self.frames[1] = tk.Frame(self.root, width=220, height=400, bg='green')
        self.frames[2] = tk.Frame(self.root, width=500, height=100,bg='blue')
        self.frames[3] = tk.Frame(self.root, width=600, height=500, bg='purple')

        self.frames[0].grid(row=0, column=0, sticky="nsew")
        self.frames[1].grid(row=0, column=1, sticky="nsew")
        self.frames[2].grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.frames[0].grid_propagate(False)
        self.frames[1].grid_propagate(False)
        self.frames[2].grid_propagate(False)
        self.frames[2].grid_rowconfigure(0, weight=1)
        self.frames[2].grid_columnconfigure(0, weight=1)
        self.frames[2].grid_columnconfigure(1, weight=0)

        self._build_option_frame()

    def _build_option_frame(self):
        degree_lbl = tk.Label(self.frames[0], width='20', text="Degree Type")
        semester_lbl = tk.Label(self.frames[0], width='20', text="Semester")
        degree_box = ttk.Combobox(self.frames[0])
        semester_box = ttk.Combobox(self.frames[0])

        degree_box.configure(textvariable=self.controller.get_degree_var(), state='readonly', height='20')
        self.controller.get_degree_var().set('Undergrad')
        degree_box['values'] = ('Undergrad', 'Graduate')

        semester_box.configure(textvariable=self.controller.get_semester_var(), state='readonly', height='20')
        semester_box['values'] = ('Spring', 'Fall', 'Summer')
        self.controller.get_semester_var().trace_add('write', lambda *args: self._build_entry_frame())

        degree_lbl.grid(row=0, column=0, padx=20, pady=10)
        semester_lbl.grid(row=1, column=0, padx=0, pady=10)
        degree_box.grid(row=0, column=1, padx=10, pady=10)
        semester_box.grid(row=1, column=1, padx=10, pady=10)

        self._build_button_frame()

    def _build_entry_frame(self):

        for widget in self.frames[1].grid_slaves():
            widget.grid_remove()
        
        self.values.clear()

        self.controller.build_semester()
        for i, term in enumerate(self.controller.get_semester_terms()):
            lbl = tk.Label(self.frames[1], text=term.get_name())
            self.values.append(tk.StringVar())
            textbox = tk.Entry(self.frames[1], textvariable=self.values[i])
            lbl.grid(row=(i+1), column=0, padx=10, pady=5)
            textbox.grid(row=(i+1), column=1, padx=10, pady=5)

    def _build_button_frame(self):
        btn = tk.Button(self.frames[2], text="Calculate", command=self.get_calculation, width=20, height=2)
        btn.grid(row=0, column=1, padx=(0, 20))

    def _build_answer_frame(self):
        output = self.controller.get_output()

        lbl = tk.Label(self.frames[3], text=output, wraplength=500, justify='left')
        lbl.grid(row=0, column=0, padx=10, pady=10)

    def get_calculation(self):
        self.controller.begin_calculations()
    

    def build_window(self, temp):
        if temp == 0:
            self.frames[3].grid_forget()
            
            self.frames[0].grid(row=0, column=0, sticky="nsew")
            self.frames[1].grid(row=0, column=1, sticky="nsew")
            self.frames[2].grid(row=1, column=0, columnspan=2, sticky="nsew")
            self.frames[0].grid_propagate(False)
            self.frames[1].grid_propagate(False)
            self.frames[2].grid_propagate(False)
            self.frames[2].grid_rowconfigure(0, weight=1)
            self.frames[2].grid_columnconfigure(0, weight=1)
            self.frames[2].grid_columnconfigure(1, weight=0)
        else:
            self.frames[0].grid_forget()
            self.frames[1].grid_forget()
            self.frames[2].grid_forget()

            self.frames[3].grid(row=0, column=0, sticky="nsew")
            self.frames[3].grid_propagate(False)
            self.frames[3].grid_rowconfigure(0, weight=1)
            self.frames[3].grid_columnconfigure(0, weight=1)
            self.frames[3].grid_columnconfigure(1, weight=0)

    def run(self):
        self.root.mainloop()