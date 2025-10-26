def sort_on(items):
    return items["num"]


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

def create_sorted_list(char_count):
    sorted_list = []
    for key in char_count:
        sorted_list.append({"char": key, "num": char_count[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
