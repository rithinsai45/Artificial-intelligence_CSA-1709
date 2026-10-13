"""
EXPERIMENT 8: A* SEARCH ALGORITHM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO4
Description: Implementation of A* Search Algorithm to find the optimal path
             using path cost g(n) and heuristic estimate h(n).
"""

import heapq

def a_star_search(graph, heuristics, start, goal):
    """
    Finds the shortest optimal path from start to goal using A* algorithm.
    f(n) = g(n) + h(n)
    """
    # Priority Queue stores: (f_score, g_score, counter, current_node, path)
    pq = []
    counter = 0
    h_start = heuristics.get(start, 0)
    heapq.heappush(pq, (h_start, 0, counter, start, [start]))

    # Track best g_score for each node
    g_scores = {start: 0}
    closed_set = set()

    print(f"{'Step':<5} | {'Expanded':<10} | {'g(n)':<8} | {'h(n)':<8} | {'f(n)':<8} | {'Current Path'}")
    print("-" * 65)

    step = 1
    while pq:
        f, g, _, current, path = heapq.heappop(pq)

        print(f"{step:<5} | {current:<10} | {g:<8} | {heuristics.get(current, 0):<8} | {f:<8} | {' -> '.join(path)}")
        step += 1

        if current == goal:
            return path, g

        closed_set.add(current)

        for neighbor, weight in graph.get(current, []):
            tentative_g = g + weight

            if neighbor in closed_set and tentative_g >= g_scores.get(neighbor, float('inf')):
                continue

            if tentative_g < g_scores.get(neighbor, float('inf')):
                g_scores[neighbor] = tentative_g
                h = heuristics.get(neighbor, 0)
                counter += 1
                new_f = tentative_g + h
                heapq.heappush(pq, (new_f, tentative_g, counter, neighbor, path + [neighbor]))

    return None, float('inf')

if __name__ == '__main__':
    # Graph with directed weighted edges: (neighbor, cost)
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('B', 2), ('C', 5), ('D', 12)],
        'B': [('C', 2)],
        'C': [('D', 3), ('G', 6)],
        'D': [('G', 1)],
        'G': []
    }

    # Heuristic estimate h(n) to goal 'G'
    heuristics = {
        'S': 7,
        'A': 6,
        'B': 4,
        'C': 3,
        'D': 1,
        'G': 0
    }

    print("=" * 65)
    print(" EXPERIMENT 8: A* SEARCH ALGORITHM IMPLEMENTATION ")
    print("=" * 65)
    print("Graph Structure (Node -> [(Neighbor, Edge Cost), ...]):")
    for node, edges in graph.items():
        print(f"  {node} -> {edges}")

    print("\nHeuristic Values h(n) to Goal 'G':")
    for node, h_val in heuristics.items():
        print(f"  h({node}) = {h_val}")

    print("\nExecuting A* Search from Start 'S' to Goal 'G':\n")
    optimal_path, total_cost = a_star_search(graph, heuristics, 'S', 'G')
    print("-" * 65)

    if optimal_path:
        print(f"\nOptimal Path Found: {' -> '.join(optimal_path)}")
        print(f"Total Minimum Path Cost: {total_cost}")
    else:
        print("Goal is not reachable from start node.")
