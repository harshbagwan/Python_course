# Python: List of Lists Example

# Creating a list of lists (2D Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print("Element at row 1, col 2:", matrix[1][2])  # Output: 6

# Modifying an element
matrix[2][2] = 10

# Adding a new row
matrix.append([10, 11, 12])

# Iterating over the list of lists
print("Matrix elements:")
for row in matrix:
    print(row)

# Flattening the matrix using list comprehension
flat_list = [num for row in matrix for num in row]
print("Flattened List:", flat_list)
