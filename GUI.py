import tkinter as tk
from tkinter import ttk
from Calculate import Calculate

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Training Time Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.left_frame = tk.Frame(self.root, width=380, height=400, bg='red')
        self.right_frame = tk.Frame(self.root, width=220, height=400, bg='green')
        self.submit_frame = tk.Frame(self.root, width=500, height=100,bg='blue')
        self.answer_frame = tk.Frame(self.root, width=600, height=500, bg='purple')
        self.answer_widgets = []
        self.lbls = []
        self.textboxes = {}
        self.degree_var = tk.StringVar(self.root)
        self.semester_var = tk.StringVar(self.root)
        self.degree_box = ttk.Combobox(self.left_frame)
        self.semester_box = ttk.Combobox(self.left_frame)

        self.initialize_window()
        self.create_widgets()
        

    def initialize_window(self):
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.submit_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.left_frame.grid_propagate(False)
        self.right_frame.grid_propagate(False)
        self.submit_frame.grid_propagate(False)
        self.submit_frame.grid_rowconfigure(0, weight=1)
        self.submit_frame.grid_columnconfigure(0, weight=1)
        self.submit_frame.grid_columnconfigure(1, weight=0)

    def create_widgets(self):
        degree_lbl = tk.Label(self.left_frame, width='20', text="Degree Type")
        degree_lbl.grid(row=0, column=0, padx=20, pady=10)

        self.degree_box.configure(textvariable=self.degree_var, state='readonly', height='20')
        self.degree_box['values'] = ('Undergraduate', 'Graduate')
        self.degree_box.grid(row=0, column=1, padx=10, pady=10)

        semester_lbl = tk.Label(self.left_frame, width='20', text="Semester")
        semester_lbl.grid(row=1, column=0, padx=0, pady=10)

        self.semester_box.configure(textvariable=self.semester_var, state='readonly', height='20')
        self.semester_box['values'] = ('Spring', 'Fall', 'Summer')
        self.semester_box.grid(row=1, column=1, padx=10, pady=10)
        self.semester_var.trace_add('write', self.create_textboxes)

        btn = tk.Button(self.submit_frame, text="Calculate", command=self.calculate, width=20, height=2)
        btn.grid(row=0, column=1, padx=(0, 20))

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

    def calculate(self):
        self.left_frame.grid_forget()
        self.right_frame.grid_forget()
        self.submit_frame.grid_forget()

        self.answer_frame.grid(row=0, column=0, sticky="nsew")
        self.answer_frame.grid_propagate(False)
        self.answer_frame.grid_rowconfigure(0, weight=1)
        self.answer_frame.grid_columnconfigure(0, weight=1)
        self.answer_frame.grid_columnconfigure(1, weight=0)

        self.answer_widgets.append(tk.Button(self.answer_frame, text="Back", command=self.main_screen, width=20, height=2))
        self.answer_widgets[0].grid(row=1, column=1, padx=(0, 20), pady=(0,20), sticky='se')

        Info = Calculate(self.degree_var.get(), self.semester_var.get(), self.textboxes)
        Info.calculate_term_percentages()
        result = Info.calculate_calculated_times()
        if result == 'full-time':
            self.answer_widgets.append(tk.Label(self.answer_frame, text="You are full-time for the entire semester"))
            self.answer_widgets[1].grid(row=0, column=0, columnspan=2, padx=(0, 20), pady=(0,20))
        if isinstance(result, tuple):
            # formatted_dates = self.date_format(result)
            self.answer_widgets.append(tk.Label(self.answer_frame, text=f"You are full-time for the entire semester except between {self.format_date(result[0])} and {self.format_date(result[1])}"))
            self.answer_widgets[1].grid(row=0, column=0, columnspan=2, padx=(0, 20), pady=(0,20))
        if isinstance(result, dict):
            # formatted_dates = self.date_format(result.keys())
            # for date in formatted_dates:
            #     print(date)
            sorted_dates = sorted(result)
            schedule_parts = []

            for i, date in enumerate(sorted_dates[:-1]):  # Go up to the second-to-last item
                current_status = result[date]
                next_date = sorted_dates[i + 1]
                schedule_parts.append(f"You will be {current_status} between {self.format_date(date)} and {self.format_date(next_date)}.")

            # Handle the last date range if needed
            if sorted_dates:
                last_date = sorted_dates[-1]
                last_status = result[last_date]
                end_date = Info.get_end_date()
                schedule_parts.append(f"You will be {last_status} between {self.format_date(last_date)} and {self.format_date(end_date)}.")

            # Combine all parts into one schedule string
            full_schedule = "\n".join(schedule_parts)
            self.answer_widgets.append(tk.Label(self.answer_frame, text=full_schedule))
            self.answer_widgets[1].grid(row=0, column=0, columnspan=2, padx=(0, 20), pady=(0,20))

    def format_date(self, date):
        if len(date) <= 4:
            date_str = str(date)
            date_str = date_str.zfill(4)
            return (date_str[:2] + '/' + date_str[2:])

    def main_screen(self):
        self.answer_frame.grid_forget()
        for widget in self.answer_widgets:
            widget.destroy()
        self.answer_widgets = []
        self.initialize_window()

gui = GUI()
gui.run()