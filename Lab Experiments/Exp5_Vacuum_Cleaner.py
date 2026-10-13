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
