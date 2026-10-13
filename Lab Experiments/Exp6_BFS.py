"""
EXPERIMENT 6: BREADTH FIRST SEARCH (BFS)
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO3
Description: Implementation of Breadth First Search (BFS) graph traversal algorithm
             using a FIFO Queue.
"""

from collections import deque

def bfs_traversal(graph, start_node):
    """
    Performs Breadth First Search traversal from start_node.
    Shows the step-by-step state of the FIFO Queue and visited set.
    """
    visited = []
    queue = deque([start_node])
    in_queue_or_visited = set([start_node])

    print(f"{'Step':<6} | {'Current Node':<14} | {'Queue Content':<25} | {'Visited List'}")
    print("-" * 75)

    step = 1
    while queue:
        current = queue.popleft()
        visited.append(current)

        # Explore unvisited neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in in_queue_or_visited:
                in_queue_or_visited.add(neighbor)
                queue.append(neighbor)

        queue_display = "[" + ", ".join(queue) + "]"
        visited_display = "[" + ", ".join(visited) + "]"
        print(f"{step:<6} | {current:<14} | {queue_display:<25} | {visited_display}")
        step += 1

    return visited

def bfs_shortest_path(graph, start, goal):
    """Finds the shortest unweighted path from start to goal using BFS."""
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

if __name__ == '__main__':
    # Sample Graph representation using Adjacency List
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("=" * 65)
    print(" EXPERIMENT 6: BREADTH FIRST SEARCH (BFS) IMPLEMENTATION ")
    print("=" * 65)
    print("Graph Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  Node {node} -> {neighbors}")
    print("\nStarting BFS traversal from Node 'A':\n")

    traversal_order = bfs_traversal(graph, 'A')
    print("-" * 75)
    print(f"\nFinal BFS Traversal Order: {' -> '.join(traversal_order)}")

    # Finding shortest path between A and F
    target = 'F'
    path = bfs_shortest_path(graph, 'A', target)
    print(f"Shortest path from 'A' to '{target}' using BFS: {' -> '.join(path)}")
