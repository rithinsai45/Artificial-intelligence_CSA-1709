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
