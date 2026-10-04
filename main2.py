# # Balanced Parentheses using Recursion

# Easy explanation

# For n = 2, we need 2 pairs:

# (())
# ()()

# So:

# count_paren(2) = 2

# For n = 3:

# ((()))
# (()())
# (())()
# ()(())
# ()()()

# So:

# count_paren(3) = 5
# Remember these 2 conditions

# 1. Add (

# if left < n:

# We can add an opening bracket if we haven't used all of them.

# 2. Add )

# if right < left:

# We can close a bracket only when we already have an opening bracket.

# The recursion keeps trying both possibilities and counts all valid combinations.

def count_paren(n, left=0, right=0):
# All brackets are used
    if left == n and right == n:
        return 1

    total = 0

    # Add an opening bracket (
    if left < n:
        total += count_paren(n, left + 1, right)

    # Add a closing bracket )
    if right < left:
        total += count_paren(n, left, right + 1)

    return total

n = int(input("Enter number of pairs: "))

print("Number of valid ways:", count_paren(n))