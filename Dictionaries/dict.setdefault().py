my_dict = {}

# Using setdefault to add a key with a default value
value = my_dict.setdefault('key1', 'default_value')
print("Returned Value:", value)  
# Output: default_value
print("Dictionary:", my_dict)  
# Output: {'key1': 'default_value'}

# Using setdefault when the key already exists
my_dict['key2'] = 'existing_value'
value = my_dict.setdefault('key2', 'new_default')
print("Returned Value:", value)  
# Output: existing_value
print("Dictionary:", my_dict)   
# Output: {'key1': 'default_value', 'key2': 'existing_value'}
# Output: {'key1': 'default_value', 'key2': 'existing_value'}
