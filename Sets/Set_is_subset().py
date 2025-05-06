def set_is_subset(set_a, set_b):
 return set_a.issubset(set_b)

# Example usage
if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}

    if set_is_subset(set1, set2):
        print(f"{set1} is a subset of {set2}")
    else:
        print(f"{set1} is not a subset of {set2}")
    # output: "{1, 2, 3} is a subset of {1, 2, 3, 4, 5}"