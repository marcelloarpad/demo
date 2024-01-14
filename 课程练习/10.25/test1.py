from bs4 import BeautifulSoup
import re
file = open("test.html", "rb")
text = file.read()
soup = BeautifulSoup(text, "html.parser")
#print(soup)
'''soup_name = soup.find_all("a", attrs={"class":"mnav"})
for i in soup_name:
    print(i.string)
'''
soup_a = soup.findAll(re.compile("a"))
print(soup_a)