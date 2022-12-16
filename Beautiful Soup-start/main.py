from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)  #prints title tag
# print(soup.title.string)  #prints what is contained
# print(soup.prettify()) #prints entire thing with indentation
# print(soup.a) prints first anchor tag
# print(soup.find_all(name="a")) prints all anchor tags refrs in a list

#to get only text contained:

# for tag in soup.find_all(name="a"):
#     print(tag.getText())


#------------------------

#to get certain attributes:

# for tag in soup.find_all(name="a"):
#     print(tag.get("href"))

# being exact:
# heading = soup.find(name="h1", id="name")
# print(heading)   for class, use class_

#--------------------------
#looking for an a tag INSIDE a p tag
#select one looks for the first one
# company_url = soup.select_one(selector="p a")
# soup.select_one("#name")
# soup.select(".heading") -- List
