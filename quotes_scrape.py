import requests 
from bs4 import BeautifulSoup
from csv import writer
# from time import sleep


authors_list = []
# authors_list = [{"name":"" ,"quote":"" ,"link":"" }]
home_page = "http://quotes.toscrape.com/" 
pages = "/page/1/"


while pages: 
    response = requests.get(f"{home_page}{pages}")
    print(f"Now Scraping {home_page}{pages}...")
    my_soup = BeautifulSoup(response.text, "html.parser")
    spoon = my_soup.find_all(class_="quote")
    # authors_quotes are in a class "text"
    # authors are in a class "author"
    # links are in an a tag

    # I need to loop and then append the scapes
    for index in spoon:
    
        authors_list.append({
            "quote": index.find(class_="text").get_text(),
            "name": index.find(class_="author").get_text(),
            "link": index.find("a")["href"]
        })

    # Multiple pages 
    next_button = my_soup.find(class_="next")
    pages = next_button.find("a")["href"] if next_button else None
    # sleep(1)


print(authors_list)





      