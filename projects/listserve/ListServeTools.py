import requests
from bs4 import BeautifulSoup
import re
import time

#  GET LINKS OF ALL E-MAILS ###
page = requests.get("https://thelistservearchive.com/")
parse = BeautifulSoup(page.text, "html.parser")

all_links = [divTag for divTag in parse.find_all(name="div", attrs = {"class" : "landing-item"}) if divTag.contents[1].name == "ul" ][0]

all_mails = ["https://thelistservearchive.com" + link.get("href") for link in all_links.find_all("a")]


## EXTRACT TEXT OF ALL E-MAILS ###

for counter, mail in enumerate(all_mails):
    page = requests.get(mail)
    parse = BeautifulSoup(page.text, "html.parser")
    container = parse.find("div", attrs={"id":"post"})

    date = container.find("p", {"class": "meta"}).text
    email = container.text

    email = re.sub(r'/\*.+\*/', '', email)
    fileName = str((counter+1))+"-"+date+".txt"
    try:
        with open(fileName, mode='w') as email_file:
            email_file.write(email)
    except Exception:
        print("\nERROR AT: {} with date {}\nSKIPPING...\n".format(counter, date))
        continue

    printString = "Writing {}, Progress {}/{}"
    print(printString.format(date, counter, len(all_mails)), "\r" * len(printString), end='')

    time.sleep(0.2)

print()
