# Ramu's Birthday Sweets Distribution
# Five-year-old Ramu is distributing sweets on his birthday. He wants to distribute one
# sweet to each of his classmates. However, his classmates each want more than one and
# will trick him. So, Ramu enters into his computer the name of the person as soon as he
# gives a sweet to that person.
# Write a program to take a list of names and print how many sweets each person
# received.
# Input will consist of one name on each line. End of input is marked by a blank line or
# EOF. You should output one line for each name. The line should contain the name
# followed by a space followed by the number of times the person took the sweet.
# Example:
# Input : hari
# babu
# ramu
# babu
# babu
# Ramu
# Output
# hari: 1
# babu: 3
# ramu: 2
# Create a dictionary to store the sweet count for each person
sweet_count = {}

print("Enter names (one per line), end input with an empty line:")

# Loop to read input until an empty line is entered
while True:
    try:
        name = input().strip()
        if name == "":
            break
        name = name.lower()  # Convert name to lowercase for case insensitivity
        if name in sweet_count:
            sweet_count[name] += 1
        else:
            sweet_count[name] = 1
    except EOFError:
        break

# Print the sweet counts for each person
print("Output:")
for name, count in sweet_count.items():
    print(f"{name}: {count}")