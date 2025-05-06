# Define two sets
set_a = {1, 2, 3, 4}
set_b = {5, 6, 7, 8}
set_c = {3, 6, 9}

print("Are set_a and set_b disjoint?", set_a.isdisjoint(set_b))  # output: "True"
print("Are set_a and set_c disjoint?", set_a.isdisjoint(set_c))  # output: "False"