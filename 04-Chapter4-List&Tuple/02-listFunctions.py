# Demonstrating most used, rare, and least used list functions in Python

def list_functions_demo():
    lst = [10, 20, 30, 40, 50]
    print("Original list:", lst)
    
    ######## MOST USED FUNCTIONS
  
    # 1. append(): Adds an element to the end of the list
    lst.append(60)
    print("Append 60:", lst)
    
    # 2. extend(): Extends list by appending elements from another list
    lst.extend([70, 80])
    print("Extend with [70, 80]:", lst)
    
    # 3. insert(): Inserts an element at a given position
    lst.insert(2, 25)
    print("Insert 25 at index 2:", lst)
    
    # 4. remove(): Removes the first occurrence of a value
    lst.remove(30)
    print("Remove 30:", lst)
    
    # 5. pop(): Removes and returns the last element (or element at given index)
    last_element = lst.pop()
    print("Pop last element:", last_element, "Updated List:", lst)
    
    # 6. index(): Returns the index of the first occurrence of a value
    print("Index of 40:", lst.index(40))
    
    # 7. count(): Counts occurrences of a value in the list
    print("Count of 20:", lst.count(20))
    
    # 8. sort(): Sorts the list in ascending order
    lst.sort()
    print("Sorted List:", lst)
    
    # 9. reverse(): Reverses the list order
    lst.reverse()
    print("Reversed List:", lst)
    
    # 10. copy(): Returns a shallow copy of the list
    copied_list = lst.copy()
    print("Copied List:", copied_list)
    
    ########### RARELY USED FUNCTIONS
  
    # 11. clear(): Removes all elements from the list
    temp_list = lst.copy()
    temp_list.clear()
    print("Cleared List:", temp_list)
    
    # 12. sort(reverse=True): Sorts the list in descending order
    lst.sort(reverse=True)
    print("Sorted in Descending Order:", lst)
    
    ########## LEAST USED FUNCTIONS
  
    # 13. del: Deletes an element by index or the entire list
    del lst[2]  # Deleting element at index 2
    print("List after deleting index 2:", lst)
    
list_functions_demo()
