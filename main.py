from art import logo
from replit import clear

def add(a, b):
    """ adds the two parameters"""
    return a + b
    
def subtract(a, b):
    """Subtracts the two parameters"""
    return a - b
    
def multiply(a, b):
    """Mutiplys the parameters"""
    return a * b
    
def division(a, b):
    """divides the parameters"""
    return a / b

def calculator():
    print (f"{logo}\n Calculator")
    operation = {
        "*": multiply,
        "+": add,
        "/": division,
        "-": subtract
    }
    digit_1 = float(input("Input a figure: "))
    rerun = True
    while rerun :
        for i in operation:
            print(i)
        
        operator = input("Select an operator from the line above: ")
        digit_2 = float(input("Input a figure: "))
    
        result = operation[f"{operator}"](digit_1,digit_2)
        print(f"{digit_1} {operator} {digit_2} = {result}")
        
        
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ").lower() == 'y':
            digit_1 = result
        else:    
            rerun = False
            calculator()
  
    
calculator()