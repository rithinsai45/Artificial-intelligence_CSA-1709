"""
EXPERIMENT 3: WATER JUG PROBLEM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO2
Description: Solving the Water Jug Problem using State Space Search (Breadth First Search).
"""

from collections import deque

def solve_water_jug(cap_a=4, cap_b=3, target=2):
    """
    Solves the Water Jug problem using Breadth-First Search (BFS).
    cap_a: capacity of jug A (default 4)
    cap_b: capacity of jug B (default 3)
    target: target amount in jug A (default 2)
    """
    # Queue stores: (current_state, path_taken)
    # state is a tuple (a, b)
    queue = deque([((0, 0), [])])
    visited = set([(0, 0)])

    while queue:
        (a, b), path = queue.popleft()

        # Goal check: target amount in either jug (typically jug A)
        if a == target:
            return path + [(f"Target achieved! Jug A contains {target}L", (a, b))]

        # All possible operations (production rules)
        rules = [
            ("Fill Jug A completely", (cap_a, b)),
            ("Fill Jug B completely", (a, cap_b)),
            ("Empty Jug A to ground", (0, b)),
            ("Empty Jug B to ground", (a, 0)),
            # Pour Jug A -> Jug B
            (f"Pour from Jug A to Jug B until B is full or A is empty",
             (a - min(a, cap_b - b), b + min(a, cap_b - b))),
            # Pour Jug B -> Jug A
            (f"Pour from Jug B to Jug A until A is full or B is empty",
             (a + min(b, cap_a - a), b - min(b, cap_a - a)))
        ]

        for rule_name, next_state in rules:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(rule_name, next_state)]))

    return None

if __name__ == '__main__':
    cap_a = 4
    cap_b = 3
    target = 2

    print("=" * 60)
    print(" EXPERIMENT 3: WATER JUG PROBLEM USING STATE SPACE SEARCH ")
    print("=" * 60)
    print(f"Jug A Capacity : {cap_a} Liters")
    print(f"Jug B Capacity : {cap_b} Liters")
    print(f"Target Quantity: {target} Liters in Jug A")
    print(f"Initial State  : Jug A = 0L, Jug B = 0L\n")

    steps = solve_water_jug(cap_a, cap_b, target)

    if steps:
        print(f"Optimal sequence of steps to measure {target} Liters:\n")
        print(f"{'Step':<6} | {'Action Performed':<50} | {'Jug A (4L)':<10} | {'Jug B (3L)':<10}")
        print("-" * 82)
        print(f"{'0':<6} | {'Initial State':<50} | {'0 L':<10} | {'0 L':<10}")
        
        for idx, (action, (a, b)) in enumerate(steps, start=1):
            print(f"{idx:<6} | {action:<50} | {f'{a} L':<10} | {f'{b} L':<10}")
            
        print("-" * 82)
        print("Success: Exact target quantity measured successfully!")
    else:
        print("No solution possible with given jug capacities.")
