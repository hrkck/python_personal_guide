import random

google2 = open("google2.txt", "w")

letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
          'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


google = 10**100

googleplex = google**100

for j in range(google):  # 10**100	<< I m afraid how much it will be >>
    l = random.choice(letter)
    google2.write(l)
