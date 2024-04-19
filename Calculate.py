import term as t
from Semester import Semester
import sys
import os

class Calculate:
    def __init__(self, chosen_degree_type, chosen_semester, widgets):
        self.chosen_degree_type = chosen_degree_type
        self.chosen_semester = chosen_semester
        self.terms = self.get_terms(widgets)
        self.semester = self.get_semester_info()
        self.term_percentages = {}
        self.dates = []

    def get_semester_info(self):
        return Semester(self.read_file(3,7), 5, "Spring") if self.chosen_semester == 'Spring' else \
                   Semester(self.read_file(11,15), 5, "Fall") if self.chosen_semester == 'Fall' else \
                   Semester(self.read_file(19,25), 7, "Summer")

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def read_file(self, start_line, end_line):
        Terms = []
        filename = self.resource_path('Undergrad.txt') if self.chosen_degree_type == "Undergraduate" else self.resource_path('Graduate.txt')
        with open(filename, 'r') as file:
            for current_line_number, line in enumerate(file, start=1):
                if current_line_number >= start_line and current_line_number <= end_line:
                    # Split the line into components and convert them to integers
                    parts = line.strip().split(' ')
                    # Ensure that there are exactly four numbers in the line
                    if len(parts) == 7:
                        nums = list(map(int, parts))
                        # Create an instance of Tmp with these numbers
                        Term = t.Term(*nums)
                        Terms.append(Term)
                elif current_line_number > end_line:
                    break  # Stop reading if end line is surpassed
        return Terms

    def get_terms(self, widgets):
        terms = {}
        for term, widget in widgets.items():
            widget_str = widget.get()
            if widget_str != "":
                terms[term] = widget_str

        return terms

    def calculate_term_percentages(self):
        for term1, credits in self.terms.items():
            for i, term2 in enumerate(self.semester.terms):
                if term1 == str(term2.term_number):
                    required_credits = term2.FT
                    self.term_percentages[term1] = int(credits) / required_credits

    def calculate_calculated_times(self):
        self.dates = []

        # Shortcut for full-time
        if '1' in self.term_percentages and len(self.term_percentages) == 1 and self.term_percentages['1'] == 1:
            return 'full-time'

        # Collect all start and end dates
        for term in self.semester.terms:
            if str(term.term_number) in self.term_percentages:
                self.dates.extend([term.start_date, term.end_date])

        # Remove duplicates and sort dates
        self.dates = sorted(set(self.dates))

        calculated_terms = {}
        # Iterate over the sorted dates
        for i, date in enumerate(self.dates):
            # Don't process the last date yet
            if i == len(self.dates) - 1:
                break
            
            tmp = []
            next_date = self.dates[i + 1]

            # For each term, check if it's active between date and next_date
            for term in self.semester.terms:
                if str(term.term_number) in self.term_percentages:
                    # Check if the current term is active in this date range
                    if term.start_date <= date and term.end_date >= next_date:
                        tmp.append(self.term_percentages[str(term.term_number)])

            # Sum the percentages in tmp and cap it at 1
            calculated_terms[date] = min(sum(tmp), 1)

        # Now categorize each calculated term into time categories
        for date, time in calculated_terms.items():
            if time >= 1:
                calculated_terms[date] = "full-time"
            elif time >= 0.75:
                calculated_terms[date] = "3/4-time"
            elif time >= 0.5:
                calculated_terms[date] = "half-time"
            elif time >= 0.25:
                calculated_terms[date] = "quarter-time"
            else:
                calculated_terms[date] = "less than quarter-time"

        # Process the last date range if needed
        last_date = self.dates[-1]
        tmp = []
        for term in self.semester.terms:
            if term.end_date == last_date and str(term.term_number) in self.term_percentages:
                tmp.append(self.term_percentages[str(term.term_number)])

        # If there are no terms ending on the last date, assume training continues at the last known rate
        if not tmp and calculated_terms:
            tmp.append(calculated_terms[self.dates[-2]])

        # Sum the percentages in tmp for the last date and cap it at 1
        calculated_terms[last_date] = min(sum(tmp), 1)
        
        # Categorize the last date into time categories
        time = calculated_terms[last_date]
        if time >= 1:
            calculated_terms[last_date] = "full-time"
        elif time >= 0.75:
            calculated_terms[last_date] = "3/4-time"
        elif time >= 0.5:
            calculated_terms[last_date] = "half-time"
        elif time >= 0.25:
            calculated_terms[last_date] = "quarter-time"
        else:
            calculated_terms[last_date] = "less than quarter-time"

        return calculated_terms
        
    def get_end_date(self):
        return str(self.semester.terms[self.semester.number_of_terms - 1].end_date)
    
    def get_dates(self):
        return self.dates