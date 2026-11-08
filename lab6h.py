# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: November 8th, 2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.
# TO DO 2: Create function find_movie().
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.
def add_movie(name, year, director, runtime):
    movie = {"Name: ":name, "Year: ":year, "Director: ":director, "Runtime: ":runtime}
    return movie

def main():
    movielist=[]
    movielist.append(add_movie("Dune", "2021", "Denis Villeneuve", "155 minutes"))
    movielist.append(add_movie("Howl's Moving Castle", "2004", "Hayao Miyazaki", "119 minutes"))
    movielist.append(add_movie("The Matrix", "1999", "The Wachowskis", "136 minutes"))
    movielist.append(add_movie("Oppenheimer", "2023", "Christopher Nolan", "180 minutes"))
    print(movielist)

if __name__ == "__main__":
    main()
