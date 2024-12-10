def read_book(path_to_book_txt):
    with open(path_to_book_txt) as f:
        file_contents = f.read()
    return file_contents


def word_count(book_txt):
    words = book_txt.split()
    return len(words)


def character_occurrences(book_txt):
    letters_dict = {}
    for ch in book_txt:
        ch = ch.lower()
        # Check if character is alphanumeric
        if ch.isalpha():
            if ch in letters_dict:
                letters_dict[ch] += 1
            else:
                letters_dict[ch] = 1
    return letters_dict


def report(path_to_book, word_count, letters_dictionary):
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    sorted_by_occurrence = dict(sorted(letters_dictionary.items(), key=lambda item: item[1], reverse=True))
    for letter in sorted_by_occurrence:
        print(f"The '{letter}' character was found {letters_dictionary[letter]} times")
    for letter in letters_dictionary:
        print(f"The '{letter}' character was found {letters_dictionary[letter]} times")
    print(f"--- End report ---")


def main():
    book_path = "./books/frankenstein.txt"
    book_txt = read_book(book_path)
    total_words = word_count(book_txt)
    total_chars = character_occurrences(book_txt)

    report(book_path, total_words, total_chars)


main()
