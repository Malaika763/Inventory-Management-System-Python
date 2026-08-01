import sqlite3
from datetime import date

def record_sale():
    # Connection to the database
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Get and validate product ID
    while True:
        try:
            product_id = int(input("Enter a product ID: "))
            break
        except ValueError:
            print("Please enter a valid product ID.")

    # Retrieve product details
    cursor.execute("""
    SELECT product_name, price, quantity
    FROM products
    WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    if not product:
        print("Product not found.")
    else:
        product_name, price, quantity = product

        print(f"\nProduct: {product_name}")
        print(f"Price: Rs.{price:.2f}")
        print(f"Available Stock: {quantity}")

        # Get quantity sold
        while True:
            try:
                quantity_sold = int(input("Enter quantity sold: "))
                if quantity_sold <= 0:
                    print("Quantity must be greater than 0.")
                elif quantity_sold > quantity:
                    print("Not enough stock available.")
                else:
                    break
            except ValueError:
                print("Please enter a valid quantity.")

        # Calculate total sale amount and remaining stock
        total_amount = price * quantity_sold
        remaining_quantity = quantity - quantity_sold

        # Update product quantity
        cursor.execute("""
        UPDATE products
        SET quantity = ?
        WHERE id = ?
        """, (remaining_quantity, product_id))

        # Save the sale
        cursor.execute("""
        INSERT INTO sales 
            (product_id, quantity_sold, total_amount, sale_date)
        VALUES (?, ?, ?, ?)
        """, (product_id, quantity_sold, total_amount, str(date.today())))

        connection.commit()

        print("\nSale recorded successfully!")
        print(f"Total Amount: Rs.{total_amount:.2f}")
        print(f"Remaining Stock: {remaining_quantity}")

    connection.close()

if __name__ == "__main__":
    record_sale()
