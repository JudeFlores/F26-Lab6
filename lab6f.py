# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: November 4th, 2026
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.
def histogram(string):
    hist = {}

    for letter in string:
        if letter == " ":
            continue
        if letter not in hist:
            hist[letter] = '*'
        else:
            hist[letter] += '*'

    for letter in hist:
        print(letter, hist[letter])


def main():
    histogram("hello world")

if __name__ == "__main__":
    main()