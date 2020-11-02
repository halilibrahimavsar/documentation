import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

url = "https://biopharmguy.com/links/states-all-geo.php"

links = []
names = []

def check_url(url):
    pure_links = []

    response = requests.get(url)
    soup = bs(response.content, "lxml")
    categories = soup.find("div", "categories")

    
    for i in categories.find_all("a"):
        pure_links.append(i.get('href'))
        names.append(i.get_text())
    
    for i in pure_links:
        full_url = urljoin(response.url, i)
        links.append(full_url)
    
    print(links)
    print(names)


check_url(url)


def open_sub_url(sub_name, sub_url):
    resp =  requests.get(sub_url)
    soup = bs(resp.content, "lxml")
    for i in soup.find_all("tr"):
        name = i.get_text()
        print("NAMEEE ::::::: ", name)




open_sub_url(names[0], links[0])

