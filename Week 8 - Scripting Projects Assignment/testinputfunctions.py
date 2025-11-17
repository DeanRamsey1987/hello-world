def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Guarantees that the user inputs a floating-point number,
    using the given prompt. Returns the float."""
    while True:
        theString = input(prompt)
        # Check if input is valid: digits or one decimal point
        if theString.replace('.', '', 1).isdigit():
            return float(theString)
        else:
            print("Error: enter digits or digits with one decimal point only")

def main():
    n = inputInt("Please enter an integer: ")
    print("You entered integer:", n)

    f = inputFloat("Please enter a float: ")
    print("You entered float:", f)

if __name__ == "__main__":
    main()
