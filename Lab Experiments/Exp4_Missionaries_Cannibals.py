"""
EXPERIMENT 4: MISSIONARIES AND CANNIBALS PROBLEM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO3
Description: Solving Missionaries and Cannibals Problem using Breadth-First Search.
"""

from collections import deque

def is_valid(m, c):
    """Checks whether the state violates the safety condition."""
    # If missionaries are present, they must not be outnumbered by cannibals
    if (m > 0 and m < c) or (3 - m > 0 and (3 - m) < (3 - c)):
        return False
    return True

def get_successors(state):
    """
    State: (m_left, c_left, boat_pos)
    boat_pos: 1 for Left bank, 0 for Right bank
    """
    m, c, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []

    for dm, dc in moves:
        if boat == 1:  # Boat moving from Left to Right
            next_m = m - dm
            next_c = c - dc
            next_boat = 0
            move_desc = f"Boat moves Left -> Right carrying {dm} Missionary(ies) and {dc} Cannibal(s)"
        else:          # Boat moving from Right to Left
            next_m = m + dm
            next_c = c + dc
            next_boat = 1
            move_desc = f"Boat moves Right -> Left carrying {dm} Missionary(ies) and {dc} Cannibal(s)"

        if 0 <= next_m <= 3 and 0 <= next_c <= 3:
            if is_valid(next_m, next_c):
                successors.append(((next_m, next_c, next_boat), move_desc))

    return successors

def solve_missionaries_cannibals():
    """Finds the shortest solution path using BFS."""
    initial_state = (3, 3, 1)  # (3M, 3C, Boat on Left)
    goal_state = (0, 0, 0)     # (0M, 0C, Boat on Right)

    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for next_state, desc in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(desc, next_state)]))

    return None

if __name__ == '__main__':
    print("=" * 65)
    print(" EXPERIMENT 4: MISSIONARIES AND CANNIBALS PROBLEM ")
    print("=" * 65)
    print("Rules:")
    print(" - Total 3 Missionaries (M) and 3 Cannibals (C).")
    print(" - Boat capacity: Maximum 2 persons, minimum 1 person.")
    print(" - Cannibals must NEVER outnumber Missionaries on either bank.\n")

    solution = solve_missionaries_cannibals()

    if solution:
        print(f"Optimal solution found in {len(solution)} river crossings!\n")
        print(f"{'Step':<5} | {'Left Bank':<12} | {'Boat':<8} | {'Right Bank':<12} | {'Action Taken'}")
        print("-" * 75)
        print(f"{'0':<5} | {'3M, 3C':<12} | {'Left':<8} | {'0M, 0C':<12} | Initial State")

        for idx, (action, (m, c, b)) in enumerate(solution, start=1):
            boat_str = "Left" if b == 1 else "Right"
            left_str = f"{m}M, {c}C"
            right_str = f"{3-m}M, {3-c}C"
            print(f"{idx:<5} | {left_str:<12} | {boat_str:<8} | {right_str:<12} | {action}")

        print("-" * 75)
        print("Success: All missionaries and cannibals reached the right bank safely!")
    else:
        print("No valid solution found.")
