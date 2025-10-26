def get_num_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_char_count(book_text):
    low_text = book_text.lower()
    char_count = {}
    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    
