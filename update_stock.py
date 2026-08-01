import sqlite3

def update_stock():

    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Get and validate product ID
    while True:
        try:
            product_id = int(input("Enter a product ID: "))
            break
        except ValueError:
            print("Please enter a valid product ID.")

    # Check if the product exists
    cursor.execute("""
    SELECT product_name, quantity 
    FROM products
    WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    # Check if the current product exists and display its current details
    if not product:
        print("Product not found.")
    else:
        product_name, current_quantity = product
        print(f"\nProduct: {product_name}")
        print(f"Current Quantity: {current_quantity}")

        # Get quantity to add
        while True:
            try:
                added_quantity = int(input("Enter quantity to add: "))
                if added_quantity <= 0:
                    print("Quantity must be greater then 0.")
                else:
                    break
            except ValueError:
                print("Please enter a valid quantity.")

        new_quantity = current_quantity + added_quantity

        # Update the quantity
        cursor.execute("""
        UPDATE products
        SET quantity = ?
        WHERE id = ?
        """, (new_quantity, product_id))

        connection.commit()

        print("\nStock updated successfully!")
        print(f"Updated Quantity: {new_quantity}")

        connection.close()

if __name__ == "__main__":
    update_stock()