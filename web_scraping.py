import requests
from bs4 import BeautifulSoup
from requests.models import Response
URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

def  get_citations_needed_count(URL):
    lst = []
    page = requests.get(URL)
# print(page.content)
    content = BeautifulSoup(page.content, "html.parser") # read it with 
    # print(content)
    span = content.find_all('span')
    for i in span:
        if i.text == "citation needed":
            lst.append(i)
    return len(lst)
def get_citations_needed_report(URL):
    lst = []
    page = requests.get(URL)
# print(page.content)
    content = BeautifulSoup(page.content, "html.parser") # read it with 
    parg = content.find_all('p')
    for i in parg:
        if i.findChildren('span', recursive  = True):
            lst.append(i.text)
    return lst



if __name__ == '__main__':
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))

