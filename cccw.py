import sys

def count_lines_words_chars(file_path):
    lines = 0
    words = 0
    characters = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters

if len(sys.argv) != 2:
    print("Usage: python cccw.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try :
    lines, words, characters = count_lines_words_chars(file_path)
    print(f"Lines: {lines}")
    print(f"words: {words}")
    print(f"Characters: {characters}")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")