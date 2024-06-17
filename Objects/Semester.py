class Semester:
    def __init__(self):
        self.terms = None
        self.number_of_terms = None

    def set_terms(self, terms):
        self.terms = terms

    def set_number_of_terms(self, number_of_terms):
        self.number_of_terms = number_of_terms

    def get_terms(self):
        return self.terms

    def get_number_of_terms(self):
        return self.number_of_terms