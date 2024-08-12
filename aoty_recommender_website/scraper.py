import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


class AotyScraper:

    def search_albums(self, album_name):
        opener = AppURLopener()
        encoded_string = urllib.parse.quote_plus(album_name)
        url = f"https://www.albumoftheyear.org/search/albums/?q={encoded_string}"
        print(url)
        page = opener.open(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        album_blocks = soup.find_all("div", {"class": "albumBlock"})
        images = []
        for album in album_blocks:
            image = album.find("img")
            if image:
                images.append(image["data-src"])
        return images
