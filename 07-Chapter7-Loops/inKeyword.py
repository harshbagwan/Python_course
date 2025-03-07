# -------------------------- 'in' Keyword in Python --------------------------

# The 'in' keyword is used to check if a value exists in a sequence (like lists, tuples, dictionaries, sets, and strings).

# -------------------------- LIST --------------------------
print("\n📌 LIST")
my_list = [10, 20, 30, 40]
print("List:", my_list)
print("Is 20 in list?", 20 in my_list)  # Output: True
print("Is 50 in list?", 50 in my_list)  # Output: False

# -------------------------- TUPLE --------------------------
print("\n📌 TUPLE")
my_tuple = (10, 20, 30, 40)
print("Tuple:", my_tuple)
print("Is 30 in tuple?", 30 in my_tuple)  # Output: True
print("Is 100 in tuple?", 100 in my_tuple)  # Output: False

# -------------------------- STRING --------------------------
print("\n📌 STRING")
my_string = "hello world"
print("String:", my_string)
print("Is 'h' in string?", 'h' in my_string)  # Output: True
print("Is 'z' in string?", 'z' in my_string)  # Output: False
print("Is 'hello' in string?", "hello" in my_string)  # Output: True (Substrings work)

# -------------------------- SET --------------------------
print("\n📌 SET")
my_set = {10, 20, 30, 40}
print("Set:", my_set)
print("Is 10 in set?", 10 in my_set)  # Output: True
print("Is 50 in set?", 50 in my_set)  # Output: False

# -------------------------- DICTIONARY --------------------------
print("\n📌 DICTIONARY (Checks for Keys Only)")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)
print("Is 'name' a key in dictionary?", "name" in my_dict)  # Output: True
print("Is 'Alice' in dictionary?", "Alice" in my_dict)  # Output: False (Values are not checked)
print("Is 'age' a key in dictionary?", "age" in my_dict)  # Output: True

# -------------------- SUMMARY TABLE --------------------
"""
| Data Structure | 'in' Usage Example      | Works On?       | Notes |
|---------------|-------------------------|----------------|----------------------------------|
| List (`list`) | `x in my_list`          | ✅ Yes         | Checks if element is present |
| Tuple (`tuple`) | `x in my_tuple`       | ✅ Yes         | Works like lists |
| String (`str`) | `"sub" in my_string`   | ✅ Yes         | Works for substrings |
| Set (`set`) | `x in my_set`            | ✅ Yes         | Fast lookup (O(1) time complexity) |
| Dictionary (`dict`) | `key in my_dict` | ✅ Yes (keys)  | Checks only for keys, not values |
"""

# -------------------- KEY TAKEAWAYS --------------------
"""
1️⃣ **`in` is used to check membership in sequences (list, tuple, string, set, dictionary).**
2️⃣ **For dictionaries, `in` checks for keys only, not values.**
3️⃣ **Using `in` with sets is faster than with lists or tuples (O(1) vs. O(n)).**
4️⃣ **Substrings can be checked in strings using `in`.**
5️⃣ **If an element is not found, `in` returns `False` without an error.**
"""

