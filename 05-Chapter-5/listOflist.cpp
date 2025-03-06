#include <iostream>
#include <vector>
using namespace std;

int main() {
    // C++: Vector of Vectors Example
    
    // Creating a vector of vectors (2D Matrix)
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Accessing elements
    cout << "Element at row 1, col 2: " << matrix[1][2] << endl; // Output: 6

    // Modifying an element
    matrix[2][2] = 10;

    // Adding a new row
    matrix.push_back({10, 11, 12});

    // Iterating over the vector of vectors
    cout << "Matrix elements:" << endl;
    for (const auto& row : matrix) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }

    // Flattening the matrix
    vector<int> flat_list;
    for (const auto& row : matrix) {
        for (int num : row) {
            flat_list.push_back(num);
        }
    }

    // Printing the flattened list
    cout << "Flattened List: ";
    for (int num : flat_list) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
