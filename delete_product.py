import sqlite3

def delete_product():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    while True:
        try:
            # Get product ID
            product_id = int(input("Enter a product ID to delete: "))

            if product_id <= 0:
                print("Product ID must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid product ID.")

    # Check if the product exists
    cursor.execute("""
    SELECT product_name
    FROM products
    WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    if not product:
        print("\nProduct not found.")
    else:
        print(f"\nProduct: {product[0]}")

        #Confirm deletion
        choice = input("Are you sure you want to delete this product? (yes/No): ").lower()

        if choice == "yes":

            # Delete the product
            cursor.execute("""
            DELETE FROM products
            WHERE id = ?
            """, (product_id,))

            connection.commit()

            print("\nProduct deleted successfully!")

        else:
            print("\nDeletion cancelled.")

    connection.close()

if __name__ == "__main__":
    delete_product()

