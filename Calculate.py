import term as t
from Semester import Semester

class Calculate:
    def __init__(self, chosen_degree_type, chosen_semester, widgets):
        self.chosen_degree_type = chosen_degree_type
        self.chosen_semester = chosen_semester
        self.widgets = widgets
        self.semester = self.get_semester_info()
        self.term_percentages = {}

    def get_semester_info(self):
        return Semester(self.read_file(3,7), 5, "Spring") if self.chosen_semester == 'Spring' else \
                   Semester(self.read_file(11,15), 5, "Fall") if self.chosen_semester == 'Fall' else \
                   Semester(self.read_file(19,25), 7, "Summer")


    def read_file(self, start_line, end_line):
        Terms = []
        filename = 'Undergrad.txt' if self.chosen_degree_type == "Undergraduate" else 'Graduate.txt'
        with open(filename, 'r') as file:
            for current_line_number, line in enumerate(file, start=1):
                if current_line_number >= start_line and current_line_number <= end_line:
                    # Split the line into components and convert them to integers
                    parts = line.strip().split(' ')
                    # Ensure that there are exactly four numbers in the line
                    if len(parts) == 6:
                        nums = list(map(int, parts))
                        # Create an instance of Tmp with these numbers
                        Term = t.Term(*nums)
                        Terms.append(Term)
                elif current_line_number > end_line:
                    break  # Stop reading if end line is surpassed
        return Terms

    def calculate_term_percentages(self):
        for i, (term, widget) in enumerate(self.widgets.items()):
            widget_str = widget.get()
            if widget_str == "":
                self.term_percentages[term] = 0
            else:
                self.term_percentages[term] = float(widget_str) / self.semester.terms[i].FT

    def calculate_calculated_times(self):
        if self.check_for_full_time() == 1:
            return 'full-time'
        elif self.check_for_full_time() == 2:
            return (self.semester.terms[1].end_date, self.semester.terms[2].start_date)
        
        return self.check_changing_dates()

    def check_for_full_time(self):

        if self.term_percentages['1'] == 1:
            return 1
        if (self.term_percentages['1'] + self.term_percentages['91'] >= 1) and \
            (self.term_percentages['1'] + self.term_percentages['3'] >= 1):
                return 1
        if (self.term_percentages['1'] + self.term_percentages['2'] >= 1) and \
            (self.term_percentages['1'] + self.term_percentages['92'] >= 1):
                return 1
        # if (self.term_percentages['91'] + self.term_percentages['3'] >= 1):
        #     return 1
        # if (self.term_percentages['2'] + self.term_percentages['92'] >= 1):
        #     return 1
        # if (self.term_percentages['91'] + self.term_percentages['92'] >= 1):
        #     return 1
        if (self.term_percentages['2'] + self.term_percentages['3'] >= 1):
            return 2

    def check_changing_dates(self):
        if self.chosen_semester != "Summer":
            changing_dates = [f"{self.semester.terms[0].start_date}", f"{self.semester.terms[4].start_date}", f"{self.semester.terms[1].end_date}", f"{self.semester.terms[2].start_date}", f"{self.semester.terms[3].end_date}"]
            calculated_times = {}
            training_times = {}
            calculated_times[changing_dates[0]] = (self.term_percentages['1'] + self.term_percentages['2'] + self.term_percentages['91'])
            calculated_times[changing_dates[1]] = (self.term_percentages['1'] + self.term_percentages['2'] + self.term_percentages['91'] + self.term_percentages['92'])
            calculated_times[changing_dates[2]] = (self.term_percentages['1'] + self.term_percentages['91'] + self.term_percentages['92'])
            calculated_times[changing_dates[3]] = (self.term_percentages['1'] + self.term_percentages['3'] + self.term_percentages['91'] + self.term_percentages['92'])
            calculated_times[changing_dates[4]] = (self.term_percentages['1'] + self.term_percentages['3'] + self.term_percentages['92'])

            for date in sorted(changing_dates):
                if calculated_times[date] > 1:
                   calculated_times[date] = 1 

            previous_time = None

            for time in calculated_times.values():
                print(time)

            for date in sorted(changing_dates):
                current_time = calculated_times[date]
                if current_time != previous_time:
                    training_times[date] = current_time
                    previous_time = current_time

            # for time in training_times.values():
            #     print(time)

            for date, time in training_times.items():
                if time >= 1:
                    training_times[date] = "full-time"
                elif time >= 0.75:
                    training_times[date] = "3/4-time"
                elif time >= 0.5:
                    training_times[date] = "half-time"
                elif time >= 0.25:
                    training_times[date] = "quarter-time"
                else:
                    training_times[date] = "less than quarter-time"

            # for value in training_times.values():
            #     print(value)
            return training_times
        
    def get_end_date(self):
        return str(self.semester.terms[self.semester.number_of_terms - 1].end_date)