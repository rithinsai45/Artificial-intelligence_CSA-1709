"""
EXPERIMENT 7: DEPTH FIRST SEARCH (DFS)
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO4
Description: Implementation of Depth First Search (DFS) graph traversal algorithm
             using Recursion and LIFO Stack.
"""

def dfs_recursive(graph, node, visited=None, traversal_order=None):
    """Performs DFS using recursive call stack."""
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(node)
    traversal_order.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

    return traversal_order

def dfs_iterative(graph, start_node):
    """
    Performs DFS iteratively using an explicit LIFO Stack.
    Displays stack contents at each step.
    """
    visited = []
    stack = [start_node]
    seen = set()

    print(f"{'Step':<6} | {'Popped Node':<14} | {'Stack Content':<25} | {'Visited Order'}")
    print("-" * 75)

    step = 1
    while stack:
        current = stack.pop()

        if current not in seen:
            seen.add(current)
            visited.append(current)

            # Push neighbors in reverse order so first neighbor is popped first
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in seen:
                    stack.append(neighbor)

            stack_display = "[" + ", ".join(stack) + "]"
            visited_display = "[" + ", ".join(visited) + "]"
            print(f"{step:<6} | {current:<14} | {stack_display:<25} | {visited_display}")
            step += 1

    return visited

if __name__ == '__main__':
    # Sample Graph representation using Adjacency List
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("=" * 65)
    print(" EXPERIMENT 7: DEPTH FIRST SEARCH (DFS) IMPLEMENTATION ")
    print("=" * 65)
    print("Graph Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  Node {node} -> {neighbors}")

    print("\nExecuting DFS (Iterative using LIFO Stack):\n")
    iterative_order = dfs_iterative(graph, 'A')
    print("-" * 75)
    print(f"Iterative DFS Traversal Result: {' -> '.join(iterative_order)}")

    recursive_order = dfs_recursive(graph, 'A')
    print(f"Recursive DFS Traversal Result: {' -> '.join(recursive_order)}")
    print("\nDFS traversal completed successfully!")
