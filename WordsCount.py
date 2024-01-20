from collections import Counter

def countWords(file):
    # ['Python', 'Course', 'Deep', 'Learning', 'Course'] -
    words = file.split()
    #Counter(words) - Counter({'Course': 2, 'Python': 1, 'Deep': 1, 'Learning': 1})
    return Counter(words)

with open('input.txt', 'r') as inputFile:
    wordsInFile = inputFile.read()

wordCounts = countWords(wordsInFile)

with open('output.txt', 'w') as outputFile:
    outputFile.write(wordsInFile)
    outputFile.write("\n")
    for w, c in wordCounts.items():
        outputFile.write(f"{w}: {c}\n")