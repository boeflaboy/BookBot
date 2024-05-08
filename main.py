def open_book(path_to_book) -> str:
    with open(f"{path_to_book}") as file:
        return file.read()

def count_words(text) -> int:
    words = text.split()
    word_count = 0
    for _ in words:
        word_count += 1
    return word_count

def count_letters(text) -> dict:
    characters = {}
    for each_character in text.lower():
        if each_character.isalpha():
            characters[each_character] = characters.get(each_character, 0) + 1
    return characters

def generate_report(book, file_content) -> None:
    print(f"--- Begin of report of {book} ---")
    print(f"{count_words(file_content)} words found in the document")
    characters = count_letters(file_content)
    characters = sorted(characters.items())
    print()
    for character, occurence in characters:
        print(f"The {character} was found {occurence} times")
    print("--- End Report ---")


book = "books/frankenstein.txt"
file_content_book = open_book(book)
generate_report(book, file_content_book)



