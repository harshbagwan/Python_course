from collections import deque

# -------------------------- LIST --------------------------
print("\n📌 LIST")
my_list = [10, 20, 30, 40]  # Initializing a list
print("List:", my_list)
print("Accessing element at index 1:", my_list[1])  # Output: 20
my_list[2] = 100  # Modifying list element
print("Modified List:", my_list)

# -------------------------- TUPLE --------------------------
print("\n📌 TUPLE")
my_tuple = (10, 20, 30, 40)  # Initializing a tuple
print("Tuple:", my_tuple)
print("Accessing element at index 2:", my_tuple[2])  # Output: 30
# my_tuple[2] = 100  # ❌ This would raise an error because tuples are immutable

# -------------------------- DICTIONARY --------------------------
print("\n📌 DICTIONARY")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # Initializing dictionary
print("Dictionary:", my_dict)
print("Accessing 'name':", my_dict["name"])
my_dict["age"] = 26  # Modifying dictionary value
print("Updated Dictionary:", my_dict)

# -------------------------- SET --------------------------
print("\n📌 SET")
my_set = {10, 20, 30, 40}  # Initializing a set
print("Set:", my_set)
my_set.add(50)  # Adding an element
print("After adding 50:", my_set)
my_set.remove(20)  # Removing an element
print("After removing 20:", my_set)
# print(my_set[1])  # ❌ This would raise an error because sets do not support indexing

# -------------------------- STRING --------------------------
print("\n📌 STRING")
my_string = "Hello"
print("String:", my_string)
print("Accessing character at index 1:", my_string[1])  # Output: 'e'
# my_string[1] = "a"  # ❌ Strings are immutable
modified_string = my_string[:1] + "a" + my_string[2:]  # Creating a modified string
print("Modified String:", modified_string)

# -------------------------- QUEUE (deque) --------------------------
print("\n📌 QUEUE (deque)")
my_queue = deque([10, 20, 30])  # Initializing queue
print("Queue:", my_queue)
my_queue.append(40)  # Enqueue (Add to rear)
print("After enqueue:", my_queue)
print("Dequeued element:", my_queue.popleft())  # Dequeue (Remove from front)
print("Queue after dequeue:", my_queue)

# -------------------------- STACK (deque) --------------------------
print("\n📌 STACK (deque)")
my_stack = deque([10, 20, 30])  # Initializing stack
print("Stack:", my_stack)
my_stack.append(40)  # Push (Add to top)
print("After push:", my_stack)
print("Popped element:", my_stack.pop())  # Pop (Remove from top)
print("Stack after pop:", my_stack)


# -------------------- SUMMARY TABLE --------------------
"""
| Data Structure | Initialization            | Accessing Elements  | Modifiable? |
|---------------|---------------------------|---------------------|-------------|
| List (`list`) | `my_list = [1, 2, 3]`      | `my_list[i]`        | ✅ Yes |
| Tuple (`tuple`) | `my_tuple = (1, 2, 3)`   | `my_tuple[i]`       | ❌ No |
| Dictionary (`dict`) | `{"a": 1, "b": 2}`   | `my_dict["a"]`      | ✅ Yes |
| Set (`set`) | `{1, 2, 3}`                 | ❌ No indexing       | ✅ Yes |
| String (`str`) | `"abc"`                  | `my_string[i]`      | ❌ No |
| Queue (`deque`) | `deque([1, 2, 3])`      | `.popleft()`        | ✅ Yes |
| Stack (`deque`) | `deque([1, 2, 3])`      | `.pop()`            | ✅ Yes |
"""

# -------------------- KEY TAKEAWAYS --------------------
"""
1️⃣ **Lists, dictionaries, and sets are mutable** (modifiable).
2️⃣ **Tuples and strings are immutable** (cannot be changed directly).
3️⃣ **Dictionaries use keys for access**, unlike lists that use indices.
4️⃣ **Sets do not allow duplicate elements and do not support indexing**.
5️⃣ **`deque` is better for queues and stacks because of fast operations**.
"""
