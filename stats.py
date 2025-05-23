def get_num_words(contents):
    """Count the number of words in a string."""
    return len(contents.split())

def get_char_count(contents):
    """Count the number of characters in a string."""
    char_counts = {}
    for char in contents.lower():
        if char in char_counts:
            char_counts[char] += 1
            # print(f"char: {char} count: {char_counts[char]}")
        else:
            char_counts[char] = 1
            # print(f"char: {char} count: {char_counts[char]}")
            
    # print(f"char_counts: {char_counts}")
    return char_counts

def sort_dict_by_value(d):
    """Sort a dictionary by its values."""
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
