"""
Authors: Jacobo Wiesner and Vera Casquero
Date: 07/23/2025
Challenge B
"""
import sys

def main():
    """ This is a common leetcode problem that shows up in interviews.
        The trick is to initialize a dictionary with the first occurence of a letter.
        Then if you see that letter again, that same poisition should also be held by the 
        same index letter in the second string to be isomorphic."""
    
    for line in sys.stdin:
        s, t = line.strip().split()
        char_index_s = {} #key is the letter, value first ocurrence index
        char_index_t = {}
        isomorphic = True

        for i in range(len(s)):
            if s[i] not in char_index_s: #initializes first occurence
                char_index_s[s[i]] = i
            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            if char_index_s[s[i]] != char_index_t[t[i]]: #checks isomorphism
                isomorphic = False
                break

        print("Isomorphic" if isomorphic else "Not Isomorphic")

if __name__ == "__main__":
    main()

