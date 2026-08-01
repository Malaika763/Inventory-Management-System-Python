import sqlite3

def view_products():

    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Retrieve all products
    cursor.execute("""
    SELECT * FROM 
        products
    ORDER BY id
    """)

    products = cursor.fetchall()

    if not products:
        print("\nNo products found.")
    else:
        print("\n" + "=" * 78)
        print(
            f"{'ID' :<5}"
            f"{'Product' :<20}"
            f"{'Category' :<20}"
            f"{'Price' :<10}"
            f"{'Quantity' :<12}"
            f"{'Minimum Stock' :<15}"
        )
        print("=" * 100)

        for product in products:
            print(
                f"{product[0]:<5}"
                f"{product[1]:<20}"
                f"{product[2]:<20}"
                f"{product[3]:<10.2f}"
                f"{product[4]:<12}"
                f"{product[5]:<15}"
            )

        print("=" * 70)

    connection.close()

if __name__ == "__main__":
    view_products()