from database import create_database
from add_product import add_product
from view_products import view_products
from update_stock import update_stock
from record_sale import record_sale
from search_product import search_product
from low_stock_alert import low_stock_alert
from restock_report import restock_report
from monthly_sales_report import monthly_sales_report
from delete_product import delete_product
from export_csv import export_csv


def main():
    # Create database and tables if they do not exist
    create_database()

    while True:
        print("\n" + "=" * 55)
        print("         INVENTORY MANAGEMENT SYSTEM")
        print("=" * 55)
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Stock")
        print("4. Record Sale")
        print("5. Search Product")
        print("6. Low Stock Alert")
        print("7. Restock Report")
        print("8. Monthly Sales Report")
        print("9. Delete Product")
        print("10. Export Inventory to CSV")
        print("11. Exit")
        print("=" * 55)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            record_sale()

        elif choice == "5":
            search_product()

        elif choice == "6":
            low_stock_alert()

        elif choice == "7":
            restock_report()

        elif choice == "8":
            monthly_sales_report()

        elif choice == "9":
            delete_product()

        elif choice == "10":
            export_csv()

        elif choice == "11":
            print("\nThank you for using Inventory Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
