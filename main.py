import sys
from stats import wordcount, sorted_characters

def main():
    if len(sys.argv) == 2:
        print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
        wordcount(sys.argv[1])
        print("--------- Character Count -------")
        for entry in sorted_characters(sys.argv[1]):
            print(f"{entry["char"]}: {entry["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()