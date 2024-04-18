import term as t
import Semester as s
from GUI import GUI


def read_file(start_line, end_line):
    Terms = []
    with open('Undergrad.txt', 'r') as file:
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

Spring = s.Semester(read_file(3,7), 5)
Fall = s.Semester(read_file(11,15), 5)
Summer = s.Semester(read_file(19,25), 7)

gui = GUI()
GUI.run()