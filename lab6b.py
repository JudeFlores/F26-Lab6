# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: November 4th, 2026
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py
# TO DO 1: Copy the code from lab6a.py and paste here.
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.

def s3_or_s5(s3, s5):
    union_set=s3.union(s5)
    common_set=s3.intersection(s5)
    result_set=union_set.difference(common_set)
    return result_set
def buildtheSet(divisor):
    s=set()
    for i in range(1,101):
        if i%divisor==0:
            s.add(i)
        else:
            i=i+1
    return s
def main():
    s3 = buildtheSet(3)
    s5 = buildtheSet(5)
    print(s3_or_s5(s3,s5))

main()