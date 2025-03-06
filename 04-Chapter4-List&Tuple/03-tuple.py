# Demonstrating most used tuple functions in Python

def tuple_functions_demo():
    t = (10, 20, 30, 40, 20, 50)
    print("Original tuple:", t)
    
    # MOST USED FUNCTIONS
    # 1. len(): Returns the length of the tuple
    print("Length of tuple:", len(t))
    
    # 2. count(): Counts occurrences of a value
    print("Count of 20:", t.count(20))
    
    # 3. index(): Finds the first index of a value
    print("Index of 30:", t.index(30))
    
    # 4. tuple(): Converts a list to a tuple
    lst = [1, 2, 3]
    print("List to tuple:", tuple(lst))
    
    # 5. slicing: Extracts a portion of a tuple
    print("Sliced tuple (1:4):", t[1:4])
    
    # 6. concatenation: Combines two tuples
    t2 = (60, 70)
    print("Concatenated tuple:", t + t2)

    t3 = (67,68,69)
    t4 = (88,89,90)
    concatenated_tuple = t3 + t4
    print (concatenated_tuple)
    
    # 7. unpacking: Assigns tuple values to variables
    a, b, c, d, e, f = t
    print("Unpacked values:", a, b, c, d, e, f)
    
    # RARELY USED FUNCTIONS
    # 8. sum(): Returns the sum of elements
    print("Sum of elements:", sum(t))
    
    # 9. sorted(): Returns a sorted list from a tuple
    print("Sorted tuple as list:", sorted(t))
    
    # 10. repetition: Repeats a tuple
    print("Repeated tuple:", t * 2)
    
    # LEAST USED FUNCTIONS
    # 11. min(): Returns the smallest element
    print("Minimum value:", min(t))
    
    # 12. max(): Returns the largest element
    print("Maximum value:", max(t))
    
    # 13. tuple comprehension alternative: Using generator expression with tuple
    squared_tuple = tuple(x**2 for x in t)
    print("Squared elements as tuple:", squared_tuple)

tuple_functions_demo()
