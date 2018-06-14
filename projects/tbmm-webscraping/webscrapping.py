from bs4 import BeautifulSoup as BS
from bs4 import UnicodeDammit
import requests
import os
# import datetime
FOL = "tutanaklar"


def create_dir():
    if not os.path.exists(FOL):
        print('Creating directory: ' + FOL)
        os.makedirs(FOL)


def prettify_dammit(parsed):
    prettified = parsed.prettify("latin-1")
    markup = UnicodeDammit(prettified).unicode_markup
    parsed = BS(markup, "html.parser")
    return parsed.get_text()


def fix_encoding(string):
    string = str(string)
    decoder = {'þ': 'ş',
                'Þ': 'Ş',
                'Ý': 'İ',
                'ý': 'ı',
                'Ð': 'Ğ',
                'ð': 'ğ'}
    # start = datetime.datetime.now()
    for key in decoder.keys():
        for s in string:
            if s == key:
                string = string.replace(s, decoder[key])
    return string
    # end = datetime.datetime.now()
    # print("Run time of decoding is : ", end - start)


def parse_link(link):
    if type(link) is list:
        parsed_list = []
        for l in link:
            parsed = parse_link(l)
            parsed_list.append(parsed)
        return parsed_list
    else:
        try:
            page = requests.get(link)
            return BS(page.text, "html.parser")
        except Exception as e:
            print(str(e))
            string = "Error with the following link\n" \
                    + str(link) \
                    + "ERROR MESSAGE:\n" \
                    + str(e) + "\n"
            with open("error_messages.txt", "a+") as output:
                output.write(string)


def get_links(parsed):
    links = []
    for tag in parsed.find_all("a"):
        if "ozet" in str(tag) or "oylama" in str(tag):
            continue
        links.append(tag.get("href"))
    return links


###
# Get main link a scrape all the links:
tbmm = "https://www.tbmm.gov.tr/tutanak/tutanaklar.htm"
ana = parse_link(tbmm)
yyl = get_links(ana)
yyp = parse_link(yyl)
brl = []
brp = []
for x in yyp:
    brl.append(get_links(x))
brl = brl[0:-8]  # Not every minutes report concern us
###


###
# Download minutes to a txt file:
create_dir()
for yy in brl:  # yasama yili
    for br in yy:  # o yasama yilinin birlesimi
        minutes = fix_encoding(prettify_dammit(parse_link(br)))  # Minutes
        # clean css markups:
        s = minutes.find("<!--")
        e = minutes.find("-->")
        minutes = minutes[:s] + minutes[e+3:]
        #
        # work out file name:
        br = str(br)
        ln = br.split("/")
        fN = FOL + "/" + ln[-4] + "-" + ln[-3] + "-" + ln[-1][:-4] + ".txt"
        #
        with open(fN, "w") as output:
            output.write(minutes)
###
