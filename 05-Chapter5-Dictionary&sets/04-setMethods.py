# Python program to demonstrate set methods with explanations and their outputs

def demonstrate_set_methods():
    # Creating sets with some common and some unique elements
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print("Set1:", set1)  # Output: Set1: {1, 2, 3, 4, 5}
    print("Set2:", set2)  # Output: Set2: {4, 5, 6, 7, 8}

    # Union - Combines elements of both sets, removing duplicates
    union_set = set1.union(set2)
    print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

    # Intersection - Returns only the common elements between both sets
    intersection_set = set1.intersection(set2)
    print("Intersection:", intersection_set)  # Output: {4, 5}

    # Difference - Returns elements that are in set1 but not in set2
    difference_set = set1.difference(set2)
    print("Difference (set1 - set2):", difference_set)  # Output: {1, 2, 3}

    # Symmetric Difference - Returns elements that are in either set, but not both
    symmetric_difference_set = set1.symmetric_difference(set2)
    print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

    # Subset - Checks if a set is a subset of another (i.e., all elements of one set exist in another)
    subset_check = {1, 2}.issubset(set1)
    print("{1, 2} is subset of set1:", subset_check)  # Output: True

    # Superset - Checks if a set is a superset of another (i.e., contains all elements of another set)
    superset_check = set1.issuperset({1, 2})
    print("Set1 is superset of {1, 2}:", superset_check)  # Output: True

    # Disjoint Sets - Checks if two sets have no elements in common
    disjoint_check = set1.isdisjoint({9, 10})
    print("Set1 is disjoint with {9, 10}:", disjoint_check)  # Output: True

    # Adding an element - Inserts an element into the set
    set1.add(10)
    print("After adding 10 to set1:", set1)  # Output: {1, 2, 3, 4, 5, 10}

    # Removing an element - Removes the specified element; raises an error if not found
    set1.remove(10)
    print("After removing 10 from set1:", set1)  # Output: {1, 2, 3, 4, 5}

    # Discarding an element - Removes the specified element if it exists; does nothing otherwise
    set1.discard(15)
    print("After discarding 15 (not in set1):", set1)  # Output: {1, 2, 3, 4, 5}

    # Popping an element - Removes and returns an arbitrary element from the set
    popped_element = set1.pop()
    print("Popped element:", popped_element, "Remaining set1:", set1)  # Output varies, as set elements have no order

    # Clearing the set - Removes all elements from the set
    set1.clear()
    print("After clearing set1:", set1)  # Output: set()

if __name__ == "__main__":
    demonstrate_set_methods()
