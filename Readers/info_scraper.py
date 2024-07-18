from bs4 import BeautifulSoup
import requests
import re
import time
import os
import sys
sys.path.append(os.path.abspath('../../'))
from Objects import term as t

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

def format_dates(date):
    month_mapping = {
        "Jan.": "01",
        "Feb.": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "Aug.": "08",
        "Sept.": "09",
        "Oct.": "10",
        "Nov.": "11",
        "Dec.": "12"
    }
    
    # line = date.split()
    # date = str(line[0]) + str(line[1])
    # return date.strip()

    line = date.split()
    month = month_mapping.get(line[0], "Unknown")
    
    return f"{month}{str(line[1])}".strip(" ")

def get_index(degree, semester):
    id = ['Summer 2024', 'collapse319650', 'collapse319662', 'collapse319663',
      'collapse319664', 'collapse319665']
    


    return id

def search_by_semester(degree, semester):
    
    term_list = []

    # index = get_index(degree, semester)

    url = 'https://uwf.edu/academic-affairs/departments/military-veteran-resource-center/tuition--funding/training-time-requirements-for-va-benefits/'
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    print("html retrieved")

    body = soup.find('main', id='main-content')

    # pattern = re.compile(f'{semester.capitalize()}.*{degree.title()}')
    # pattern = re.compile(rf'{re.escape(semester.capitalize())}.*?{re.escape(degree.title())}', re.DOTALL)
    # caption = body.find('caption', text=lambda text: text and semester.capitalize() in text and degree.title() in text)

    # # caption = body.find('caption', text=re.compile(pattern))

    # tbody = caption.find_next_sibling('tbody')

    # div = body.find('div', id=id[index])

    # tbody = div.find('tbody')

    start_time = time.time()
    # Use lambda function to match caption text
    caption = body.find('caption', text=lambda text: text and semester.capitalize() in text and degree.title() in text)
    if not caption:
        print("No matching caption found")
        return term_list, 0

    # Find the next sibling tbody
    tbody = caption.find_next_sibling('tbody')
    if not tbody:
        print("No tbody found after caption")
        return term_list, 0

    terms = list(tbody.find_all('tr'))

    for term in terms:
        line = term.find('th').get_text()
        FT = int(term.find('td').get_text())
        print(f"FT: {FT}")

        term_number = line[:(line.find(" "))]
        line = line[(line.find("(")+1):-1]
        dates = line.split("-")
        start_date = format_dates(dates[0])
        end_date = format_dates(dates[1])

        print(f"Start - {start_date} ; End - {end_date}")

        new_term = t.Term(term_number, FT, start_date, end_date)

        term_list.append(new_term)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return term_list, len(term_list)


def main():
    url = 'https://uwf.edu/academic-affairs/departments/military-veteran-resource-center/tuition--funding/training-time-requirements-for-va-benefits/'
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    body = soup.find('main', id='main-content')

    charts = list(body.find_all('td'))

    terms = ['Summer1', 'Summer2', 'Summer3', 'Summer4', 'Summer10', 'Summer90', 'Summer96', '2Summer1', '2Summer2', '2Summer3', '2Summer4', '2Summer10', '2Summer90', '2Summer96', 'Fall1', 'Fall2', 'Fall3', 'Fall91', 'Fall92', 'Fall1', 'Fall2', 'Fall3', 'Fall91', 'Fall92', 'Spring1', 'Spring2', 'Spring3', 'Spring91', 'Spring92', '2Spring1', '2Spring2', '2Spring3', 'Spring91', 'Spring92']

    i = 0

    for term in terms:
        print(term)
        print("Full time:" + charts[i].get_text())
        print()
        i += 3

if __name__ == "__main__":
    main()