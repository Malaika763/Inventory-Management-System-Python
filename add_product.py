import sqlite3

def add_product():

    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Get and validate product name
    while True:
        product_name = input("Enter product name: ").strip()
        if product_name == "":
            print("Product name cannot be empty.")
            continue

        cursor.execute("SELECT * FROM products WHERE product_name = ?",
                       (product_name,))

        if cursor.fetchone():
            print("A product with this name already exists.")
        else:
            break

    # Get and validate category
    while True:
        category = input("Enter category: ").strip()
        if category == "":
            print("Category cannot be empty.")
        else:
            break

    # Get and validate price
    while True:
        try:
            price = float(input("Enter price: "))
            if price <= 0:
                print("Price must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid price.")

    # Get and validate quantity
    while True:
        try:
            quantity = int(input("Enter quantity:"))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid quantity.")

    # Get and validate minimum stock
    while True:
        try:
            minimum_stock = int(input("Enter minimum stock level: "))
            if minimum_stock < 0:
                print("Minimum stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Insert product into the database
    cursor.execute("""
    INSERT INTO products (
        product_name, category, price, quantity, minimum_stock)
        VALUES (?, ?, ?, ?, ?)
    """, (
        product_name, category, price, quantity, minimum_stock))

    connection.commit()
    connection.close()

    print("\nProduct added successfully!")

if __name__ == "__main__":
    add_product()