def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))
    
main()