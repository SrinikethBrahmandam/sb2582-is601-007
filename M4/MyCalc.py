class MyCalc:
    def __init__(self):
        self.ans = 0

    def add(self, num):
        try:
            self.ans += num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    #sb2582(Sriniketh Brahmandam) - 10/16/2023
    #The add method in the MyCalc class accepts a numeric value (num) and adds it to the running total (ans). 
    #It has error handling built in to look for invalid input types, notably TypeError, and produces an error message if one is found.
    #The functionality of the calculator for addition operations relies heavily on this technique.

    def subtract(self, num):
        try:
            self.ans -= num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    #sb2582(Sriniketh Brahmandam) - 10/16/2023
    #A numerical value ('num') is subtracted from the running total ('ans') using the'subtract' function in the 'MyCalc' class. 
    #It has error handling built in to look for invalid input types, notably 'TypeError', and displays an error message if one arises.
    #Carrying out subtraction operations since it makes sure that the internal state is updated appropriately and that any potential input errors are handled.

    
    def multiply(self, num):
        try:
            self.ans *= num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    #sb2582(Sriniketh Brahmandam) - 10/16/2023
    #The current running total ('ans') is multiplied by a number ('num') using the'multiply' function in the 'MyCalc' class.
    #It includes error management, notably handling 'TypeError' exceptions, to verify for proper input types.
    #It displays an error message asking the user to enter a valid number when an invalid input is found.
    #It makes sure that multiplication operations are carried out correctly and that input errors are handled politely.


    def divide(self, num):
        try:
            if num == 0:
                print("Error: Division by zero.")
            else:
                self.ans /= num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    #sb2582(Sriniketh Brahmandam) - 10/16/2023
    #The `divide` method in the `MyCalc` class is responsible for performing division operations, taking a numeric value (`num`) as its input.
    #It includes error handling to check for both division-by-zero circumstances and incorrect input types, notably "TypeError" errors.
    #Any attempt to divide by zero results in an error message reading, "Error: Division by zero."
    #It requests a valid numerical number from the user in the event of invalid input.
    #This function plays a key role in how the calculator performs division operations, delivering accurate output and effective error control.


def main():
    calc = MyCalc()
    while True:
        user_input = input("Enter an operation (e.g., 2 * 2 or ans / 2) or 'q' to quit: ")
        if user_input == 'q':
            break
        try:
            result = eval(user_input, {'ans': calc.ans})
            calc.ans = result
            print(f"Result: {result}")
        except (SyntaxError, NameError, ZeroDivisionError):
            print("Invalid input. Please provide a valid operation.")
#sb2582(Sriniketh Brahmandam) - 10/16/2023


# Test cases
def test_initial_ans_value():
    calc = MyCalc()
    assert calc.ans == 0
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_number_add_number():
    calc = MyCalc()
    calc.add(5)
    assert calc.ans == 5
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_ans_add_number():
    calc = MyCalc()
    calc.ans = 3
    calc.add(2)
    assert calc.ans == 5
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_number_subtract_number():
    calc = MyCalc()
    calc.subtract(3)
    assert calc.ans == -3
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_ans_subtract_number():
    calc = MyCalc()
    calc.ans = 7
    calc.subtract(3)
    assert calc.ans == 4
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_number_multiply_number():
    calc = MyCalc()
    calc.multiply(4)
    assert calc.ans == 0
#sb2582(Sriniketh Brahmandam) - 10/16/2023


def test_ans_multiply_number():
    calc = MyCalc()
    calc.ans = 2
    calc.multiply(5)
    assert calc.ans == 10
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_number_divide_number():
    calc = MyCalc()
    calc.divide(2)
    assert calc.ans == 0
#sb2582(Sriniketh Brahmandam) - 10/16/2023

def test_ans_divide_number():
    calc = MyCalc()
    calc.ans = 8
    calc.divide(4)
    assert calc.ans == 2
#sb2582(Sriniketh Brahmandam) - 10/16/2023
