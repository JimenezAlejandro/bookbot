def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    character_counts = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in character_counts:
            character_counts[char_lower] = 0
        character_counts[char_lower] += 1
    return character_counts