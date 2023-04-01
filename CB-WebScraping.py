import requests
import bs4
import lxml

base_url = 'http://quotes.toscrape.com/page/{}/'

authors = set()

n=1

while True:

    scrape_url = base_url.format(n)
    
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    
    if "No quotes found!" in soup.select(".col-md-8")[1].text:
        break
    else:
        authors_list = soup.select(".author")
    
        for auth in authors_list:
            authors = authors.union(set(auth.contents))
            #authors.add(auth.text)
        n+=1

print(authors)