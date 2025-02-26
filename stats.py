def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    letters = {}
    text = text.lower()
    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_on(dict):
    for k,v in dict.items():
        return v

