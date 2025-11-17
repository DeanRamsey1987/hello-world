def isSorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def int_list():
    """Prompt until the user enters only integers separated by spaces.
    Blank input means an empty list."""
    while True:
        s = input("Enter integers separated by spaces (blank for empty list): ").strip()
        if s == "":
            return []
        parts = s.split()
        try:
            return [int(p) for p in parts]
        except ValueError:
            print("Error: please enter only integers separated by spaces.")

def main():
    data = int_list()
    print("List:", data)
    print("Sorted ascending?", isSorted(data))

if __name__ == "__main__":
    main()
