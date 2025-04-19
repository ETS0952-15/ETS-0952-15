# Define a dictionary
data = {"name": "Minte",
        "age": 20,
        "city": "Addis Ababa"}
# Remove an item using pop() and get its value
removed_value = data.pop("age")
print("Removed value:", removed_value)  # Output: Removed value: 25
print("Updated dictionary:", data)  # Output: {'name': 'Alice', 'city': 'New York'}