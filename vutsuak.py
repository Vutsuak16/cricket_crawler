import requests
from bs4 import BeautifulSoup
import urllib

crawl_links = []
links = []
country = ['1', '2', '3', '4', '5', '6', '7', '8', '25', '9']
redundant = ['Remember me', 'Regulars', 'Highlights', 'Opinion', '/', '\n']
ct = 0


def spider():
    try:

        url = "http://www.espncricinfo.com/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):
            try:
                href = "www.espncricinfo.com" + link.get('href')

                if href not in links:
                    links.append(href)
            except:
                continue
        return links
    except:
        print "Connection error"


Url = spider()
index = []
url = ""


def get_player():
    for i in Url:
        if "player" in i:
            index.append(Url.index(i))
            url = Url[index[0]]
            url = "http://" + url
            return url


passer = get_player()
player_links = []

data = []


def Vutsuak_spider(html, Name):
    x = passer

    source_code = requests.get(html)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for link in soup.findAll('a'):

        global ct
        href = "www.espncricinfo.com" + link.get('href')
        if '.html' in href:
            try:
                if Name in link.string:
                    player_links.append("http://" + href)
                    if not (href is None):
                        return "http://" + href
                else:

                    cricketer = x + "?country={0}".format(country[ct])
                    ct += 1
                    Vutsuak_spider(cricketer, Name)
            except:
                continue


def imp_funct(player):
    Link = Vutsuak_spider(passer, player)
    try:
        if Link is not None:
            print Link, "1"
            spider2(Link)
        else:
            print player_links[0], "2"
            spider2(player_links[0])
    except:
        print "player not found", "3"


def spider2(L):
    source_code = requests.get(L)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    co=0

    for link in soup.findAll('a'):
        try:
                if 1 > 0:
                    if '#' in link.get('href'):
                        crawl_links.append(L + link.get('href'))
                        print crawl_links[co]
                        co+=1
                    else:
                        crawl_links.append("http://www.espncricinfo.com" + link.get('href'))
                        print crawl_links[co]
                        co += 1
        except:
            break

    for link in soup.findAll('span'):
        try:

            if 'Batting and fielding averages' in link.string:
                break
            if link.string is not None and not (link.string in redundant):
                data.append(link.string)

        except:
            continue
    st = ""
    print "The player profile is :"
    for text in soup.find_all('p', {'class': 'ciPlayerprofiletext1'}):
        if text.string is not None:
            st = st + text.string
    data.append(st)

    for Image in soup.find_all('img'):

        if 'src' in str(Image) and 'inline' in str(Image):
            part = ""
            counter = 0
            x = str(Image)
            try:
                for i in x:
                    counter += 1
                    if i == "/":
                        while 1 > 0:
                            part += x[counter - 1]
                            counter += 1
                            if i == "1":
                                break
                        break
            except:

                break
    part2 = ""
    for i in part:
        if i == " ":
            break
        part2 += i

    for images in soup.find_all('a', {'class': 'wallpaperbrowsultext'}):
        if images.string == 'Photos':
            img_url = "http://www.espncricinfo.com" + images.get('href')
            print img_url
            source_code2 = requests.get(img_url)
            plain_text2 = source_code2.text
            soup2 = BeautifulSoup(plain_text2)
            img_number = 1
            for photos in soup2.find_all('img'):
                if '.jpg' in photos.get('src'):
                    # print "http://www.espncricinfo.com" + photos.get('src')
                    urllib.urlretrieve(("http://www.espncricinfo.com" + photos.get('src')),
                                       ("/home/kaustuv/Desktop/IMAGES/player{0}.jpg").format(img_number))
                    img_number += 1

    image = "http://www.espncricinfo.com" + part2[:-1]
    # print image
    urllib.urlretrieve(image, "/home/kaustuv/Desktop/IMAGES/player.jpg")

LIST=[data,crawl_links]
def retdata():
    return LIST



