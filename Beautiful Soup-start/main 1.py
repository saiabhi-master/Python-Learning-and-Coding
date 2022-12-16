from bs4 import BeautifulSoup

import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
titles_list = [title.getText() for title in all_titles]
print(titles_list)

# for n in range(len(titles_list) - 1, -1, -1):
#     print(titles_list[n])
# (OR)

titles = titles_list[::-1]

with open("title.txt", mode="w") as file:
    for movie in titles:
        file.write(f"{movie}\n")






