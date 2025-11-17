def mean(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def median(nums):
    if not nums:
        return 0
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    return nums[mid]

def mode(nums):
    if not nums:
        return 0
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    max_count = max(counts.values())
    for k, v in counts.items():
        if v == max_count:
            return k

def main():
    try:
        with open("numbers.txt", "r") as file:
            nums = [float(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print("numbers.txt not found.")
        return

    print("Numbers:", nums)
    print("Mean:", mean(nums))
    print("Median:", median(nums))
    print("Mode:", mode(nums))

if __name__ == "__main__":
    main()
