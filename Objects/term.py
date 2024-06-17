import tkinter as tk

class Term:
    def __init__(self, term_number, FT, start_date, end_date):
        self.name = None
        self._set_name(term_number)     # Set the name of the term

        self.FT = FT                    # Store the full-time requirement for the term
        self.start_date = start_date    # Store the term's start date
        self.end_date = end_date        # Store the term's end date

    def _set_name(self, number):
        self.name = f"Term {number}"

    def get_formatted_date(self, chosen_date):
        date = self.start_date if chosen_date == 'start' else self.end_date
        if len(str(date)) <= 4:
            date_str = str(date)
            date_str = date_str.zfill(4)
            return (date_str[:2] + '/' + date_str[2:])
        
    def get_name(self):
        return self.name

    def get_full_time(self):
        return self.FT
        
    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date