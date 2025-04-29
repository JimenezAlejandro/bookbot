import sys
from stats import get_num_words, get_char_count_dict, get_sorted_char_count


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count_dict(text)
    sorted_chars = get_sorted_char_count(char_count)
    print_divider_with_text("BOOKBOT", "=", 12)
    print(f"Analyzing book found at {book_path}...")
    print_divider_with_text("Word Count", "-", 11)
    print(f"Found {num_words} total words")
    print_divider_with_text("Character Count", "-", 9)
    for d in sorted_chars:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print_divider_with_text("END", "=", 13)
    
def print_divider_with_text(text, divider, divider_count):
    print(f"{divider * divider_count} {text} {divider * divider_count}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()