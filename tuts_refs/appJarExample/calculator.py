from appJar import gui

app = gui("Calculator", "560x240")

### FUNCTIONS ###

n1, n2 = 0.0, 0.0
result = 0.0
isFirst = True
calc = ""

def doMath(btn):
    global result, n1, n2, isFirst, calc

    inputNumber()

    if(btn == "Add"): calc =  "a"
    if(btn == "Substract"): calc = "s"
    if(btn == "Multiply"): calc = "m"
    if(btn == "Divide"): calc = "d"

    app.clearEntry("Number")

def calculate(btn):
    global result, n1, n2, isFirst, calc

    inputNumber()

    if(calc == 'a'): result = n1 + n2
    if(calc == 's'): result = n1 - n2
    if(calc == 'm'): result = n1 * n2
    if(calc == 'd'):
        try:
            result = n1 / n2
        except ZeroDivisionError:
            clearOut(btn)
            app.errorBox("DivisionByZero", "You can't divide by Zero.")

    app.clearEntry("Number")
    app.setLabel("Result", result)

def clearOut(btn):
    global result, n1, n2, isFirst, calc
    n1, n2 = 0.0, 0.0
    result = 0.0
    isFirst = True
    calc = ""

def inputNumber():
    global n1, n2, isFirst

    if(isFirst):
        n1 = app.getEntry("Number")
        isFirst = False
    else:
        n2 = app.getEntry("Number")
        isFirst = True


### FUNCTIONS ###

app.setStretch("column")
app.setSticky("")
app.setResizable(True)
app.addNumericEntry("Number")
app.setEntryDefault("Number", "Enter Number")

app.addButtons(["Add", "Substract", "Multiply", "Divide"], doMath)
app.addButtons(["Calculate!", "clearOut"], [calculate, clearOut])
app.setButton("clearOut", "C")

app.addEmptyLabel("Result")

app.go()
