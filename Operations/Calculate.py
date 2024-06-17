class Calculate():
    def __init__(self):
        self.term_percentages = {}
        self.dates = []
        self.calculated_terms = {}
        self.c = 0

    def set_values(self, credits, terms):
        for (key, value) in credits.items():
            for term in terms:
                if term.get_name() == key:
                    self.term_percentages[key] = ((int(value)) / term.get_full_time())
                    self.dates.extend([term.get_start_date(), term.get_end_date()])
                    break

        self.dates = sorted(set(self.dates))

    def calculate_training_times3(self, terms):
        self.calculated_terms = {}
        current_terms = {}
        first = True

        for i, date in enumerate(self.dates):
            removed_term = None
            added_term = None
            
            for term, credits in self.term_percentages.items():
                operation = self.find_terms(date, term, terms)
                if operation == 'add' and term not in current_terms:
                    current_terms[term] = credits
                    added_term = term
                elif operation == 'remove' and term in current_terms:
                    current_terms.pop(term, None)
                    removed_term = term

            combined_training_time = min(sum(current_terms.values()), 1.0)

            if first:
                self.calculated_terms['beginning'] = combined_training_time
                first = False
            elif i == (len(self.dates) - 1):
                break
            else:
                if added_term:
                    self.calculated_terms[added_term] = combined_training_time
                elif removed_term:
                    self.calculated_terms[removed_term] = combined_training_time

        return self.calculated_terms



    
    def find_terms(self, date, current_term, terms):
        for term in terms:
            if (term.get_name() == current_term):
                if (date == term.get_start_date()):
                    return 'add'
                if (date == term.get_end_date()):
                    return 'remove'
        return 'ignore'

    def calculate_training_times(self, terms):

        if 'Term 1' in self.term_percentages and self.term_percentages['Term 1'] == 1:
            return 'full-time'

        calculated_terms = {}
        for i, date in enumerate(self.dates):
            if i == len(self.dates) - 1:
                break
            
            tmp = []
            next_date = self.dates[i + 1]

            for key, percentage in self.term_percentages.items():
                start_date, end_date = self._get_term_dates_by_key(key, terms)
                if start_date <= date and end_date >= next_date:
                    tmp.append(percentage)

            calculated_terms[date] = min(sum(tmp), 1)

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


        last_date = self.dates[-1]
        tmp = []
        for key, percentage in self.term_percentages.items():
            _, end_date = self._get_term_dates_by_key(key, terms)
            if end_date == last_date:
                tmp.append(percentage)

        if not tmp and calculated_terms:
            tmp.append(calculated_terms[self.dates[-2]])

        calculated_terms[last_date] = min(sum(tmp), 1)
        
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
    
    def _get_term_dates_by_key(self, key, terms):
        for term in terms:
            if key == term.get_name():
                return term.get_start_date(), term.get_end_date()