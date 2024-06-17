import sys
import os
sys.path.append(os.path.abspath('../../'))

from Objects import Semester as S
from Readers import FileReader as FR
from Operations import FormatOutput as ftt

class Controller():
    def __init__(self, calculate):
        self.semester = S.Semester()
        self.calculate = calculate
        self.degree_var = None
        self.semester_var = None
        self.credits = None
        self.calculated_terms = None
        self.output = None

    def build_semester(self):
        terms, number_of_terms = FR.read_file(self.degree_var.get(), self.semester_var.get())
        self.semester.set_terms(terms)
        self.semester.set_number_of_terms(number_of_terms)

    def get_number_of_semester_terms(self):
        return self.semester.get_number_of_terms()
    
    def get_semester_terms(self):
        return self.semester.get_terms()

    def set_degree_var(self, degree_var):
        self.degree_var = degree_var

    def set_semester_var(self, semester_var):
        self.semester_var = semester_var
    
    def set_credits(self, credits):
        self.credits = credits

    def get_degree_var(self):
        return self.degree_var

    def get_semester_var(self):
        return self.semester_var
    
    def get_credits(self):
        terms = self.get_semester_terms()
        given_credits = {}
        for i, credit in enumerate(self.credits):
            if credit.get() != "":
                given_credits[terms[i].get_name()] = credit.get()

        return given_credits
    
    def get_output(self):
        return self.output
    
    def begin_calculations(self):
        given_credits = self.get_credits()
        if (len(given_credits) != 0):
            self.calculate.set_values(given_credits, self.get_semester_terms())
            self.calculated_terms = self.calculate.calculate_training_times3(self.get_semester_terms())
            print(f"Console - {self.calculated_terms}")
            self.output = ftt.format_training_time(self.calculated_terms)
            print(self.output)

        else:
            print("No credits given")
    