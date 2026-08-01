import sqlite3

def low_stock_alert():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Retrieve products with low stock
    cursor.execute("""
    SELECT * FROM products
    WHERE quantity <= minimum_stock
    ORDER BY quantity
    """)

    products = cursor.fetchall()

    # Display low stock products
    if not products:
        print("\nAll products have sufficient stock.")
    else:
        print("\nLow Stock Alert!")
        print("=" * 90)
        print(
            f"{'ID':<5}"
            f"{'Product':<20}"
            f"{'Category':<20}"
            f"{'Price':<10}"
            f"{'Quantity':<12}"
            f"{'Minimum Stock':<15}"
        )
        print("=" * 90)

        for product in products:
            print(
                f"{product[0]:<5}"
                f"{product[1]:<20}"
                f"{product[2]:<20}"
                f"{product[3]:<10.2f}"
                f"{product[4]:<12}"
                f"{product[5]:<15}"
            )
            print("=" * 90)

    connection.close()

if __name__ == "__main__":
    low_stock_alert()