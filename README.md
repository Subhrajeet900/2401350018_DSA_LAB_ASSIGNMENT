# Grocery Store Inventory System 
Introduction

This is my Python project for the Inventory System of a Grocery Store.
The program can keep records of items like their ID, name, quantity, and price.
It uses arrays to store the data and supports basic operations like adding, deleting, and searching items.

The project also shows how price and quantity can be stored in row-major and column-major order.
For rarely restocked products, it uses a sparse representation to save space.

# Features

Add a new item to the inventory

Delete an item using its ID

Search item by ID or name

Manage price and quantity in row-major / column-major form

Sparse representation for low stock items

Shows time and space complexity of all functions

# Files

Invantory.py → main Python file with the complete code

README.md → this file

How to Run

Install Python on your system.

Save the code in a file called Invantory.py.

Open terminal / command prompt and run:

python Invantory.py

# Sample Output
Found Item: 2 Bananas 1 1.2
Row-Major Ordering: [1, 10, 2.5, 2, 1, 1.2]
Column-Major Ordering: [1, 2, 10, 1, 2.5, 1.2]
Sparse Storage: {2: ('Bananas', 1, 1.2)}

Complexity Analysis:
insertItem: Time=O(1) amortized, Space=O(1)
deleteItem: Time=O(n), Space=O(1)
searchItem: Time=O(n), Space=O(1)
addItemRecord: Time=O(1), Space=O(1)
removeItemRecord: Time=O(n), Space=O(1)
searchByItem: Time=O(n), Space=O(1)
managePriceQuantity: Time=O(n*m), Space=O(n*m)
optimizeSparseStorage: Time=O(n), Space=O(k)

# Complexity Table
Function	Time	Space
insertItem	O(1)	O(1)
deleteItem	O(n)	O(1)
searchItem	O(n)	O(1)
addItemRecord	O(1)	O(1)
removeItemRecord	O(n)	O(1)
searchByItem	O(n)	O(1)
managePriceQuantity	O(n*m)	O(n*m)
optimizeSparseStorage	O(n)	O(k)

# Conclusion

This assignment helped me understand how arrays can be used for real-life inventory management.
I also learned about row-major and column-major ordering, sparse representation, and how to calculate time and space complexity for each operation.


