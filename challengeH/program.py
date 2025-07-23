"""
Authors: Jacobo Wiesner and Vera Casquero
Date: 07/23/2025
Challenge H
"""

import sys
from collections import defaultdict

def build_graph(lines, idx, families):
    """Reads families lines starting at lines[idx] and returns:
    graph: dict mapping each person to sets of neighbors:
    sets are better in this case than lists to avoid repetition and O(1) access.
    graph[name]['parent'], graph[name]['child'], graph[name]['spouse']
    updated idx"""

    graph = defaultdict(lambda: {'parent': set(), 'child': set(), 'spouse': set()}) #mapping to sets

    for i in range(families):
        line = lines[idx].strip()
        idx += 1
        if not line:
            continue

        edited_line   = line.strip() #edit to get parent and children
        colon_idx  = edited_line.find(':')
        parents_str  = edited_line[:colon_idx].strip()
        children_str = edited_line[colon_idx+1:].strip() 

        parents  = parents_str.split()
        children = children_str.split()

        # parent to child and viceversa
        for p in parents:
            for c in children:
                graph[p]['child'].add(c)
                graph[c]['parent'].add(p)

        # spouse to spouse (first two parents)
        if len(parents) >= 2:
            a, b = parents[0], parents[1]
            graph[a]['spouse'].add(b)
            graph[b]['spouse'].add(a)

    return graph, idx

def get_nieces_and_nephews(person, graph):
    """Returns a sorted list of all:
    children of person's siblings
    children of spouse's siblings
    """
    result = set()

    # own side
    for parent in graph[person]['parent']:
        for sib in graph[parent]['child']:
            if sib != person:
                result.update(graph[sib]['child'])

    # spouse side
    for spouse in graph[person]['spouse']:
        for parent in graph[spouse]['parent']:
            for sib in graph[parent]['child']:
                if sib != spouse:
                    result.update(graph[sib]['child'])

    return sorted(result)

def main():
    lines = sys.stdin.read().splitlines()
    index = 0

    while index < len(lines):
        #number of family descriptions
        try:
            families = int(lines[index].strip())
        except (IndexError, ValueError):
            return
        index += 1

        # zero indicates end of all cases
        if families == 0:
            return

        graph, index = build_graph(lines, index, families)

        # number of gift‑givers
        try:
            givers_count = int(lines[index].strip())
        except (IndexError, ValueError):
            return
        index += 1

        for _ in range(givers_count):
            giver = lines[index].strip()
            index += 1

            recipients = get_nieces_and_nephews(giver, graph)
            if recipients:
                print(f"{giver} needs to buy gifts for: {', '.join(recipients)}")
            else:
                print(f"{giver} does not need to buy gifts")

if __name__ == "__main__":
    main()

