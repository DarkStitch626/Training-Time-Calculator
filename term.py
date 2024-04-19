class Term:
    def __init__(self, term_number, FT, TQT, HT, QT, start_date, end_date):
        self.term_number = term_number
        self.FT = FT    # Full time
        self.TQT = TQT    # Half Three-quarter time
        self.HT = HT     # Half time
        self.QT = QT     # Quarter time
        self.start_date = start_date
        self.end_date = end_date

    def _calculate_training_time(self, enrolled_credits):
        if enrolled_credits == 0:
            return 0
        current_percentage = (enrolled_credits / self.FT)
        if current_percentage < 1:
            return current_percentage
        else:
            return 1
        
    def _get_start_date(self):
        return self.start_date
    
    def _get_end_date(self):
        return self.end_date
        