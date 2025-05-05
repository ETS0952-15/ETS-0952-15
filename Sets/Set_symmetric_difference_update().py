# Define two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.symmetric_difference_update(set_b)
print("Updated set_a after symmetric difference update:", set_a)
# output: {1, 2, 5, 6}
