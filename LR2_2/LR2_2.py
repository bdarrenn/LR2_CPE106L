import sys

enterfile = input("Enter the file name: ")

with open(enterfile) as f:
    lines = [line.rstrip() for line in f]

print("The number of lines in this .txt file is", len(lines))

while True:
    num = int(input("Please enter a line number or press 0 to quit: "))

    if num > 0 and num < len(lines) + 1:
        print(lines[num - 1]) 
    elif num == 0:
        print('Exiting...')
        sys.exit(0)