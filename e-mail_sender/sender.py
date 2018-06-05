import smtplib

content = "Example content"
sender = "hakkirizakucuk@gmail.com"
receiver = "hakkirizakucuk@yandex.com"

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(sender,"supersecretpass")
mail.sendmail(sender, receiver, content)
mail.close()
