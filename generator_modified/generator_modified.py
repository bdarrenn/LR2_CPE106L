import random

def getWords(fileName):
    with open(fileName) as f:
        lines = [line.rstrip() for line in f]
    return tuple(lines)

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))

    for i in range(number):
        print(sentence())

prepositions = getWords("prepositions.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
articles = getWords("articles.txt")

# The entry point for program execution
if __name__ == "__main__":
    main()