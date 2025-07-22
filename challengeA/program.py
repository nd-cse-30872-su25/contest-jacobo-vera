"""
Author: Jacobo Wiesner and Vera Casquero
Date: 07/21/2025
Challenge A
"""

import sys

def main():
    """Counts and prints buildings that are strictly taller than all
    buildings to their right, for each input line of heights."""

    while True:
        line = sys.stdin.readline()
        if not line:
            break 
        arr = list(map(int, line.strip().split()))

        if not arr:
            continue

        counter = 0 #counter of buildings that see the sun
        maximum = float('-inf') #just a value to start the function

        for i in range(len(arr) - 1, -1, -1): #loops in reverse with index
            if arr[i] > maximum:
                maximum = arr[i]
                counter += 1 #add if taller than all buildings to the right

        print(counter)

if __name__ == "__main__":
    main()

