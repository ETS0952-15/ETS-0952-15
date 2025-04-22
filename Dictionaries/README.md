# Dict. get() method
This method is dictionary method that returns the value of the specified key.
If the key does not exist, it returns None or the specified default value.
# Dict. items() method
This method is dictionary method that returns a view object that displays a list of a dictionary's key-value tuple pairs.
The view object changes when the dictionary changes.
# Dict. keys() method
This method is dictionary method that returns a view object that displays a list of all the keys in the dictionary.
# Dict. values() method
This method is dictionary method that returns a view object that displays a list of all the values in the dictionary.
The view object is dynamic and reflects any changes made to the dictionary.
# Dict. update() method
This method is dictionary method that updates the dictionary with the elements from another dictionary or from an iterable of key/value pairs.
If the key already exists, the value is updated; if not, a new key/value pair is added.
This method does not return any value; it modifies the original dictionary in place.
This is useful for merging dictionaries or adding new entries without creating a new dictionary.
# Dict. pop() method
This method is dictionary method that removes the specified key and returns the corresponding value.
If the key is not found, it raises a KeyError unless a default value is provided.
This method is useful for removing items from a dictionary while also retrieving their values.
The popitem() method removes and returns the last inserted key-value pair as a tuple.
# Dict. copy() method
This method is dictionary method that creates a shallow copy of the dictionary, meaning it copies the dictionary itself but not the objects it contains.
If the dictionary contains mutable objects (like lists), changes to those objects in the copied dictionary will also affect the original dictionary.
# Dict. clear() method
This method is dictionary method that removes all items from the dictionary, leaving it empty.
After calling clear(), the dictionary will have no key-value pairs, and its length will be 0. 
# Dict. popitem() method
The popitem() method is useful when you want to remove and retrieve the last inserted item from a dictionary.
It can be helpful in various scenarios, such as implementing a stack or managing a cache.
# Dict. fromkeys(iterable,value=none) method
This method is dictionary method that creates a new dictionary with keys from an iterable and a specified value.
# Dict. setdefault(key, default=None) method
This method is dictionary method that returns the value of the key if it exists; otherwise, inserts the key with the specified default value.