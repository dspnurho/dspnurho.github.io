from bs4 import BeautifulSoup
soup = BeautifulSoup('index.html', 'html.parser')
print(soup.prettify())
