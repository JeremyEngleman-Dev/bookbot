def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_word_count(text)
    character_count = get_char_count(text)
    list_of_characters = process_char_count(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {number_of_words} words in the file.")
    print(" ")
    for char in list_of_characters:
        print(f"The {char['char']} character was found {char['num']} times")
    print("--- End report ---")

def get_word_count(content):
    words = content.split()
    return len(words)

def get_char_count(content):
    lower_case_content = content.lower()
    characters = {}
    for letter in lower_case_content:
        if letter.isalpha() == False:
            continue
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_on(d):
    return d["num"]

def process_char_count(characters):
    character_list = []
    for char in characters.items():
        character_list.append({"char": char[0], "num": char[1]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()