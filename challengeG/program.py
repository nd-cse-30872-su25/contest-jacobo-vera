"""
Authors: Jacobo Wiesner and Vera Casquero
Date: 07/23/2025
Challenge G
"""

import sys
from collections import deque

def build_graph():
    """Reads the next graph from stdin.
    returns (n, matrix), or (None, None) on none."""
    while True:
        line = sys.stdin.readline()
        if line == "":      #end
            return None, None
        line = line.strip()

        if not line:
            continue

        n = int(line)
        matrix = []
        for i in range(n):
            parts = sys.stdin.readline().split()
            row = []
            for num_str in parts:
                row.append(int(num_str))
            matrix.append(row)
        return n, matrix

def bfs(n, matrix):
    """ My approach was an iterative bfs on the entire row to see 
    if there exists a direct connection. if neighbor hasnt been visited then marked 
    and added to queue"""

    visited = set()
    components = 0

    for source in range(n):
        if source in visited:
            continue
        components += 1
        queue = deque([source])
        visited.add(source)

        #bfs
        while queue:
            current = queue.popleft()
            for neighbor, edge in enumerate(matrix[current]):
                if edge and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return components

def main():
    index = 1
    while True:
        n, matrix = build_graph()
        if n is None:
            break
        count = bfs(n, matrix)
        print(f"System {index} isolated circuits: {count}")
        index += 1

if __name__ == "__main__":
    main()
