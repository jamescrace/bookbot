import sys
from stats import count_words, count_characters, sort_on


def get_book_text(filepath):
    with open(filepath) as f:
        file_string = f.read()
    return file_string


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    characters = count_characters(text)
    char_list = []
    for k, v in characters.items():
        if k.isalpha():
            char_list.append({k: v})
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_list:
        for k, v in char.items():
            print(f"{k}: {v}")


main()
