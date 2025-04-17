my_list = [10, 20, 30, 40, 50]
last_element = my_list.pop()
print("Popped element:", last_element) # Output: "Popped element: 50"
print("List after popping:", my_list) # output: "List after popping: [10, 20, 30, 40]"
index = 3
element_at_index = my_list.pop(index)
print(f"Popped element at index {index}:", element_at_index)
# Output: "Popped element at index 3: 40"
print("List after popping:", my_list)
# Output: "List after popping: [10, 20, 30]"