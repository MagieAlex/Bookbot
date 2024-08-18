def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    letter_list = dict_to_list(letter_count)
#    print(letter_count)
#    print(letter_list)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in letter_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_list(d):
    return d["num"]

def dict_to_list(dict):
    list = []
    for ch in dict:
        list.append({"char": ch, "num": dict[ch]})
    list.sort(reverse=True, key=sort_list)
    return list

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

