# CSA17 — ARTIFICIAL INTELLIGENCE LAB OBSERVATION MANUAL
### SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES (SIMATS ENGINEERING)
**Department of Computer Science and Engineering**

- **Student Name:** Vishal Balaji J
- **Register Number:** 192525014
- **Course Code & Title:** CSA17 — Artificial Intelligence
- **Degree & Branch:** B.Tech Computer Science and Engineering

---

## INDEX / EXPERIMENT SCHEDULE

| Exp. No. | Submission Date | Experiment Title | Course Outcome | Status |
|:---:|:---:|:---|:---:|:---:|
| **1** | 13.10.2026 | 8-Puzzle Problem using A* Search | CO1 | Completed |
| **2** | 13.10.2026 | 8-Queen Problem using Backtracking | CO1 | Completed |
| **3** | 13.10.2026 | Water Jug Problem using State Space Search | CO2 | Completed |
| **4** | 13.10.2026 | Missionaries and Cannibals Problem | CO3 | Completed |
| **5** | 13.10.2026 | Vacuum Cleaner Agent (Vacuum World) | CO3 | Completed |
| **6** | 15.10.2026 | Breadth First Search (BFS) Implementation | CO3 | Completed |
| **7** | 15.10.2026 | Depth First Search (DFS) Implementation | CO4 | Completed |
| **8** | 15.10.2026 | A* Search Algorithm on Weighted Graph | CO4 | Completed |
| **9** | 15.10.2026 | Crypt-Arithmetic Problem (SEND + MORE = MONEY) | CO2 | Completed |
| **10** | 15.10.2026 | Travelling Salesman Problem (TSP) | CO4 | Completed |

---

## EXPERIMENT 1: 8-PUZZLE PROBLEM USING A* SEARCH

- **Date:** 13.10.2026
- **Course Outcome:** CO1
- **Submission Target:** Assigned for 13.10.2026

### AIM
To write and execute a Python program to solve the 8-puzzle problem using the A* Search Algorithm with the Manhattan Distance heuristic.

### PROCEDURE
- Understand the 8-puzzle board configuration consisting of a 3x3 grid with tiles numbered 1 to 8 and one empty blank space (represented by 0).
- Define the initial state and the target goal state.
- Implement the Manhattan Distance heuristic function h(n) calculating the sum of absolute horizontal and vertical distances of tiles from their goal positions.
- Generate valid successor states by sliding the blank tile Up, Down, Left, or Right.
- Employ a priority queue (min-heap) to explore states with the minimum evaluation cost f(n) = g(n) + h(n).
- Maintain a visited set to avoid redundant state expansions and cycles.
- Execute the program in Python IDLE and record the optimal sequence of puzzle configurations.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Define the Goal State as [[1, 2, 3], [4, 5, 6], [7, 8, 0]].
Step 3: Define heuristic function h(state) returning the total Manhattan distance of all tiles from their goal coordinates.
Step 4: Initialize a Priority Queue (Open List) and push the Initial State with g = 0 and f = h(initial).
Step 5: Initialize a Visited Dictionary (Closed List) to track minimum path costs.
Step 6: While the Priority Queue is not empty:
       a. Pop the node with the minimum f-score.
       b. If current state equals Goal State, reconstruct the solution path and terminate.
       c. For each valid move (UP, DOWN, LEFT, RIGHT):
          i. Calculate tentative cost g_new = g + 1.
          ii. If neighbor is unvisited or g_new < visited[neighbor], update visited and push to Priority Queue.
Step 7: Display the step-by-step tile moves and final solved board.
Step 8: Stop the program.
```

### SOURCE CODE
```python
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

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=======================================================
 EXPERIMENT 1: SOLVING 8-PUZZLE USING A* SEARCH 
=======================================================

Initial State (0 represents empty space):
  +---+---+---+
  | 1 | 2 | 3 |
  +---+---+---+
  |   | 4 | 6 |
  +---+---+---+
  | 7 | 5 | 8 |
  +---+---+---+

Goal State:
  +---+---+---+
  | 1 | 2 | 3 |
  +---+---+---+
  | 4 | 5 | 6 |
  +---+---+---+
  | 7 | 8 |   |
  +---+---+---+

Searching for optimal solution using A*...

Solution found in 3 steps!

Step 1: Move Blank 'RIGHT'
  +---+---+---+
  | 1 | 2 | 3 |
  +---+---+---+
  | 4 |   | 6 |
  +---+---+---+
  | 7 | 5 | 8 |
  +---+---+---+
Step 2: Move Blank 'DOWN'
  +---+---+---+
  | 1 | 2 | 3 |
  +---+---+---+
  | 4 | 5 | 6 |
  +---+---+---+
  | 7 |   | 8 |
  +---+---+---+
Step 3: Move Blank 'RIGHT'
  +---+---+---+
  | 1 | 2 | 3 |
  +---+---+---+
  | 4 | 5 | 6 |
  +---+---+---+
  | 7 | 8 |   |
  +---+---+---+
Goal reached successfully!
```

### RESULT
The Python program to solve the 8-puzzle problem using the A* Search algorithm was successfully executed in Python IDLE. The optimal path to reach the goal state was determined in 3 steps.

---

## EXPERIMENT 2: 8-QUEEN PROBLEM USING BACKTRACKING

- **Date:** 13.10.2026
- **Course Outcome:** CO1
- **Submission Target:** Assigned for 13.10.2026

### AIM
To write and execute a Python program to solve the 8-Queen problem using the Backtracking algorithm.

### PROCEDURE
- Understand the problem: Place 8 queens on an 8x8 chessboard such that no two queens attack each other.
- Formulate non-attacking constraints: No two queens can share the same row, same column, or same diagonal.
- Develop the is_safe() utility function to check whether a queen can be safely placed in board[row][col] without conflicting with previously placed queens.
- Use a recursive backtracking approach to place queens column by column.
- If placing a queen leads to a valid state, proceed to the next column. If no safe row exists, backtrack by removing the previously placed queen.
- Execute the code in Python IDLE, find all valid solutions (92 configurations), and display the board matrices.
- Record the output and verify the queen coordinates.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Initialize an 8x8 chessboard matrix with all cells set to 0.
Step 3: Define function is_safe(board, row, col):
       a. Check if any queen exists in the same row on the left columns.
       b. Check if any queen exists on the upper diagonal to the left.
       c. Check if any queen exists on the lower diagonal to the left.
       d. Return True if all checks pass; otherwise return False.
Step 4: Define recursive function backtrack(col):
       a. If col >= 8, all 8 queens are safely placed; save the board configuration.
       b. For each row from 0 to 7:
          i. If is_safe(board, row, col) is True:
             - Place queen: board[row][col] = 1.
             - Recursively call backtrack(col + 1).
             - Backtrack: board[row][col] = 0.
Step 5: Display the visual 8x8 board representation and queen coordinates.
Step 6: Stop the program.
```

### SOURCE CODE
```python
"""
EXPERIMENT 2: 8-QUEEN PROBLEM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO1
Description: Solving the 8-Queens Problem using Backtracking Algorithm.
"""

def is_safe(board, row, col, n=8):
    """Checks if a queen can be safely placed at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board, n=8):
    """Prints the chessboard visually."""
    print("   " + " ".join([f"C{c}" for c in range(n)]))
    print("  +" + "---" * n + "+")
    for r in range(n):
        row_str = " ".join([" Q" if board[r][c] == 1 else " ." for c in range(n)])
        print(f"R{r}|{row_str} |")
    print("  +" + "---" * n + "+")

def solve_n_queens_all(n=8):
    """Finds all valid solutions for N-Queens problem using backtracking."""
    board = [[0] * n for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col >= n:
            solutions.append([row[:] for row in board])
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0  # Backtrack

    backtrack(0)
    return solutions

if __name__ == '__main__':
    N = 8
    print("=" * 55)
    print(f" EXPERIMENT 2: SOLVING {N}-QUEENS PROBLEM USING BACKTRACKING ")
    print("=" * 55)
    print(f"Aim: Place {N} queens on an {N}x{N} chessboard such that")
    print("     no two queens attack each other.\n")

    solutions = solve_n_queens_all(N)
    print(f"Total valid non-attacking solutions found: {len(solutions)}\n")

    print("Displaying Solution 1:")
    sol1 = solutions[0]
    print_board(sol1, N)

    print("\nQueen Positions (Row, Column):")
    for r in range(N):
        for c in range(N):
            if sol1[r][c] == 1:
                print(f"  Queen {r + 1}: Row {r}, Column {c}")

    print("\nDisplaying Solution 2 (Alternative configuration):")
    sol2 = solutions[1]
    print_board(sol2, N)
    print("\nProblem solved successfully!")

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=======================================================
 EXPERIMENT 2: SOLVING 8-QUEENS PROBLEM USING BACKTRACKING 
=======================================================
Aim: Place 8 queens on an 8x8 chessboard such that
     no two queens attack each other.

Total valid non-attacking solutions found: 92

Displaying Solution 1:
   C0 C1 C2 C3 C4 C5 C6 C7
  +------------------------+
R0| Q  .  .  .  .  .  .  . |
R1| .  .  .  .  .  .  Q  . |
R2| .  .  .  .  Q  .  .  . |
R3| .  .  .  .  .  .  .  Q |
R4| .  Q  .  .  .  .  .  . |
R5| .  .  .  Q  .  .  .  . |
R6| .  .  .  .  .  Q  .  . |
R7| .  .  Q  .  .  .  .  . |
  +------------------------+

Queen Positions (Row, Column):
  Queen 1: Row 0, Column 0
  Queen 2: Row 1, Column 6
  Queen 3: Row 2, Column 4
  Queen 4: Row 3, Column 7
  Queen 5: Row 4, Column 1
  Queen 6: Row 5, Column 3
  Queen 7: Row 6, Column 5
  Queen 8: Row 7, Column 2

Displaying Solution 2 (Alternative configuration):
   C0 C1 C2 C3 C4 C5 C6 C7
  +------------------------+
R0| Q  .  .  .  .  .  .  . |
R1| .  .  .  .  .  .  Q  . |
R2| .  .  .  Q  .  .  .  . |
R3| .  .  .  .  .  Q  .  . |
R4| .  .  .  .  .  .  .  Q |
R5| .  Q  .  .  .  .  .  . |
R6| .  .  .  .  Q  .  .  . |
R7| .  .  Q  .  .  .  .  . |
  +------------------------+

Problem solved successfully!
```

### RESULT
The Python program for the 8-Queen problem was successfully developed and executed in Python IDLE. All 92 non-attacking queen solutions were identified and displayed.

---

## EXPERIMENT 3: WATER JUG PROBLEM USING STATE SPACE SEARCH

- **Date:** 13.10.2026
- **Course Outcome:** CO2
- **Submission Target:** Assigned for 13.10.2026

### AIM
To write and execute a Python program to solve the Water Jug Problem using state space search (Breadth First Search).

### PROCEDURE
- Identify the given parameters: Jug A capacity = 4 Liters, Jug B capacity = 3 Liters, Target quantity = 2 Liters in Jug A.
- Model state as a tuple (a, b) representing the current volume of water in Jug A and Jug B.
- Define production rules: Fill Jug A, Fill Jug B, Empty Jug A, Empty Jug B, Pour Jug A to Jug B, Pour Jug B to Jug A.
- Use Breadth-First Search (BFS) with a FIFO queue to systematically explore reachable states starting from (0, 0).
- Check for the goal state (2, b) and reconstruct the step-by-step operations.
- Run the program in Python IDLE and observe the state transitions.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Initialize capacities cap_a = 4, cap_b = 3, target = 2.
Step 3: Initialize BFS Queue with initial state ((0, 0), []) and a visited set.
Step 4: While Queue is not empty:
       a. Dequeue current state (a, b) and operation path.
       b. If a == target, return the solution path.
       c. Generate all 6 possible successor states:
          1. Fill A: (cap_a, b)
          2. Fill B: (a, cap_b)
          3. Empty A: (0, b)
          4. Empty B: (a, 0)
          5. Pour A -> B: (a - pour, b + pour) where pour = min(a, cap_b - b)
          6. Pour B -> A: (a + pour, b - pour) where pour = min(b, cap_a - a)
       d. For each unvisited successor state, add to visited set and enqueue.
Step 5: Print the formatted table of steps, actions taken, and jug volumes.
Step 6: Stop the program.
```

### SOURCE CODE
```python
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

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
============================================================
 EXPERIMENT 3: WATER JUG PROBLEM USING STATE SPACE SEARCH 
============================================================
Jug A Capacity : 4 Liters
Jug B Capacity : 3 Liters
Target Quantity: 2 Liters in Jug A
Initial State  : Jug A = 0L, Jug B = 0L

Optimal sequence of steps to measure 2 Liters:

Step   | Action Performed                                   | Jug A (4L) | Jug B (3L)
----------------------------------------------------------------------------------
0      | Initial State                                      | 0 L        | 0 L       
1      | Fill Jug A completely                              | 4 L        | 0 L       
2      | Pour from Jug A to Jug B until B is full or A is empty | 1 L        | 3 L       
3      | Empty Jug B to ground                              | 1 L        | 0 L       
4      | Pour from Jug A to Jug B until B is full or A is empty | 0 L        | 1 L       
5      | Fill Jug A completely                              | 4 L        | 1 L       
6      | Pour from Jug A to Jug B until B is full or A is empty | 2 L        | 3 L       
7      | Target achieved! Jug A contains 2L                 | 2 L        | 3 L       
----------------------------------------------------------------------------------
Success: Exact target quantity measured successfully!
```

### RESULT
The Water Jug problem was successfully solved in Python using BFS. Exactly 2 Liters were measured in Jug A in 6 operational steps without measuring marks.

---

## EXPERIMENT 4: MISSIONARIES AND CANNIBALS PROBLEM

- **Date:** 13.10.2026
- **Course Outcome:** CO3
- **Submission Target:** Assigned for 13.10.2026

### AIM
To write and execute a Python program to solve the Missionaries and Cannibals problem using state space search.

### PROCEDURE
- Understand the problem constraints: 3 Missionaries (M) and 3 Cannibals (C) are on the left bank and must cross to the right bank using a boat carrying at most 2 people.
- Safety rule: If missionaries are present on either bank, they must never be outnumbered by cannibals (M >= C).
- Represent state as (m_left, c_left, boat_pos) where boat_pos is 1 (Left bank) or 0 (Right bank).
- Define valid boat movements: (1,0), (2,0), (0,1), (0,2), (1,1).
- Implement BFS to find the shortest safe crossing sequence from (3,3,1) to (0,0,0).
- Execute the program in Python IDLE and record the river crossing schedule.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Define initial state as (3, 3, 1) and goal state as (0, 0, 0).
Step 3: Define validation function is_valid(m, c):
       - If m > 0 and m < c: return False (Missionaries eaten on left bank).
       - If (3 - m) > 0 and (3 - m) < (3 - c): return False (Missionaries eaten on right bank).
       - Else return True.
Step 4: Initialize BFS queue with (initial_state, []) and add initial state to visited set.
Step 5: While queue is not empty:
       a. Dequeue (current_state, path).
       b. If current_state == (0, 0, 0), return path.
       c. For each possible boat move (dm, dc) in [(1,0), (2,0), (0,1), (0,2), (1,1)]:
          - Compute next state depending on boat direction.
          - If valid and unvisited, add to visited set and enqueue.
Step 6: Display the step-by-step river crossing log.
Step 7: Stop the program.
```

### SOURCE CODE
```python
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

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=================================================================
 EXPERIMENT 4: MISSIONARIES AND CANNIBALS PROBLEM 
=================================================================
Rules:
 - Total 3 Missionaries (M) and 3 Cannibals (C).
 - Boat capacity: Maximum 2 persons, minimum 1 person.
 - Cannibals must NEVER outnumber Missionaries on either bank.

Optimal solution found in 11 river crossings!

Step  | Left Bank    | Boat     | Right Bank   | Action Taken
---------------------------------------------------------------------------
0     | 3M, 3C       | Left     | 0M, 0C       | Initial State
1     | 3M, 1C       | Right    | 0M, 2C       | Boat moves Left -> Right carrying 0 Missionary(ies) and 2 Cannibal(s)
2     | 3M, 2C       | Left     | 0M, 1C       | Boat moves Right -> Left carrying 0 Missionary(ies) and 1 Cannibal(s)
3     | 3M, 0C       | Right    | 0M, 3C       | Boat moves Left -> Right carrying 0 Missionary(ies) and 2 Cannibal(s)
4     | 3M, 1C       | Left     | 0M, 2C       | Boat moves Right -> Left carrying 0 Missionary(ies) and 1 Cannibal(s)
5     | 1M, 1C       | Right    | 2M, 2C       | Boat moves Left -> Right carrying 2 Missionary(ies) and 0 Cannibal(s)
6     | 2M, 2C       | Left     | 1M, 1C       | Boat moves Right -> Left carrying 1 Missionary(ies) and 1 Cannibal(s)
7     | 0M, 2C       | Right    | 3M, 1C       | Boat moves Left -> Right carrying 2 Missionary(ies) and 0 Cannibal(s)
8     | 0M, 3C       | Left     | 3M, 0C       | Boat moves Right -> Left carrying 0 Missionary(ies) and 1 Cannibal(s)
9     | 0M, 1C       | Right    | 3M, 2C       | Boat moves Left -> Right carrying 0 Missionary(ies) and 2 Cannibal(s)
10    | 1M, 1C       | Left     | 2M, 2C       | Boat moves Right -> Left carrying 1 Missionary(ies) and 0 Cannibal(s)
11    | 0M, 0C       | Right    | 3M, 3C       | Boat moves Left -> Right carrying 1 Missionary(ies) and 1 Cannibal(s)
---------------------------------------------------------------------------
Success: All missionaries and cannibals reached the right bank safely!
```

### RESULT
The Missionaries and Cannibals problem was successfully solved using Breadth-First Search in Python IDLE. All 6 individuals crossed safely in 11 boat trips.

---

## EXPERIMENT 5: VACUUM CLEANER PROBLEM (VACUUM WORLD)

- **Date:** 13.10.2026
- **Course Outcome:** CO3
- **Submission Target:** Assigned for 13.10.2026

### AIM
To write and execute a Python program to implement the Vacuum Cleaner reflex agent in a two-room environment.

### PROCEDURE
- Formulate the environment: Two rooms A and B, where each room can be either 'Clean' or 'Dirty'.
- Define the agent percept: Current location (A or B) and current room status ('Clean' or 'Dirty').
- Formulate the condition-action reflex rules:
-    - If current room is 'Dirty', perform action 'SUCK'.
-    - If current room is 'Clean' and location is 'A', perform action 'RIGHT'.
-    - If current room is 'Clean' and location is 'B', perform action 'LEFT'.
- Simulate agent interactions under multiple starting conditions (both dirty, one clean, etc.).
- Record the action logs and environment status changes until all rooms are clean.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Create VacuumCleanerAgent class with location and cost tracker.
Step 3: Define reflex_action(status) method:
       - If status == 'Dirty', return 'SUCK'.
       - Else if location == 'A', return 'RIGHT'.
       - Else if location == 'B', return 'LEFT'.
Step 4: Define simulation loop:
       - While Room A is 'Dirty' or Room B is 'Dirty':
         a. Sense current room status.
         b. Invoke reflex_action().
         c. Update room status to 'Clean' if 'SUCK' was chosen.
         d. Update agent position if movement action was chosen.
         e. Increment agent cost counter and log state.
Step 5: Print final summary showing all rooms clean and total cost.
Step 6: Stop the program.
```

### SOURCE CODE
```python
"""
EXPERIMENT 5: VACUUM CLEANER PROBLEM (VACUUM WORLD)
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO3
Description: Implementation of Reflex Vacuum Cleaner Agent in a 2-room environment.
"""

class VacuumCleanerAgent:
    def __init__(self, start_location='A'):
        self.location = start_location
        self.cost = 0

    def reflex_action(self, status):
        """
        Determines the agent's action based on current percept (location, status).
        Rule 1: If current room is Dirty -> Suck dirt.
        Rule 2: If current room is Clean and location is A -> Move Right.
        Rule 3: If current room is Clean and location is B -> Move Left.
        """
        if status == 'Dirty':
            return 'SUCK'
        elif self.location == 'A':
            return 'RIGHT'
        elif self.location == 'B':
            return 'LEFT'

def simulate_environment(initial_location, state_a, state_b):
    """Simulates the vacuum agent until both rooms are Clean."""
    env = {'A': state_a, 'B': state_b}
    agent = VacuumCleanerAgent(initial_location)
    step = 1

    print(f"\n--- Simulation: Agent starting in Room {initial_location} ---")
    print(f"Initial State -> Room A: {env['A']}, Room B: {env['B']}")
    print(f"{'Step':<6} | {'Agent At':<10} | {'Percept':<10} | {'Action Taken':<14} | {'Environment State'}")
    print("-" * 65)

    # Continue until both rooms are clean
    while env['A'] == 'Dirty' or env['B'] == 'Dirty':
        current_loc = agent.location
        current_status = env[current_loc]
        action = agent.reflex_action(current_status)

        if action == 'SUCK':
            env[current_loc] = 'Clean'
            action_desc = f"Cleaned {current_loc}"
            agent.cost += 1
        elif action == 'RIGHT':
            agent.location = 'B'
            action_desc = "Moved -> B"
            agent.cost += 1
        elif action == 'LEFT':
            agent.location = 'A'
            action_desc = "Moved -> A"
            agent.cost += 1

        print(f"{step:<6} | {current_loc:<10} | {current_status:<10} | {action_desc:<14} | Room A: {env['A']}, Room B: {env['B']}")
        step += 1

    print("-" * 65)
    print(f"Goal Reached: All rooms are Clean! Total Action Cost = {agent.cost}")

if __name__ == '__main__':
    print("=" * 65)
    print(" EXPERIMENT 5: VACUUM CLEANER PROBLEM (REFLEX AGENT) ")
    print("=" * 65)
    print("Environment: 2 Rooms (A and B).")
    print("Possible states per room: Clean or Dirty.")
    print("Agent actions: SUCK, RIGHT, LEFT.\n")

    # Case 1: Both rooms dirty, agent in A
    print(">>> Test Case 1: Agent in Room A, Both rooms are Dirty")
    simulate_environment('A', 'Dirty', 'Dirty')

    # Case 2: Agent in Room B, Room A Clean, Room B Dirty
    print("\n>>> Test Case 2: Agent in Room B, Room A Clean, Room B Dirty")
    simulate_environment('B', 'Clean', 'Dirty')

    # Case 3: Agent in Room B, Room A Dirty, Room B Clean
    print("\n>>> Test Case 3: Agent in Room B, Room A Dirty, Room B Clean")
    simulate_environment('B', 'Dirty', 'Clean')

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=================================================================
 EXPERIMENT 5: VACUUM CLEANER PROBLEM (REFLEX AGENT) 
=================================================================
Environment: 2 Rooms (A and B).
Possible states per room: Clean or Dirty.
Agent actions: SUCK, RIGHT, LEFT.

>>> Test Case 1: Agent in Room A, Both rooms are Dirty

--- Simulation: Agent starting in Room A ---
Initial State -> Room A: Dirty, Room B: Dirty
Step   | Agent At   | Percept    | Action Taken   | Environment State
-----------------------------------------------------------------
1      | A          | Dirty      | Cleaned A      | Room A: Clean, Room B: Dirty
2      | A          | Clean      | Moved -> B     | Room A: Clean, Room B: Dirty
3      | B          | Dirty      | Cleaned B      | Room A: Clean, Room B: Clean
-----------------------------------------------------------------
Goal Reached: All rooms are Clean! Total Action Cost = 3

>>> Test Case 2: Agent in Room B, Room A Clean, Room B Dirty

--- Simulation: Agent starting in Room B ---
Initial State -> Room A: Clean, Room B: Dirty
Step   | Agent At   | Percept    | Action Taken   | Environment State
-----------------------------------------------------------------
1      | B          | Dirty      | Cleaned B      | Room A: Clean, Room B: Clean
-----------------------------------------------------------------
Goal Reached: All rooms are Clean! Total Action Cost = 1

>>> Test Case 3: Agent in Room B, Room A Dirty, Room B Clean

--- Simulation: Agent starting in Room B ---
Initial State -> Room A: Dirty, Room B: Clean
Step   | Agent At   | Percept    | Action Taken   | Environment State
-----------------------------------------------------------------
1      | B          | Clean      | Moved -> A     | Room A: Dirty, Room B: Clean
2      | A          | Dirty      | Cleaned A      | Room A: Clean, Room B: Clean
-----------------------------------------------------------------
Goal Reached: All rooms are Clean! Total Action Cost = 2
```

### RESULT
The Vacuum Cleaner reflex agent was successfully simulated in Python IDLE. The agent effectively perceived its environment, cleaned both rooms, and minimized movement costs across multiple test scenarios.

---

## EXPERIMENT 6: BREADTH FIRST SEARCH (BFS) IMPLEMENTATION

- **Date:** 15.10.2026
- **Course Outcome:** CO3
- **Submission Target:** Assigned for 15.10.2026

### AIM
To write and execute a Python program to implement the Breadth First Search (BFS) graph traversal algorithm.

### PROCEDURE
- Represent the graph using an Adjacency List (Python dictionary).
- Select a starting node to begin traversal.
- Use a FIFO (First-In, First-Out) queue from the collections module (deque) to manage frontier nodes.
- Maintain a visited list to prevent revisiting already explored nodes.
- Explore all neighbor nodes level by level, printing queue states at each step.
- Implement a shortest path utility using BFS.
- Execute the program in Python IDLE and record the traversal sequence.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Represent graph as adjacency list with nodes and neighbor lists.
Step 3: Define bfs_traversal(graph, start_node):
       a. Initialize empty list visited = [].
       b. Initialize FIFO queue with start_node.
       c. Mark start_node as seen.
Step 4: While queue is not empty:
       a. Dequeue current node.
       b. Append current node to visited list.
       c. For each unvisited neighbor of current node:
          - Mark neighbor as seen.
          - Enqueue neighbor into queue.
Step 5: Output the step-by-step queue contents and final traversal path.
Step 6: Stop the program.
```

### SOURCE CODE
```python
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

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=================================================================
 EXPERIMENT 6: BREADTH FIRST SEARCH (BFS) IMPLEMENTATION 
=================================================================
Graph Adjacency List:
  Node A -> ['B', 'C']
  Node B -> ['A', 'D', 'E']
  Node C -> ['A', 'F']
  Node D -> ['B']
  Node E -> ['B', 'F']
  Node F -> ['C', 'E']

Starting BFS traversal from Node 'A':

Step   | Current Node   | Queue Content             | Visited List
---------------------------------------------------------------------------
1      | A              | [B, C]                    | [A]
2      | B              | [C, D, E]                 | [A, B]
3      | C              | [D, E, F]                 | [A, B, C]
4      | D              | [E, F]                    | [A, B, C, D]
5      | E              | [F]                       | [A, B, C, D, E]
6      | F              | []                        | [A, B, C, D, E, F]
---------------------------------------------------------------------------

Final BFS Traversal Order: A -> B -> C -> D -> E -> F
Shortest path from 'A' to 'F' using BFS: A -> C -> F
```

### RESULT
The Breadth First Search (BFS) algorithm was successfully implemented and executed in Python IDLE. The graph was traversed level by level producing the order: A -> B -> C -> D -> E -> F.

---

## EXPERIMENT 7: DEPTH FIRST SEARCH (DFS) IMPLEMENTATION

- **Date:** 15.10.2026
- **Course Outcome:** CO4
- **Submission Target:** Assigned for 15.10.2026

### AIM
To write and execute a Python program to implement the Depth First Search (DFS) graph traversal algorithm.

### PROCEDURE
- Represent the directed/undirected graph as an adjacency list.
- Implement DFS using both recursive call stack and explicit LIFO stack.
- Begin exploration from a designated root node.
- Traverse as deeply as possible along each branch before backtracking.
- Maintain a visited set to avoid infinite loops and redundant exploration.
- Run the program in Python IDLE, compare iterative and recursive results, and record outputs.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Define graph structure using an adjacency dictionary.
Step 3: Recursive Approach:
       a. Define dfs_recursive(graph, node, visited):
       b. Mark node as visited.
       c. For each unvisited neighbor, recursively call dfs_recursive().
Step 4: Iterative Approach (LIFO Stack):
       a. Initialize stack = [start_node] and seen = set().
       b. While stack is not empty:
          i. Pop top node from stack.
          ii. If not in seen, mark as seen and add to visited list.
          iii. Push unvisited neighbors onto stack in reverse order.
Step 5: Display the step-by-step stack states and final traversal order.
Step 6: Stop the program.
```

### SOURCE CODE
```python
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

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=================================================================
 EXPERIMENT 7: DEPTH FIRST SEARCH (DFS) IMPLEMENTATION 
=================================================================
Graph Adjacency List:
  Node A -> ['B', 'C']
  Node B -> ['D', 'E']
  Node C -> ['F']
  Node D -> []
  Node E -> ['F']
  Node F -> []

Executing DFS (Iterative using LIFO Stack):

Step   | Popped Node    | Stack Content             | Visited Order
---------------------------------------------------------------------------
1      | A              | [C, B]                    | [A]
2      | B              | [C, E, D]                 | [A, B]
3      | D              | [C, E]                    | [A, B, D]
4      | E              | [C, F]                    | [A, B, D, E]
5      | F              | [C]                       | [A, B, D, E, F]
6      | C              | []                        | [A, B, D, E, F, C]
---------------------------------------------------------------------------
Iterative DFS Traversal Result: A -> B -> D -> E -> F -> C
Recursive DFS Traversal Result: A -> B -> D -> E -> F -> C

DFS traversal completed successfully!
```

### RESULT
The Depth First Search (DFS) algorithm was successfully implemented in Python IDLE using both recursive and iterative stack methods. Both methods verified identical deep traversal paths.

---

## EXPERIMENT 8: A* SEARCH ALGORITHM IMPLEMENTATION

- **Date:** 15.10.2026
- **Course Outcome:** CO4
- **Submission Target:** Assigned for 15.10.2026

### AIM
To write and execute a Python program to implement the A* Search Algorithm on a weighted graph with heuristics.

### PROCEDURE
- Construct a weighted graph with edge costs g(n) and heuristic estimates h(n) to the goal node.
- Understand the evaluation function f(n) = g(n) + h(n), balancing actual path cost and heuristic prediction.
- Initialize a Priority Queue (Open List) containing the start node.
- Maintain a Closed List to store already evaluated nodes and prevent suboptimal re-expansions.
- Pop the node with minimum f(n), examine outgoing edges, and update path costs.
- Terminate when the goal node is popped from the priority queue.
- Display expansion steps, optimal path, and minimum total cost.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Define graph with weighted edges and heuristic table h(n).
Step 3: Define a_star_search(graph, heuristics, start, goal):
       a. Push start node to priority queue with f = h(start), g = 0.
       b. Initialize g_scores dictionary with g_scores[start] = 0.
       c. Initialize closed_set = set().
Step 4: While priority queue is not empty:
       a. Pop node with lowest f-score.
       b. If current node == goal, return reconstructed path and cost g.
       c. Add current node to closed_set.
       d. For each (neighbor, weight) from current node:
          i. Calculate tentative_g = g + weight.
          ii. If tentative_g < g_scores[neighbor]:
              - Update g_scores[neighbor] = tentative_g.
              - Calculate new_f = tentative_g + h(neighbor).
              - Push neighbor into priority queue.
Step 5: Display step-by-step evaluation table and optimal path.
Step 6: Stop the program.
```

### SOURCE CODE
```python
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

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=================================================================
 EXPERIMENT 8: A* SEARCH ALGORITHM IMPLEMENTATION 
=================================================================
Graph Structure (Node -> [(Neighbor, Edge Cost), ...]):
  S -> [('A', 1), ('B', 4)]
  A -> [('B', 2), ('C', 5), ('D', 12)]
  B -> [('C', 2)]
  C -> [('D', 3), ('G', 6)]
  D -> [('G', 1)]
  G -> []

Heuristic Values h(n) to Goal 'G':
  h(S) = 7
  h(A) = 6
  h(B) = 4
  h(C) = 3
  h(D) = 1
  h(G) = 0

Executing A* Search from Start 'S' to Goal 'G':

Step  | Expanded   | g(n)     | h(n)     | f(n)     | Current Path
-----------------------------------------------------------------
1     | S          | 0        | 7        | 7        | S
2     | A          | 1        | 6        | 7        | S -> A
3     | B          | 3        | 4        | 7        | S -> A -> B
4     | B          | 4        | 4        | 8        | S -> B
5     | C          | 5        | 3        | 8        | S -> A -> B -> C
6     | C          | 6        | 3        | 9        | S -> A -> C
7     | D          | 8        | 1        | 9        | S -> A -> B -> C -> D
8     | G          | 9        | 0        | 9        | S -> A -> B -> C -> D -> G
-----------------------------------------------------------------

Optimal Path Found: S -> A -> B -> C -> D -> G
Total Minimum Path Cost: 9
```

### RESULT
The A* Search algorithm was successfully executed in Python IDLE. The optimal path from Start 'S' to Goal 'G' was determined as S -> A -> B -> C -> D -> G with an optimal total cost of 9.

---

## EXPERIMENT 9: CRYPT-ARITHMETIC PROBLEM (SEND + MORE = MONEY)

- **Date:** 15.10.2026
- **Course Outcome:** CO2
- **Submission Target:** Assigned for 15.10.2026

### AIM
To write and execute a Python program to solve the Crypt-Arithmetic Problem using Constraint Satisfaction and Backtracking.

### PROCEDURE
- Understand the puzzle: SEND + MORE = MONEY where each distinct letter represents a unique decimal digit (0 to 9).
- Identify constraints:
-    - Unique digit per letter across {S, E, N, D, M, O, R, Y}.
-    - Leading letters S and M must not be 0.
-    - The arithmetic summation constraint: SEND + MORE == MONEY.
- Formulate search space using permutations of digits and evaluate validity.
- Run the program in Python IDLE and verify the resulting digit assignments.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Define unique letters list ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'].
Step 3: Iterate through permutations of digits (0 to 9) of length 8.
Step 4: Map each permutation to the letter list.
Step 5: Check leading digit constraint: if S == 0 or M == 0, continue.
Step 6: Calculate numerical values:
       - SEND = 1000*S + 100*E + 10*N + D
       - MORE = 1000*M + 100*O + 10*R + E
       - MONEY = 10000*M + 1000*O + 100*N + 10*E + Y
Step 7: If SEND + MORE == MONEY, output the solution and terminate.
Step 8: Stop the program.
```

### SOURCE CODE
```python
"""
EXPERIMENT 9 (SYLLABUS EXP 4): CRYPT-ARITHMETIC PROBLEM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO2
Description: Solving Crypt-Arithmetic Problem (SEND + MORE = MONEY)
             using Constraint Satisfaction and Backtracking.
"""

from itertools import permutations

def solve_cryptarithmetic():
    """
    Solves SEND + MORE = MONEY
    Constraints:
      - Unique digit (0-9) for each letter: S, E, N, D, M, O, R, Y
      - Leading letters S and M cannot be 0
    """
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading characters cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        send = (mapping['S'] * 1000 +
                mapping['E'] * 100 +
                mapping['N'] * 10 +
                mapping['D'])

        more = (mapping['M'] * 1000 +
                mapping['O'] * 100 +
                mapping['R'] * 10 +
                mapping['E'])

        money = (mapping['M'] * 10000 +
                 mapping['O'] * 1000 +
                 mapping['N'] * 100 +
                 mapping['E'] * 10 +
                 mapping['Y'])

        if send + more == money:
            return mapping, send, more, money

    return None, None, None, None

if __name__ == '__main__':
    print("=" * 60)
    print(" EXPERIMENT 9: CRYPT-ARITHMETIC PROBLEM (SEND + MORE = MONEY) ")
    print("=" * 60)
    print("Problem Equation:\n    SEND\n  + MORE\n  ------\n   MONEY\n")
    print("Solving using Constraint Satisfaction Search...")

    mapping, send, more, money = solve_cryptarithmetic()

    if mapping:
        print("\nSolution Found:")
        print("-" * 35)
        for letter in sorted(mapping.keys()):
            print(f"  {letter} = {mapping[letter]}")
        print("-" * 35)
        print(f"\nArithmetic Verification:")
        print(f"    {send}")
        print(f"  + {more}")
        print(f"  ------")
        print(f"   {money}")
        print(f"\nVerification Check: {send} + {more} = {send + more} (Matches MONEY = {money})")
        print("Crypt-Arithmetic Problem solved successfully!")
    else:
        print("No solution exists for this equation.")

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
============================================================
 EXPERIMENT 9: CRYPT-ARITHMETIC PROBLEM (SEND + MORE = MONEY) 
============================================================
Problem Equation:
    SEND
  + MORE
  ------
   MONEY

Solving using Constraint Satisfaction Search...

Solution Found:
-----------------------------------
  D = 7
  E = 5
  M = 1
  N = 6
  O = 0
  R = 8
  S = 9
  Y = 2
-----------------------------------

Arithmetic Verification:
    9567
  + 1085
  ------
   10652

Verification Check: 9567 + 1085 = 10652 (Matches MONEY = 10652)
Crypt-Arithmetic Problem solved successfully!
```

### RESULT
The Crypt-Arithmetic problem SEND + MORE = MONEY was successfully solved in Python IDLE. The unique assignment (9567 + 1085 = 10652) satisfies all arithmetic and CSP constraints.

---

## EXPERIMENT 10: TRAVELLING SALESMAN PROBLEM (TSP)

- **Date:** 15.10.2026
- **Course Outcome:** CO4
- **Submission Target:** Assigned for 15.10.2026

### AIM
To write and execute a Python program to solve the Travelling Salesman Problem using State Space Search / Branch and Bound.

### PROCEDURE
- Understand the TSP problem: Given a set of cities and pairwise distances, find the shortest closed tour visiting each city exactly once and returning to the origin.
- Represent city inter-distances using a 4x4 symmetric distance matrix.
- Fix the starting city (City 'A') to avoid circular permutation duplicates.
- Evaluate all possible permutations of visiting intermediate cities.
- Compute total round-trip costs and determine the minimum cost Hamiltonian cycle.
- Execute the program in Python IDLE and display all evaluated tours.

### ALGORITHM
```text
Step 1: Start the program.
Step 2: Define list of cities ['A', 'B', 'C', 'D'] and distance matrix.
Step 3: Set start_city = 'A'.
Step 4: Generate all permutations of remaining cities ['B', 'C', 'D'].
Step 5: For each permutation:
       a. Construct tour = [start] + list(perm) + [start].
       b. Calculate tour cost = sum of adjacent edge weights in distance matrix.
       c. If tour cost < min_cost, update min_cost and best_tour.
Step 6: Print table of all candidate tours and highlight the optimal tour.
Step 7: Stop the program.
```

### SOURCE CODE
```python
"""
EXPERIMENT 10 (SYLLABUS EXP 9): TRAVELLING SALESMAN PROBLEM (TSP)
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO4
Description: Solving the Travelling Salesman Problem using State Space Search / Branch and Bound.
"""

from itertools import permutations

def solve_tsp(cities, distance_matrix, start_city):
    """
    Solves the TSP by evaluating permutations of intermediate cities
    to find the tour with minimum total cost returning to start_city.
    """
    n = len(cities)
    other_cities = [c for c in cities if c != start_city]
    
    min_cost = float('inf')
    best_tour = None
    all_evaluated_tours = []

    for perm in permutations(other_cities):
        current_tour = [start_city] + list(perm) + [start_city]
        current_cost = 0
        valid_tour = True

        for i in range(len(current_tour) - 1):
            u = current_tour[i]
            v = current_tour[i + 1]
            cost = distance_matrix[u][v]
            if cost == float('inf'):
                valid_tour = False
                break
            current_cost += cost

        if valid_tour:
            all_evaluated_tours.append((current_tour, current_cost))
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour

    return best_tour, min_cost, all_evaluated_tours

if __name__ == '__main__':
    cities = ['A', 'B', 'C', 'D']
    
    # Distance Matrix between 4 cities
    #        A    B    C    D
    dist_matrix = {
        'A': {'A': 0,  'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0,  'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0,  'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0 }
    }

    print("=" * 65)
    print(" EXPERIMENT 10: TRAVELLING SALESMAN PROBLEM (TSP) ")
    print("=" * 65)
    print("Distance Matrix between Cities:")
    print(f"{'':>6} | " + " | ".join([f"{c:>4}" for c in cities]))
    print("-" * 35)
    for row in cities:
        print(f"{row:>6} | " + " | ".join([f"{dist_matrix[row][col]:>4}" for col in cities]))
    print("-" * 35)

    start = 'A'
    print(f"\nStarting and ending city: {start}\n")
    print("Evaluating all possible distinct Hamilton tours:")
    print(f"{'No':<4} | {'Tour Path':<25} | {'Total Cost'}")
    print("-" * 45)

    best_tour, min_cost, tours = solve_tsp(cities, dist_matrix, start)

    for idx, (tour, cost) in enumerate(tours, start=1):
        tour_str = ' -> '.join(tour)
        is_best = " (Optimal)" if cost == min_cost else ""
        print(f"{idx:<4} | {tour_str:<25} | {cost}{is_best}")

    print("-" * 45)
    print(f"\nOptimal Tour: {' -> '.join(best_tour)}")
    print(f"Minimum Tour Distance: {min_cost}")
    print("Travelling Salesman Problem solved successfully!")

```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
=================================================================
 EXPERIMENT 10: TRAVELLING SALESMAN PROBLEM (TSP) 
=================================================================
Distance Matrix between Cities:
       |    A |    B |    C |    D
-----------------------------------
     A |    0 |   10 |   15 |   20
     B |   10 |    0 |   35 |   25
     C |   15 |   35 |    0 |   30
     D |   20 |   25 |   30 |    0
-----------------------------------

Starting and ending city: A

Evaluating all possible distinct Hamilton tours:
No   | Tour Path                 | Total Cost
---------------------------------------------
1    | A -> B -> C -> D -> A     | 95
2    | A -> B -> D -> C -> A     | 80 (Optimal)
3    | A -> C -> B -> D -> A     | 95
4    | A -> C -> D -> B -> A     | 80 (Optimal)
5    | A -> D -> B -> C -> A     | 95
6    | A -> D -> C -> B -> A     | 95
---------------------------------------------

Optimal Tour: A -> B -> D -> C -> A
Minimum Tour Distance: 80
Travelling Salesman Problem solved successfully!
```

### RESULT
The Travelling Salesman Problem was successfully implemented and solved in Python IDLE. The optimal tour A -> B -> D -> C -> A was identified with a minimum distance of 80.

---
