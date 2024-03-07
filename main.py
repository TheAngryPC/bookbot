#!/home/codespace/.python/current/bin/python
#!/home/devnat/.pyenv/shims/python

PATH = "books/frank.txt"


def main():
    text = get_book_text(PATH)
    report(text)


def report(text:str):
    text = get_book_text(PATH)
    letters = get_letter_count(text)
    num_words = get_word_count(text)

    print(f"--- BEGIN REPORT OF {PATH} ---")
    print(f"{num_words} words found in the document")
    print()
    for char in letters:
        print(f"The {char} character was found {letters[char]} times")
    print("--- END REPORT ---")

def get_letter_count(text:str):
    letters = {}

    for char in text.lower():
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            elif char in letters:
                letters[char] += 1
    return letters


def get_word_count(text:str):
    words = text.split()
    return len(words)


def get_book_text(path:str):
    with open(path) as file:
        return file.read()


if __name__ == "__main__":
    main()
