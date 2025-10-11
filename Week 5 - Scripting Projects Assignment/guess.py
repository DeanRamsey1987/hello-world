import math

# Getting range
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
if larger < smaller:
    smaller, larger = larger, smaller

# Getting limit
size = larger - smaller + 1
min_guesses = 1 if size <= 1 else math.ceil(math.log(size, 2))

print(f"\nThink of an integer between {smaller} and {larger}.")
print(f"I will find it in at most {min_guesses} guess(es).\n")

low = smaller
high = larger
count = 0

def ask_hint(guess: int) -> str:
    """Normalize user hint to 'h', 'l', or 'c'."""
    while True:
        resp = input(f"Is it {guess}? (h)igher, (l)ower, or (c)orrect: ").strip().lower()
        if resp in ("h", "higher"):
            return "h"
        if resp in ("l", "lower"):
            return "l"
        if resp in ("c", "correct", "y", "yes"):
            return "c"
        print("Please type h, l, or c.")

while low <= high:
    guess = (low + high) // 2
    count += 1
    hint = ask_hint(guess)

    if hint == "c":
        print(f"\nYou've got it! Your number is {guess}.")
        print(f"I used {count} guess(es) out of the {min_guesses} allowed.")
        break

    if hint == "h":
        # Cheating check
        if guess == high:
            print("\nThat hint is impossible (no higher numbers left). No cheating!")
            break
        low = guess + 1

    elif hint == "l":
        # Cheating check
        if guess == low:
            print("\nThat hint is impossible (no lower numbers left). No cheating!")
            break
        high = guess - 1

    # Checking if still consistent
    if low > high:
        print("\nYour hints are inconsistent with any number in the range. Low blow Karen!")
        break

    # Prevent exceeding the minimum if misled
    remaining = high - low + 1
    remaining_min = 0 if remaining <= 1 else math.ceil(math.log(remaining, 2))
    if count + remaining_min > min_guesses:
        print("\nYour hints made it impossible to finish within the minimum number of guesses.")
        print("That suggests inconsistent or misleading answers. Let's try again fairly.")
        break
else:
    print("\nNo number fits those hints. That indicates cheating or input errors.")
