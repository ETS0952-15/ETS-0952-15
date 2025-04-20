# Creating a dictionary
sample_dict = {
    'name': 'Minte',
    'age': 20,
    'city': 'Addis Ababa',
    'country': 'Ethiopia',
    'occupation': 'Student',
    'hobby': 'Playing Piano',
    'favorite_color': 'Brown'
}

# Removing and returning the last inserted key-value pair
key, value = sample_dict.popitem()

print(f"Removed item: ({key}, {value})")
print(f"Updated dictionary: {sample_dict}")
# Output:
# Removed item: (favorite_color, Brown) 
# Updated dictionary: {'name': 'Minte', 'age': 20, 'city': 'Addis Ababa', 'country': 'Ethiopia', 'occupation': 'Student', 'hobby': 'Playing Piano'}