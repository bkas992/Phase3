import time
import random
import sys
from collections import defaultdict

#Product class
class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity  # Add or subtract depending on the value

    def update_price(self, price):
        self.price = price  # New price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

#Inventory Management Class
class Inventory:
    def __init__(self):
        self.inventory = {}  # Dictionary to hold Product objects
    
    def add_product(self, product):
        """Add a new product or update if it exists."""
        if product.product_id in self.inventory:
            print(f"Product with ID {product.product_id} already exists. Updating it.")
            self.update_product(product.product_id, product.price, product.quantity)
        else:
            self.inventory[product.product_id] = product
            print(f"Added new product: {product}")
    
    def update_product(self, product_id, new_price=None, new_quantity=None):
        """Update the product price or quantity."""
        if product_id in self.inventory:
            product = self.inventory[product_id]
            if new_price is not None:
                product.update_price(new_price)
            if new_quantity is not None:
                product.update_quantity(new_quantity)
            print(f"Updated product: {product}")
        else:
            print(f"Product with ID {product_id} not found.")
    
    def delete_product(self, product_id):
        """Delete a product by ID."""
        if product_id in self.inventory:
            deleted_product = self.inventory.pop(product_id)
            print(f"Deleted product: {deleted_product}")
        else:
            print(f"Product with ID {product_id} not found.")
    
    def get_product(self, product_id):
        """Get the details of a product by ID."""
        return self.inventory.get(product_id, None)
    
    def generate_report(self):
        """Generate a summary report of total inventory value."""
        total_value = 0
        total_items = 0
        for product in self.inventory.values():
            total_value += product.price * product.quantity
            total_items += product.quantity
        return {
            "total_inventory_value": total_value,
            "total_products": len(self.inventory),
            "total_items": total_items
        }

    def display_inventory(self):
        """Display all products in the inventory."""
        for product in self.inventory.values():
            print(product)

# Create an Inventory instance
inventory = Inventory()

# Add products
product1 = Product(1, "Laptop", "Electronics", 1000, 5)
product2 = Product(2, "Shirt", "Clothing", 25, 10)
product3 = Product(3, "Smartphone", "Electronics", 700, 3)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Update product quantity or price
inventory.update_product(1, new_price=950, new_quantity=7)

# Delete a product
inventory.delete_product(2)

# Query a product
product = inventory.get_product(3)
if product:
    print("Queried Product:", product)

# Generate and display the report
report = inventory.generate_report()
print("\nInventory Report:")
print(f"Total Inventory Value: ${report['total_inventory_value']:.2f}")
print(f"Total Products: {report['total_products']}")
print(f"Total Items: {report['total_items']}")

# Display all products in the inventory
print("\nFull Inventory:")
inventory.display_inventory()

# Create Inventory instance
inventory = Inventory()

# Simulate adding a large number of products
def generate_large_inventory(num_products=10000):
    products = []
    for i in range(num_products):
        product = Product(
            product_id=i,
            name=f"Product_{i}",
            category="Category_" + str(random.randint(1, 5)),
            price=round(random.uniform(10, 500), 2),
            quantity=random.randint(1, 100)
        )
        products.append(product)
    return products

# Batch insert 10,000 products
large_inventory = generate_large_inventory(10000)
start_time = time.time()
inventory.batch_add_products(large_inventory)
end_time = time.time()

print(f"Time to add 10,000 products: {end_time - start_time:.4f} seconds")

# Test: Query non-existent product
non_existent_product = inventory.get_product(99999)
if not non_existent_product:
    print("Product not found for ID 99999")

# Test: Update product
inventory.update_product(5000, new_price=299.99, new_quantity=50)

# Test: Delete a product
inventory.delete_product(5001)

# Generate and display inventory report
report = inventory.generate_report()
print("\nInventory Report:")
print(f"Total Inventory Value: ${report['total_inventory_value']:.2f}")
print(f"Total Products: {report['total_products']}")
print(f"Total Items: {report['total_items']}")

# Display first 5 products in the inventory
print("\nSample Inventory (First 5 Products):")
for idx, product in enumerate(inventory.inventory.values()):
    if idx < 5:
        print(product)

# Memory usage before adding large dataset
print(f"Memory usage before: {sys.getsizeof(inventory.inventory)} bytes")

# Add large dataset
inventory.batch_add_products(large_inventory)

# Memory usage after adding large dataset
print(f"Memory usage after: {sys.getsizeof(inventory.inventory)} bytes")
