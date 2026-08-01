import sqlite3

def monthly_sales_report():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Get month from the user
    month = input("Enter month (MM): ").strip()

    # Retrieve monthly sales
    cursor.execute("""
    SELECT
        products.product_name,
        sales.quantity_sold,
        sales.total_amount,
        sales.sale_date
    FROM sales
    JOIN products
    ON sales.product_id = products.id
    WHERE strftime('%m', sales.sale_date) = ?
    ORDER BY sales.sale_date
    """, (month,))

    sales = cursor.fetchall()

    # Display monthly sales report
    if not sales:
        print("\nNo sales found for this month.")
    else:
        print("\nMonthly Sales Report" )
        print("=" * 80)
        print(
            f"{'Product':<20}"
            f"{'Quantity Sold':<18}"
            f"{'Total Amount':<18}"
            f"{'Sale Date':<15}"
        )
        print("=" * 80)

        total_revenue = 0

        for sale in sales:
            print(
                f"{sale[0]:<20}"
                f"{sale[1]:<18}"
                f"{sale[2]:<18.2f}"
                f"{sale[3]:<15}"
            )

            total_revenue += sale[2]
        print("=" * 80)
        print(f"Total Revenue: Rs. {total_revenue:.2f}")

    connection.close()

if __name__ == "__main__":
    monthly_sales_report()