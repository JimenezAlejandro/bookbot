

def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()