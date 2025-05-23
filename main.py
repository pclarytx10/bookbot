import sys
from stats import get_num_words, get_char_count, sort_dict_by_value

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
# Read the file contents
with open(sys.argv[1]) as f:
    file_contents = f.read()

num_words = get_num_words(file_contents)  # Count the number of words in the file
char_count = get_char_count(file_contents)  # Count the number of characters in the file
sorted_chars = sort_dict_by_value(char_count)  # Sort the character counts by value
def print_top_chars(sorted_chars):
    for char, count in sorted_chars.items():
        if char.isalpha():
            print(f"{char}: {count}")

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")  # Print the first 1000 characters of the file
print("--------- Character Count -------")
print_top_chars(sorted_chars)
print("============= END ===============")
