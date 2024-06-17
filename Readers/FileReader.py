import os
import sys
sys.path.append(os.path.abspath('../../'))
from Objects import term as t

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

def read_file(chosen_degree, chosen_semester):
    Terms = []
    i = 0
    needed_file = f"{chosen_degree}_{chosen_semester}"
    filename = resource_path(f"..\\Textfiles\\{needed_file}")
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == "":
                break

            parts = line.strip().split(' ')
            if len(parts) == 4:
                try:
                    nums = list(map(int, parts))
                    Term = t.Term(*nums)
                    Terms.append(Term)
                    i += 1
                except ValueError:
                    print("You broke something idoit")
    return Terms, i