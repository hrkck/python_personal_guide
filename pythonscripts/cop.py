"""
Condition Oriented Test:
Abstracting conditional flow from transitional flow.
"""

print(__doc__)

AMOUNT = 100


def amount_bigger_than(that):
    if(that < AMOUNT):
        return True


if amount_bigger_than(50):
    print("Yes!")
