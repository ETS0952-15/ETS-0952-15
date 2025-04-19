# Define a dictionary
section_A_result = {'Abebe': 30, 'Bamlak': 25, 'Amare': 43}
# Dictionary to update with
section_B_result = {'Minte': 50, 'Martha': 48}
# Updating the original dictionary
section_A_result.update(section_B_result)
print("Updated Dictionary:", section_A_result)
# Output: Updated Dictionary: {'Abebe': 30, 'Bamlak': 25, 'Amare': 43, 'Minte': 50, 'Martha': 48} 