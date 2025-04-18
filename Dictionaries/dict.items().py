Sample_dict = {
    "Name": "Minte",
    "Age": 20,
    "City": "Addis Ababa"
}
# Using the items() method to get key-value pairs
for Student, value in Sample_dict.items():
    print(f"Student:{Student}: {value}")
    # Output: "Student:Name: Minte"
    #         "Student:Age: 20"   
    #         "Student:City: Addis Ababa"