import smtplib

content = \
"""
flashlights expands and collaps around me,
did I come from Eve?
my eyes starves to see the absolute light:
does Universe expand in shephard's sight?
 
cold and hot conflict on my skin,
feeling of truth or sin?
I want to feel stars:
was Ptolemeious right or blind?
"""


sender = "hakkirizakucuk@gmail.com"
receiver = "hakkirizakucuk@yandex.com"

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(sender,"supersecretpass")
mail.sendmail(sender, receiver, content)
mail.close()
