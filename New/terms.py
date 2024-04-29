import tkinter as tk

class Term:
    def __init__(self, term_number, FT, start_date, end_date, master):
        self.name = None
        self._set_name(term_number)

        self.FT = FT
        self.start_date = start_date
        self.end_date = end_date

        self.num_signal = tk.StringVar()
        self.num_signal.trace_add('write', self._update_num)
        self.num = None
        self.lbl = tk.Label(master, text=self.name)
        self.textbox = tk.Entry(master, textvariable=self.num_signal)

    def _set_name(self, number):
        self.name = f"Term {number}"

    def _update_num(self):
        var = self.num_signal.get()
        try:
            self.num = int(var) if var else 0
        except ValueError:
            self.num = 0

    def display_widgets(self, row):
        self.lbl.grid(row=row, column=0, padx=10, pady=5)
        self.textbox.grid(row=row, column=1, padx=10, pady=5)

    def format_date(self, chosen_date):
        date = self.start_date if chosen_date == 'start' else self.end_date
        if len(str(date)) <= 4:
            date_str = str(date)
            date_str = date_str.zfill(4)
            return (date_str[:2] + '/' + date_str[2:])

    def calculate_training_time(self, enrolled_credits):
        if enrolled_credits == 0:
            return 0
        current_percentage = (enrolled_credits / self.FT)
        if current_percentage < 1:
            return current_percentage
        else:
            return 1
        
    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date
        