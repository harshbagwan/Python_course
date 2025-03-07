// C++ program demonstrating 'goto' statement

#include <iostream>
using namespace std;

// Definition: 'goto' jumps to a labeled statement in the program.
// It changes the normal execution flow and is generally discouraged.

int main() {
    int i = 0;

start:  // Label
    cout << i << " ";
    i++;

    if (i < 5)
        goto start;  // Jumps back to 'start' label, creating a loop-like effect

    return 0;
}

/* Key Takeaways:
- 'goto' moves execution to a labeled statement.
- It should be avoided as it makes debugging harder (spaghetti code).
- Unlike 'pass' in Python, 'goto' affects program flow.
- Use loops instead of 'goto' for better readability.
*/
