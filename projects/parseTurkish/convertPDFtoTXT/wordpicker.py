

def thePicker():

    src = open("DUZGUN.txt", 'r')
    dst = open("sozcuk_dagarcigi.txt", 'w')

    for line in src:
        if "*" not in line:
            dst.write(line)

    src.close()
    dst.close()

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
           'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


def cleaner():

    src = open("sozcuk_dagarcigi.txt", "r")
    dst = open("KULLANILABILIR.txt", "w")

    for line in src:
        if not line.strip():
            continue
        else:
            dst.write(line)

    src.close()
    dst.close()


thePicker()
cleaner()
