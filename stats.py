def wordcount():
    with open("books/frankenstein.txt") as f:
        wordlist = f.read().split()
    print(f"Found {len(wordlist)} total words")

def characters():
    characters = {}
    with open("books/frankenstein.txt") as f:
        lowercase_contents = f.read().lower()
        for char in lowercase_contents:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        return characters

def sorted_characters():
    sorted = characters().sort(reverse=True, key=sort_key)
    return sorted
