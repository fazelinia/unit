""" module doc pylint sample2.py"""
def add(number1, number2):
    """
        add two nums
    """
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
