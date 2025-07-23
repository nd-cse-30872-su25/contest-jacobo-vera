#!/usr/bin/env python3

# ChallengeD: Football Scores
# Vera Casquero & Jacobo Weisner 
import sys 

#Global 
POINTS = [2, 3, 7]
MAX = 100

#Functions 
#Dynamic programming 
def build_arr(score: int) -> list[list[list[int]]]: 
    #Create empty arr and set first possibility
    ways = [[] for _ in range(score + 1)]
    ways[0] = [[]]
    #Iter through points, 
    for point in POINTS: 
        #Each possible total score
        for sum in range(point,score+1): 
            #Each way to achieve a smaller score
            for way in ways[sum-point]: 
                new_way = way + [point]
                #Append new way
                ways[sum].append(new_way)
    return ways

#Main Execution 
def main(): 
    #Read in from stdin
    scores = []
    for line in sys.stdin: 
        score = int(line.strip())
        scores.append(score)
    max_score = max(scores)
    #Get all possible ways to score
    ways = build_arr(max_score)

    #Print for each test case
    for n in scores: 
        combinations = sorted(ways[n])
        count = len(combinations)

        if count == 1: 
            print(f"There is 1 way to achieve a score of {n}:")
        else: 
            print(f"There are {count} ways to achieve a score of {n}:")
        
        for combination in combinations: 
            print(' '.join(map(str,combination)))

if __name__ == "__main__": 
    main() 
