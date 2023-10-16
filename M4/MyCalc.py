class MyCalc:
    def __init__(self):
        self.ans = 0

    def add(self, num):
        try:
            self.ans += num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    
    def subtract(self, num):
        try:
            self.ans -= num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    
    def multiply(self, num):
        try:
            self.ans *= num
        except TypeError:
            print("Invalid input. Please provide a valid number.")
    
    def divide(self, num):
        try:
            if num == 0:
                print("Error: Division by zero.")
            else:
                self.ans /= num
        except TypeError:
            print("Invalid input. Please provide a valid number.")

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

# Test cases
def test_calculation():
    calc = MyCalc()

    # Test number-add-number
    calc.add(2)
    assert calc.ans == 2

    # Test ans-add-number
    calc.add(3)
    assert calc.ans == 5

    # Test number-sub-number
    calc.subtract(1)
    assert calc.ans == 4

    # Test ans-sub-number
    calc.subtract(2)
    assert calc.ans == 2

    # Test number-mult-number
    calc.multiply(5)
    assert calc.ans == 10

    # Test ans-mult-number
    calc.multiply(2)
    assert calc.ans == 20

    # Test number-div-number
    calc.divide(4)
    assert calc.ans == 5

    # Test ans-div-number
    calc.divide(2)
    assert calc.ans == 2.5

if __name__ == "__main__":
    main()
