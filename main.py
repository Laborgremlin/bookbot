from stats import get_num_words
from stats import get_char_count
from stats import create_sorted_list

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = create_sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()