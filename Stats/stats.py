import os
import sys

def median(listName):
    fileName = listName
    f = open(fileName, 'r')
        
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    # Sort the list and print the number at its midpoint
    numbers.sort()
    midpoint = len(numbers) // 2
    print("The median is", end=" ")
    if len(numbers) % 2 == 1:
        print(numbers[midpoint])
    else:
        print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

def mode(listName):
    fileName = listName
    f = open(fileName, 'r')
        
    # Input the text, convert its to words to uppercase, and
    # add the words to a list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())

    # Obtain the set of unique words and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    for word in words:
        number = theDictionary.get(word, None)
        if number == None:
            # word entered for the first time
            theDictionary[word] = 1
        else:
            # word already seen, increment its number
            theDictionary[word] = number + 1

    # Find the mode by obtaining the maximum value
    # in the dictionary and determining its key
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            print("The mode is", key)
            break

def mean(listName):
    fileName = listName
    f = open(fileName, 'r')

    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))
    print("The mean is ", sum(numbers)/2)

def main():
    file_name = input("File name: ")
    filesize = os.path.getsize(file_name)
    if filesize == 0:
        print("Empty file")
        return 0
    else:
        choice = int(input("1. Mean \n2. Median \n3. Mode \n4. Exit \n"))
        while True:
            if choice == 1:
                mean(file_name)
            elif choice == 2:
                median(file_name)
            elif choice == 3:
                mode(file_name)
            elif choice == 4:
                sys.exit(0)
            else:
                print("Invalid input. Try again.")
            choice = int(input("1. Mean \n2. Median \n3. Mode \n4. Exit \n"))

main()