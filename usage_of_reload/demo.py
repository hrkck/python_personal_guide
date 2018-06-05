import usefulFunction
from importlib import reload


def main():
    try:
        reload(usefulFunction)
        usefulFunction.myFunction()
    except Exception as e:
        print(str(e))

while True:
    main()
    input("Press Enter to re-run:\n")
