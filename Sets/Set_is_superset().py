def set_is_superset(superset, subset):
 return superset.issuperset(subset)

# Example usage
if __name__ == "__main__":
    set_a = {1, 2, 3, 4, 5}
    set_b = {2, 3}
    set_c = {6, 7}

    print(f"Is set_a a superset of set_b? {set_is_superset(set_a, set_b)}")  # output: "True"
    print(f"Is set_a a superset of set_c? {set_is_superset(set_a, set_c)}")  # output: "False"