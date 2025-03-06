# Demonstrating most used dictionary functions in Python

def dictionary_functions_demo():
    # Creating a sample dictionary
    student = {
        "name": "Alice",
        "age": 22,
        "course": "Computer Science",
        "marks": 85
    }
    
    print("Original Dictionary:", student)

    # MOST USED FUNCTIONS
    # 1. keys(): Returns all dictionary keys
    print("Keys:", student.keys())

    # 2. values(): Returns all dictionary values
    print("Values:", student.values())

    # 3. items(): Returns key-value pairs as tuples
    print("Key-Value Pairs:", student.items())

    # 4. get(): Safely retrieves a value for a given key
    print("Get 'age':", student.get("age"))

    # 5. update(): Updates dictionary with another dictionary
    student.update({"marks": 90, "city": "New York"})
    print("Updated Dictionary:", student)

    # 6. pop(): Removes and returns a value by key
    removed_value = student.pop("marks")
    print("Removed 'marks':", removed_value)
    print("Dictionary after pop:", student)

    # 7. popitem(): Removes and returns the last inserted key-value pair
    removed_pair = student.popitem()
    print("Removed last item:", removed_pair)
    print("Dictionary after popitem:", student)

    # RARELY USED FUNCTIONS
    # 8. setdefault(): Returns value if key exists, else sets and returns default
    age = student.setdefault("age", 25)
    print("Set default 'age':", age)

    # 9. fromkeys(): Creates a dictionary with default values
    keys = ["id", "department", "salary"]
    default_dict = dict.fromkeys(keys, "N/A")
    print("Dictionary from keys:", default_dict)

    # LEAST USED FUNCTIONS
    # 10. copy(): Creates a shallow copy of the dictionary
    student_copy = student.copy()
    print("Copied Dictionary:", student_copy)

    # 11. clear(): Removes all items from the dictionary
    student.clear()
    print("Cleared Dictionary:", student)

dictionary_functions_demo()
