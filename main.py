from bs4 import BeautifulSoup
import requests

date = input("which year do you want to travel to? type the date in this format YYYY-MM-DD: ")


response = requests.get("https://www.billboard.com/charts/hot-100/" + date + "/")
# response = requests.get("https://www.billboard.com/charts/hot-100/2017-01-01/")
music = response.text
soup = BeautifulSoup(music, "html.parser")
musics = soup.find_all(name="h3", class_="a-no-trucate")
all_musics = []

for song in musics:
    a = song.getText().replace('\n', '').replace('\t', '')
    all_musics.append(a)

# for n in range(len(all_musics)):
#     print(musics)

print(all_musics)
