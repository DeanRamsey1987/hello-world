def myRange(start, stop=None, step=None):
    if stop is None:
        return list(range(start))
    elif step is None:
        return list(range(start, stop))
    else:
        return list(range(start, stop, step))

def main():
    print("Test myRange function")
    print("Enter 1, 2, or 3 numbers to test it.")

    # Get user input as a single line, like: 5 or 2 10 or 1 10 2
    user_input = input("Enter numbers separated by spaces: ")
    parts = user_input.split()

    # Convert parts to integers
    nums = [int(x) for x in parts]

    # Call myRange based on how many values user entered
    if len(nums) == 1:
        result = myRange(nums[0])
    elif len(nums) == 2:
        result = myRange(nums[0], nums[1])
    elif len(nums) == 3:
        result = myRange(nums[0], nums[1], nums[2])
    else:
        print("Please enter 1, 2, or 3 numbers only.")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
