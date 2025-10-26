from stats import get_num_words
from stats import get_char_count

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    print(f"Found {word_count} total words")
    print(char_count)
    
main()