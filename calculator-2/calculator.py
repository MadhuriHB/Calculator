"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

import arithmetic
def utilize_userinput():
    operation = raw_input("Please enter the calculation you want>>>")
# asks user to input the operation they want
    operation = operation.split(" ") 

    num1 = int(operation[1])
    if len(operation) > 2:
        num2 = int(operation[2]) # accepts integers
        
    if operation[0] == "add":
        return arithmetic.add(num1, num2)
    elif operation[0] == "subtract":
        return arithmetic.subtract(num1, num2)
    elif operation[0] == "divide":
        return arithmetic.divide(num1, num2)
    elif operation[0] == "multiply":
        return arithmetic.multiply(num1, num2)
    elif operation[0] == "power":
        return arithmetic.power(num1, num2)
    elif operation[0] == "square":
        return arithmetic.square(num1)
    elif operation[0] == "cube":
        return arithmetic.cube(num1)
    elif operation[0] == "mod":
        return arithmetic.mod(num1, num2)
    else:
        print "Please enter valid operation."
        
        
            
    # if statements to check for valid operations, if incorrect continue to ask

       
def try_again():
    while True:
        print "Would you like to play?"
        answer = raw_input("Please enter Y for Yes or N for No>>>")
        if answer == "Y":
            print utilize_userinput()
        else:
            print "Thank you!"
            break

try_again()


