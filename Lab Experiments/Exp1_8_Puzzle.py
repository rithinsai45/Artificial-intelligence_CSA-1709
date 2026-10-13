"""
EXPERIMENT 1: 8-PUZZLE PROBLEM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO1
Description: Solving the 8-Puzzle Problem using the A* Search Algorithm
             with Manhattan Distance Heuristic.
"""

import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan_distance(state):
    """Calculates the Manhattan distance heuristic of the given state to the goal."""
    dist = 0
    for idx, val in enumerate(state):
        if val != 0:
            target_idx = val - 1
            curr_r, curr_c = divmod(idx, 3)
            target_r, target_c = divmod(target_idx, 3)
            dist += abs(curr_r - target_r) + abs(curr_c - target_c)
    return dist

def get_neighbors(state):
    """Generates valid next states by moving the blank tile (0)."""
    neighbors = []
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)
    
    directions = [
        ('UP', r - 1, c, zero_idx - 3),
        ('DOWN', r + 1, c, zero_idx + 3),
        ('LEFT', r, c - 1, zero_idx - 1),
        ('RIGHT', r, c + 1, zero_idx + 1),
    ]
    
    for action, new_r, new_c, new_idx in directions:
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append((action, tuple(new_state)))
            
    return neighbors

def print_board(state):
    """Prints the 3x3 puzzle board in formatted grid."""
    print("  +---+---+---+")
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else ' ' for x in state[i:i+3]]
        print(f"  | {' | '.join(row)} |")
        print("  +---+---+---+")

def solve_8_puzzle(start_state):
    """Solves the 8-puzzle using A* Search algorithm."""
    pq = []
    counter = 0
    h_init = manhattan_distance(start_state)
    heapq.heappush(pq, (h_init, 0, counter, start_state, []))
    visited = {start_state: 0}
    
    while pq:
        f, g, _, current, path = heapq.heappop(pq)
        
        if current == GOAL_STATE:
            return path
            
        for action, neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                h = manhattan_distance(neighbor)
                counter += 1
                heapq.heappush(pq, (new_g + h, new_g, counter, neighbor, path + [(action, neighbor)]))
                
    return None

if __name__ == '__main__':
    print("=" * 55)
    print(" EXPERIMENT 1: SOLVING 8-PUZZLE USING A* SEARCH ")
    print("=" * 55)
    
    # An initial state requiring 4 moves to reach goal
    initial_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    
    print("\nInitial State (0 represents empty space):")
    print_board(initial_state)
    
    print("\nGoal State:")
    print_board(GOAL_STATE)
    
    print("\nSearching for optimal solution using A*...")
    solution_path = solve_8_puzzle(initial_state)
    
    if solution_path is not None:
        print(f"\nSolution found in {len(solution_path)} steps!\n")
        current = initial_state
        for step, (action, next_state) in enumerate(solution_path, start=1):
            print(f"Step {step}: Move Blank '{action}'")
            print_board(next_state)
        print("Goal reached successfully!")
    else:
        print("No solution exists for this configuration.")
