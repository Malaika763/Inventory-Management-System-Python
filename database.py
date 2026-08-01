import sqlite3

def create_database():

    # Connection to the SQLite database (create it if it does not exist)
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    # Create the products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS
    products (
        id INTEGER PRIMARY KEY
    AUTOINCREMENT, 
        product_name TEXT NOT NULL UNIQUE,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL, 
        minimum_stock INTEGER NOT NULL)
    """)

    # Create the sales table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS
    sales (
        sale_id INTEGER PRIMARY KEY
    AUTOINCREMENT, 
        product_id INTEGER NOT NULL,
        quantity_sold INTEGER NOT NULL,
        total_amount REAL NOT NULL,
        sale_date TEXT NOT NULL,
        FOREIGN KEY (product_id)
    REFeRENCES products(id))
    """)

    # Save changes and close the connection
    connection.commit()
    connection.close()

    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()