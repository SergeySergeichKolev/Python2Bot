# pip install bs4, lxml
from bs4 import BeautifulSoup


#открыть файл в нужной кодировке
file = open("сайт.html", encoding="utf-8")

#прочитываю файл
rfile = file.read()

#разобранный сайт
soup = BeautifulSoup(rfile, "lxml")

#забрать код элемента по классу
title = soup.select_one(".title")
price = soup.select_one(".price")

#get_text - забрать внутренность кода

print(title.get_text())
print(price.get_text())