from bs4 import BeautifulSoup
import requests

id = ['collapse319649', 'collapse319650', 'collapse319662', 'collapse319663',
      'collapse319664', 'collapse319665']

def format_dates(date_string):
    pass

def search_by_semester(index):
    url = 'https://uwf.edu/academic-affairs/departments/military-veteran-resource-center/tuition--funding/training-time-requirements-for-va-benefits/'
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    body = soup.find('main', id='main-content')

    table = body.find('div', class_='table-responsive')

    tbody = table.find('tbody')

    for child in tbody.children:
        pass

    





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