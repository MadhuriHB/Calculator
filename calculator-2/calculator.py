"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic


def operations():
    while True:

        operation = raw_input("Please enter the calculation you want >>>\n")
        # asks user to input the operation they want
        try:
            operation = operation.split(" ")
            op = operation[0]
            num1 = int(operation[1])
            if len(operation) > 2:
                num2 = int(operation[2])  # accepts integers
        except IndexError:
            print "Did you enter a valid format ? Please try again\n "
            continue

        if op == "add":
            return arithmetic.add(num1, num2)
        elif op == "subtract":
            return arithmetic.subtract(num1, num2)
        elif op == "divide":
            return arithmetic.divide(num1, num2)
        elif op == "multiply":
            return arithmetic.multiply(num1, num2)
        elif op == "power":
            return arithmetic.power(num1, num2)
        elif op == "square":
            return arithmetic.square(num1)
        elif op == "cube":
            return arithmetic.cube(num1)
        elif op == "mod":
            return arithmetic.mod(num1, num2)


def calculate():
    answer = "Y"
    while answer == "Y":

        print "Would you like to play?"
        answer = raw_input("Please enter Y for Yes or N for No >>> \n")
        if answer == "Y":
            print operations()
        else:
            print "Thank you!"


calculate()
