import sqlite3


def setup_database():
    # Connect to the SQLite database (creates 'ecommerce.db' if it doesn't exist)
    conn = sqlite3.connect('ecommerce.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Drop tables if they already exist for a clean setup
    cursor.execute("DROP TABLE IF EXISTS sales")
    cursor.execute("DROP TABLE IF EXISTS products")

    # SQL query to create the products table
    cursor.execute("""
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        category TEXT,
        price REAL
    )
    """)

    # SQL query to create the sales table
    cursor.execute("""
    CREATE TABLE sales (
        sale_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER,
        sale_date TEXT,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    # Mock Data: 5 Products
    products_data = [
        (1, 'Wireless Mouse', 'Electronics', 25.99),
        (2, 'Mechanical Keyboard', 'Electronics', 89.50),
        (3, 'Desk Mat', 'Accessories', 15.00),
        (4, 'USB-C Hub', 'Electronics', 45.00),
        (5, 'Coffee Mug', 'Kitchen', 12.99)
    ]

    # Insert product data using executemany
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products_data)

    # Mock Data: 20 Sales Records (Targeting the week of July 16 - July 23, 2026)
    sales_data = [
        (101, 1, 2, '2026-07-16'),
        (102, 2, 1, '2026-07-17'),
        (103, 5, 3, '2026-07-17'),
        (104, 3, 1, '2026-07-18'),
        (105, 4, 2, '2026-07-18'),
        (106, 1, 1, '2026-07-19'),
        (107, 2, 2, '2026-07-19'),
        (108, 5, 1, '2026-07-19'),
        (109, 3, 4, '2026-07-20'),
        (110, 4, 1, '2026-07-20'),
        (111, 1, 3, '2026-07-20'),
        (112, 2, 1, '2026-07-21'),
        (113, 5, 2, '2026-07-21'),
        (114, 3, 1, '2026-07-21'),
        (115, 1, 5, '2026-07-22'),
        (116, 4, 2, '2026-07-22'),
        (117, 2, 1, '2026-07-22'),
        (118, 5, 4, '2026-07-23'),
        (119, 3, 2, '2026-07-23'),
        (120, 4, 1, '2026-07-23')
    ]

    # Insert sales data
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", sales_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Success! 'ecommerce.db' created with 5 products and 20 sales records.")


if __name__ == "__main__":
    setup_database()