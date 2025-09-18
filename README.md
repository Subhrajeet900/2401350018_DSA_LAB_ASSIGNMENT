# Name - subhrajeet dash , Roll - 2401350018

# Grocery Store Inventory System 
Introduction
This is my **Java project** for the Inventory System of a Grocery Store.  
The program keeps records of items including their **ID, name, quantity, and price**.  
It uses an **ArrayList** to store the data and supports basic operations like **adding, deleting, searching, and displaying items**.

# Features

- Add a new item to the inventory  
- Delete an item using its ID  
- Search item by **ID or name**  
- Display all items in a **tabular format**  
- Simple, beginner-friendly **menu-driven interface**  
- Shows **time and space complexity** of each operation

# Sample output
--- Inventory System Menu ---
1. Add Item
2. Remove Item
3. Search Item
4. Display All Items
0. Exit
Enter your choice: 1
Enter ID: 2
Enter Name: Bananas
Enter Quantity: 5
Enter Price: 1.2
Item added successfully!

Enter your choice: 4

ID    Name            Quantity   Price     
----------------------------------------
2     Bananas         5          1.20      

Enter your choice: 3
Enter ID or Name to search: 2
Found -> ID: 2, Name: Bananas, Quantity: 5, Price: 1.2

# Complexity Analysis
Function	Time Complexity	Space Complexity
Add Item	O(1)	O(1)
Remove Item	O(n)	O(1)
Search Item	O(n)	O(1)
Display All Items	O(n)	O(1)


