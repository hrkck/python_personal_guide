"""
MARKUP kodunu HTML koduna cevirir.
"""


def updatehtml(resim_url):
    html_tag = '<img class="resim" src="' + resim_url + '">'
    return html_tag


def markuptohtml(markuplines = ""):
    html_lines = []
    for line in markuplines:
        # Aralik degerlerini bul
        startP = line.find("![](")

        # Bulamazsan devam et
        if startP == -1:
            html_lines.append(line[:-1])
            continue

        startP += 5
        endP = line.rfind(")")
        # resim URL'ini bul
        resim_url = line[startP:endP]
        html_tag = updatehtml(resim_url)
        # append to list
        html_lines.append(html_tag)

    return "\n".join(html_lines)


def dosya_oku_yaz(txt):
    with open(txt, "r") as text:
        html_version = markuptohtml(text.readlines())
    with open("html_hali", "w") as text:
        text.write(html_version)
