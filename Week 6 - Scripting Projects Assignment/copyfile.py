# File names
source_name = "source.txt"
target_name = "copy.txt"

try:
    with open(source_name, 'r') as source_file:
        # Open source
        with open(target_name, 'w') as target_file:
            # Copy contents
            for line in source_file:
                target_file.write(line)

    print(f"Contents of '{source_name}' have been copied to '{target_name}'.")

except FileNotFoundError:
    print(f"Error: The file '{source_name}' was not found.")
except IOError:
    print("Error: There was a problem reading or writing the files.")
