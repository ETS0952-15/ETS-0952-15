# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Create a shallow copy of the dictionary
copied_dict = original_dict.copy()

# Modify the copied dictionary
copied_dict['d'] = 4

# Print both dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)