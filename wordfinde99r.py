"""Word Finder: finds random words from a dictionary."""
import random
file_path = "C:\\Users\Rosty\OneDrive\Desktop\words.txt"
with open(file_path, "r") as file:
    file_contents = file.read()
word = file_contents.split()
random_word = random.choice(word)
print(random_word)

