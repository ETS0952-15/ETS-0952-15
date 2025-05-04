# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# Perform symmetric difference using the ^ operator
symmetric_diff = set_a ^ set_b
print("Symmetric Difference", symmetric_diff) # output: {1, 2, 3, 6, 7, 8}