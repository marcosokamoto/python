from bs4 import BeautifulSoup


import requests

# Objeto site recebendo o conteudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content

# Objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

# Transforma html em string e o print vai exibir  html
print(soup.prettify())