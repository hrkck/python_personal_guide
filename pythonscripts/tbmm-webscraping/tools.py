from bs4 import BeautifulSoup as BS
import requests
# import time


def read_page(parsed):
    return parsed.get_text()


def parse_link(link):
    if type(link) is list:
        parsed_list = []
        for l in link:
            parsed = parse_link(l)
            parsed_list.append(parsed)
        return parsed_list
    else:
        page = requests.get(link)
        return BS(page.text, "html.parser")


def get_links(parsed):
    links = []
    for tag in parsed.find_all("a"):
        links.append(tag.get("href"))
    return links

# Anasayfa İndirilir ve Ayrıştırılır
anasayfa_linki = "https://www.tbmm.gov.tr/tutanak/tutanaklar.htm"
anasayfa = parse_link(anasayfa_linki)

# Tüm yasama yılları indirilir ve ayrıştırılır
yasama_yili_linkleri = get_links(anasayfa)
yasama_yili_sayfalari = parse_link(yasama_yili_linkleri)

birlesim_linkleri = []
birlesim_sayfalari = []
for yasama_yili_sayfasi in yasama_yili_sayfalari:
    links = get_links(yasama_yili_sayfasi)
    birlesim_linkleri.append(links)
    # birlesim_sayfalari.append(parse_link(links))


print(birlesim_linkleri[0:-8])
string = read_page(parse_link(birlesim_linkleri[0][0]))
with open("sample.txt", "w") as myFile:
    myFile.write(string)
