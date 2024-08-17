def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print(letter_count)

def get_letter_count(text):
    lower_text = text.lower()
    letter_count = {}
    for character in text:
        if character not in letter_count:
            letter_count[character] = 1
        else:
            letter_count[character] += 1
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()

