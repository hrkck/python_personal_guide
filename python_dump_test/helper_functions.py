import dis
green = '\033[32m'
reset = '\033[0m'


def print_me(text1, text2, code_object):
    print(text1 + " kod nesnesi " + text2 + ": " + green)
    if(text2.__eq__("çalıştırılıyor")):
        exec(code_object)
    else:
        dis.dis(code_object)
    print(reset + " Son. \n")
