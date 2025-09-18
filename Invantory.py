# 2401350018 subhrajeet dash

class InventoryItem:
    def __init__(self, item_id, item_name, quantity, price):
        self.ItemID = item_id
        self.ItemName = item_name
        self.Quantity = quantity
        self.Price = price

    def insertItem(self, array, data):
        array.append(data)

    def deleteItem(self, array, item_id):
        for i, item in enumerate(array):
            if item.ItemID == item_id:
                del array[i]
                return True
        return False

    def searchItem(self, array, key):
        for item in array:
            if item.ItemID == key or item.ItemName == key:
                return item
        return None


class InventorySystem:
    def __init__(self):
        self.ItemArray = []
        self.SparseMatrix = {}
        self.PriceQuantityTable = []

    def addItemRecord(self, item):
        self.ItemArray.append(item)

    def removeItemRecord(self, item_id):
        for i, item in enumerate(self.ItemArray):
            if item.ItemID == item_id:
                del self.ItemArray[i]
                return True
        return False

    def searchByItem(self, key):
        for item in self.ItemArray:
            if item.ItemID == key or item.ItemName == key:
                return item
        return None

    def managePriceQuantity(self):
        self.PriceQuantityTable = [
            [item.ItemID, item.Quantity, item.Price] for item in self.ItemArray
        ]
        row_major = []
        for row in self.PriceQuantityTable:
            for col in row:
                row_major.append(col)
        col_major = []
        for c in range(len(self.PriceQuantityTable[0])):
            for r in range(len(self.PriceQuantityTable)):
                col_major.append(self.PriceQuantityTable[r][c])
        return row_major, col_major

    def optimizeSparseStorage(self, threshold=2):
        self.SparseMatrix = {}
        for item in self.ItemArray:
            if item.Quantity <= threshold:
                self.SparseMatrix[item.ItemID] = (item.ItemName, item.Quantity, item.Price)
        return self.SparseMatrix


def complexity_analysis():
    complexities = {
        "insertItem": {"Time": "O(1) amortized", "Space": "O(1)"},
        "deleteItem": {"Time": "O(n)", "Space": "O(1)"},
        "searchItem": {"Time": "O(n)", "Space": "O(1)"},
        "addItemRecord": {"Time": "O(1)", "Space": "O(1)"},
        "removeItemRecord": {"Time": "O(n)", "Space": "O(1)"},
        "searchByItem": {"Time": "O(n)", "Space": "O(1)"},
        "managePriceQuantity": {"Time": "O(n*m)", "Space": "O(n*m)"},
        "optimizeSparseStorage": {"Time": "O(n)", "Space": "O(k)"},
    }
    return complexities


if __name__ == "__main__":
    system = InventorySystem()

    item1 = InventoryItem(1, "Apples", 10, 2.5)
    item2 = InventoryItem(2, "Bananas", 1, 1.2)
    item3 = InventoryItem(3, "Oranges", 5, 3.0)

    system.addItemRecord(item1)
    system.addItemRecord(item2)
    system.addItemRecord(item3)

    found = system.searchByItem(2)
    if found:
        print("Found Item:", found.ItemID, found.ItemName, found.Quantity, found.Price)

    system.removeItemRecord(3)

    row, col = system.managePriceQuantity()
    print("Row-Major Ordering:", row)
    print("Column-Major Ordering:", col)

    sparse = system.optimizeSparseStorage()
    print("Sparse Storage:", sparse)

    print("\nComplexity Analysis:")
    for func, details in complexity_analysis().items():
        print(f"{func}: Time={details['Time']}, Space={details['Space']}")
