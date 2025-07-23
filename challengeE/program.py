#!/usr/bin/env python3

# ChallengeD: Tree Paths
# Vera Casquero & Jacobo Weisner 
import sys 

#Functions 
def find_paths(tree: list[int], target: int, index: int, path: list[int], results:list[list[int]]) -> None: 
    #Check if index is out of bounds 
    if index >= len(tree) or tree[index] == 0: 
        return 

    #Add starting index to path
    path.append(tree[index])
    
    #Create left and right indexes to traverse graph
    left = 2*index + 1
    right = 2 * index + 2

    #Boolean statement to check if current node is a leaf
    leaf = (left >= len(tree) or tree[left] == 0) and (right >= len(tree) or tree[right] == 0)

    #If leaf, check sum of the path and append to result if = target
    if leaf: 
        if sum(path) == target: 
            results.append(list(path))
    else: 
        #Recurse
        find_paths(tree,target,left,path,results)
        find_paths(tree,target,right,path,results)
    #Backtrack 
    path.pop()

#Main Execution 
def main(): 
    #Read input from stdin 
    lines = [line.strip() for line in sys.stdin]
    i = 0
    #Iter through lines to get target & tree
    while i < len(lines): 
        target = int(lines[i])
        tree = list(map(int,lines[i+1].split()))
        i += 2

        #Store all paths for target sum
        results = []
        find_paths(tree, target, 0, [], results)

        #Sort for correct output and print
        results.sort()
        for p in results: 
            print(f"{target}: {', '.join(map(str, p))}")



if __name__ == "__main__": 
    main()

