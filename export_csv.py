import sqlite3
import csv


def export_csv():
    # Connect to the database
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Retrieve all products
    cursor.execute("""
    SELECT *
    FROM products
    ORDER BY id
    """)

    products = cursor.fetchall()

    if not products:
        print("\nNo products found.")

    else:
        # Create CSV file
        with open("inventory_report.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Write column headings
            writer.writerow([
                "ID",
                "Product Name",
                "Category",
                "Price",
                "Quantity",
                "Minimum Stock"
            ])

            # Write product records
            writer.writerows(products)

        print("\nInventory exported successfully!")
        print("File Name: inventory_report.csv")

    connection.close()


if __name__ == "__main__":
    export_csv()