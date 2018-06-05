from marshal import dump, load
from helper_functions import print_me


myFunction_str = """
def myFunction(param1=3, param2=4):
    result = param1 + param2
    print("The result is ", result)
    return result

myFunction()
"""


code_object = compile(myFunction_str, "", "exec")

# Kod Nesnesi Kaydediliyor
with open("myFunction.dump", "wb") as filehandler:
    dump(code_object, filehandler)

# Kod Nesnesi
with open("myFunction.dump", "rb") as filehandler:
    loaded_object = load(filehandler)

# Terminale bas:
print_me("Derlenmiş", "çalıştırılıyor", code_object)
print_me("Yüklenmiş", "çalıştırılıyor", loaded_object)
print_me("Derlenmiş", "çözümleniyor",  code_object)
print_me("Yüklenmiş", "çözümleniyor", loaded_object)
