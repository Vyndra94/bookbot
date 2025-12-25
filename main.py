from stats import wordcount, sorted_characters

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    wordcount()
    print("--------- Character Count -------")
    for entry in sorted_characters():
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()