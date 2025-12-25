def wordcount():
    with open("books/frankenstein.txt") as f:
        wordlist = f.read().split()
    print(f"Found {len(wordlist)} total words")

def characters():
    characters = {}
    with open("books/frankenstein.txt") as f:
        lowercase_contents = f.read().lower()
        for char in lowercase_contents:
            if char.isalpha():
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
        return characters

def sorted_characters():
    sorted_characters = list({"char": k, "num": v} for k, v in characters().items())
    def sort_key(sorted_characters):
        return sorted_characters["num"]
    sorted_characters.sort(reverse=True, key=sort_key)
    return sorted_characters
