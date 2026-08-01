import sqlite3

def search_product():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Get product name from the user
    product_name = input("Enter product name: ").strip()

    cursor.execute("""
    SELECT * FROM products
    WHERE LOWER (product_name) = LOWER(?)
    """, (product_name,))

    product = cursor.fetchone()

    # Display the search result
    if not product:
        print("\nProduct not found.")
    else:
        print("\nProduct found.")
        print("=" * 50)
        print(f"ID: {product[0]}")
        print(f"Product Name: {product[1]}")
        print(f"Category: {product[2]}")
        print(f"Price: {product[3]:.2f}")
        print(f"Quantity: {product[4]}")
        print(f"Minimum Stock: {product[5]}")
        print("=" * 50)

    connection.close()

if __name__ == "__main__":
    search_product()
