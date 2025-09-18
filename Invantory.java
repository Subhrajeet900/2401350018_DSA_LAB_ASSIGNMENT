
import java.util.*;

// InventoryItem
class InventoryItem {

    int id;
    String name;
    int quantity;
    double price;

    InventoryItem(int id, String name, int quantity, double price) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }
}

// Inventory System Class
class InventorySystem {

    ArrayList<InventoryItem> items = new ArrayList<>();

    // Add item
    void addItem(int id, String name, int quantity, double price) {
        items.add(new InventoryItem(id, name, quantity, price));
        System.out.println("Item added successfully!");
    }

    // Remove item
    void removeItem(int id) {
        boolean removed = false;
        for (int i = 0; i < items.size(); i++) {
            if (items.get(i).id == id) {
                items.remove(i);
                removed = true;
                break;
            }
        }
        if (removed) {
            System.out.println("Item removed successfully!"); 
        }else {
            System.out.println("Item not found!");
        }
    }

    // Search item
    void searchItem(String key) {
        boolean found = false;
        for (InventoryItem item : items) {
            if (String.valueOf(item.id).equals(key) || item.name.equalsIgnoreCase(key)) {
                System.out.println("Found -> ID: " + item.id + ", Name: " + item.name
                        + ", Quantity: " + item.quantity + ", Price: " + item.price);
                found = true;
            }
        }
        if (!found) {
            System.out.println("Item not found!");
        }
    }

    // Display all items
    void displayItems() {
        if (items.isEmpty()) {
            System.out.println("No items in inventory!");
            return;
        }
        System.out.printf("\n%-5s %-15s %-10s %-10s\n", "ID", "Name", "Quantity", "Price");
        System.out.println("----------------------------------------");
        for (InventoryItem item : items) {
            System.out.printf("%-5d %-15s %-10d %-10.2f\n", item.id, item.name, item.quantity, item.price);
        }
    }
}

// Main class
public class Invantory {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        InventorySystem system = new InventorySystem();

        while (true) {
            System.out.println("\n--- Inventory System Menu ---");
            System.out.println("1. Add Item");
            System.out.println("2. Remove Item");
            System.out.println("3. Search Item");
            System.out.println("4. Display All Items");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Enter Name: ");
                    String name = sc.nextLine();
                    System.out.print("Enter Quantity: ");
                    int qty = sc.nextInt();
                    System.out.print("Enter Price: ");
                    double price = sc.nextDouble();
                    system.addItem(id, name, qty, price);
                }
                case 2 -> {
                    System.out.print("Enter ID to remove: ");
                    int id = sc.nextInt();
                    system.removeItem(id);
                }
                case 3 -> {
                    System.out.print("Enter ID or Name to search: ");
                    String key = sc.next();
                    system.searchItem(key);
                }
                case 4 ->
                    system.displayItems();
                case 0 -> {
                    System.out.println("Exiting...");
                    sc.close();
                    return;
                }
                default ->
                    System.out.println("Invalid choice! Try again.");
            }
        }
    }
}
