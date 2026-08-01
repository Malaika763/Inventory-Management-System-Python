import sqlite3


def restock_report():
    # Connect to the database
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Retrieve products that need restocking
    cursor.execute("""
    SELECT *
    FROM products
    WHERE quantity <= minimum_stock
    ORDER BY quantity
    """)

    products = cursor.fetchall()

    if not products:
        print("\nNo products need restocking.")

    else:
        TARGET_STOCK = 20

        print("\nRestock Report")
        print("=" * 120)
        print(
            f"{'ID':<5}"
            f"{'Product':<20}"
            f"{'Category':<20}"
            f"{'Price':<10}"
            f"{'Current Quantity':<20}"
            f"{'Minimum Stock':<18}"
            f"{'Order Quantity':<18}"
        )
        print("=" * 120)

        for product in products:

            order_quantity = TARGET_STOCK - product[4]

            if order_quantity < 0:
                order_quantity = 0

            print(
                f"{product[0]:<5}"
                f"{product[1]:<20}"
                f"{product[2]:<20}"
                f"{product[3]:<10.2f}"
                f"{product[4]:<20}"
                f"{product[5]:<18}"
                f"{order_quantity:<18}"
            )

        print("=" * 120)

    connection.close()


if __name__ == "__main__":
    restock_report()