def main():
    filename = input("Enter a filename: ")

    try:
        with open(filename, "r") as file:
            lines = [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        print("File not found.")
        return

    total = len(lines)
    print("The file has", total, "lines.")

    while True:
        try:
            choice = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Goodbye!")
            break
        elif 1 <= choice <= total:
            print(f"Line {choice}: {lines[choice - 1]}")
        else:
            print("Line number out of range.")

if __name__ == "__main__":
    main()
