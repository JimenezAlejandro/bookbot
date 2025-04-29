def get_num_words(text):
    return len(text.split())

def get_char_count_dict(text):
    character_counts = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in character_counts:
            character_counts[char_lower] = 0
        character_counts[char_lower] += 1
    return character_counts

def sort_on(dict):
    return dict["num"]

def get_sorted_char_count(char_dict):
    sorted = []
    for char in char_dict:
        sorted.append({ "char": char, "num": char_dict[char] })
    sorted.sort(reverse=True, key=sort_on)
    return sorted