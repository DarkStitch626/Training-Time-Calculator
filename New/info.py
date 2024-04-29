from Semesters import Semester

class Info:
    _instance = None  # Class attribute that holds the singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Info, cls).__new__(cls)
            # Initialize the instance here (only happens the first time)
        return cls._instance
    
    def __init__(self):
        self.semester = None

    def set_semester(self, degree_var, semester_var, root):
        print("hello")
        self.semester = Semester(degree_var, semester_var, root)