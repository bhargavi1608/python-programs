# Take input from the user
input_string = input("Enter a string: ")

# Convert the string to lowercase to ensure case insensitivity
input_string = input_string.lower()

# Split the string into words
words = input_string.split()

# Create a dictionary to store the word frequencies
word_count = {}

# Iterate over the words and count their frequencies
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word frequencies
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")