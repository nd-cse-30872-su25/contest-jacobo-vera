#!/usr/bin/env python3

# ChallengeF: Matrix
# Vera Casquero & Jacobo Weisner 
import sys 
import heapq
from collections import defaultdict

#Types 
Graph = dict[int, dict[int,int]]

#Functions 
def build_graph(matrix: list[list[int]], m: int, n: int) -> Graph: 
    graph: Graph = defaultdict(dict)

    #Iter through each cell and try possible directions to build graph (adj list)
    for row in range(m): 
        for col in range(n - 1): 
            cur = row * n + col
            for dir_row in (-1, 0, 1): 
                n_row = (row+dir_row) % m
                n_col = col + 1
                next = n_row * n + n_col

                graph[cur][next] = matrix[n_row][n_col]
    return graph 

def dijkstra(graph: Graph, start_cost: dict[int,int]) -> tuple[dict[int,int], dict[int,int]]: 
    #Using dijkstra's algorithm 
    frontier = []
    for node, cost in start_cost.items():
        #Include nodes in first col 
        heapq.heappush(frontier,(cost,node,None))
    distance = {}
    source = {}

    while frontier: 
        cost, node, s = heapq.heappop(frontier)
        if node in source: 
            continue 
        #Record cost & source of target 
        distance[node] = cost
        source[node] = s

        for neighbor, weight in graph[node].items(): 
            if neighbor not in source: 
                heapq.heappush(frontier,(cost + weight,neighbor,node))

    return distance, source

def reconstruct_path(source: dict[int,int], end: int) -> list[int]: 
    #Reconstructing the path
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = source[cur]
    return list(reversed(path))



#Main Execution 
def main(): 
    #Read input from stdin 
    data = sys.stdin.read().split()
    i = 0

    #Iter through data
    while i < len(data): 
        #Collect dimensions
        m = int(data[i])
        i += 1
        n = int(data[i])
        i += 1

        #Create matrix
        matrix = []
        for j in range(m): 
            row = list(map(int,data[i:i+n]))
            matrix.append(row)
            i += n

        #Build graph
        graph = build_graph(matrix,m,n)
        #Build starting dict & pass to dijkstra's algorithm 
        start_costs = {r*n: matrix[r][0] for r in range(m)}
        dist, source = dijkstra(graph, start_costs)

        #Pick best
        best_cost = float('inf')
        best_node = None
        for r in range(m):
            node = r * n + (n - 1)
            cost = dist.get(node,float('inf'))
            if cost < best_cost: 
                best_cost = cost
                best_node = node
        
        #Recover path 
        path = reconstruct_path(source, best_node)
        rows = [p//n + 1 for p in path]

        #Print
        print(f"{best_cost}")
        print(f"{' '.join(map(str, rows))}")

    
       
if __name__ == "__main__": 
    main()
