from Semester import Semester
import tkinter as tk

root = tk.Tk()
semester = Semester("Undergrad", "Fall", root)

print(semester.terms[0].get_start_date())
print(semester.terms[0].format_date("start"))
