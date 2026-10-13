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
