import mysql.connector
import pandas as pd
import datetime

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "B@1Guy202",
    database = "retail_db"
)

cursor = conn.cursor()

# CREATES DATABASE ------------------------------
# cursor.execute("CREATE DATABASE retail_db")
# CREATES DATABASE ------------------------------

# CREATES TABLES ------------------------------
# cursor.execute("""
#     CREATE TABLE products(
#         ProductID VARCHAR(100) PRIMARY KEY,
#         ProductName VARCHAR(100),
#         CategoryID VARCHAR(100),
#         FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID)
#     )
# """)

# cursor.execute("""
#     CREATE TABLE categories(
#         CategoryID VARCHAR(100) PRIMARY KEY,
#         CategoryName VARCHAR(100)
#     )
# """)

# cursor.execute("""
#     CREATE TABLE customers(
#         CustomerID VARCHAR(100) PRIMARY KEY,
#         Gender VARCHAR(100),
#         Age INT,
#         City VARCHAR(100),
#         CustomerSegment VARCHAR(100),
#         SignUpDate DATE
#     )
# """)

# cursor.execute("""
#     CREATE TABLE order_details(
#         OrderID VARCHAR(100),
#         ProductID VARCHAR(100),
#         Quantity INT,
#         UnitCost DECIMAL (10, 2),
#         UnitPrice DECIMAL (10, 2),
#         DiscountRate DECIMAL (10, 2),
#         isReturned INT,
#         ReturnDate DATE,
#         ReturnTime TIME,
#         ReturnReason VARCHAR(100),
#         FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
#         FOREIGN KEY (ProductID) REFERENCES products(ProductID),
#         PRIMARY KEY (OrderID, ProductID)
#     )
# """)

# cursor.execute("""
#     CREATE TABLE orders(
#         OrderID VARCHAR(100) PRIMARY KEY,
#         CustomerID VARCHAR(100),
#         OrderDate DATE,
#         OrderTime TIME,
#         FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
#     )
# """)
# CREATES TABLES ------------------------------

# FILLS TABLES ------------------------------
# PRODUCTS
# df = pd.read_csv("products.csv")
# data = list(df.itertuples(index=False, name=None))

# cursor.executemany("""
#     INSERT INTO products (ProductID, ProductName, CategoryID)
#     VALUES (%s, %s, %s)
# """, data)

# CATEGORIES
# df = pd.read_csv("categories.csv")
# data = list(df.itertuples(index=False, name=None))

# cursor.executemany("""
#     INSERT INTO categories (CategoryID, CategoryName)
#     VALUES (%s, %s)
# """, data)

# CUSTOMERS
# cursor.execute("""
#     ALTER TABLE customers ADD COLUMN Region VARCHAR(100)
# """)
# df = pd.read_csv("customers.csv")
# df["SignUpDate"] = pd.to_datetime(df["SignUpDate"]).dt.date
# data = list(df.itertuples(index=False, name=None))

# cursor.executemany("""
#     INSERT INTO customers (CustomerID, Gender, Age, City, Region, CustomerSegment, SignUpDate)
#     VALUES (%s, %s, %s, %s, %s, %s, %s)
# """, data)

# ORDERS
# cursor.execute("DROP TABLE order_details")
# cursor.execute("DROP TABLE orders")
# cursor.execute("ALTER TABLE orders MODIFY COLUMN OrderTime TIME")

# cursor.execute("SELECT * FROM order_details LIMIT 10")
# rows = cursor.fetchall()
# print(rows)

# df = pd.read_csv("orders.csv")
# # df["OrderDate"] = pd.to_datetime(df["OrderDate"]).dt.date
# # df["OrderTime"] = df["OrderTime"].apply(
# #     lambda t: datetime.datetime.strptime(t, "%H:%M:%S").time()
# # )
# df["OrderDate"] = df["OrderDate"].apply(lambda d: d.strftime("%Y-%m-%d"))
# df["OrderTime"] = df["OrderTime"].apply(lambda t: t.strftime("%H:%M:%S"))
# data = list(df.itertuples(index=False, name=None))

# df = pd.read_csv("orders.csv")

# # Ensure date is in correct format
# df["OrderDate"] = pd.to_datetime(df["OrderDate"]).dt.strftime("%Y-%m-%d")

# # Ensure time is in correct format
# df["OrderTime"] = pd.to_datetime(df["OrderTime"], format="%H:%M:%S").dt.strftime("%H:%M:%S")

# data = list(df.itertuples(index=False, name=None))

# cursor.executemany("""
#     INSERT INTO orders (OrderID, CustomerID, OrderDate, OrderTime)
#     VALUES (%s, %s, %s, %s)
# """, data)

# ORDER DETAILS
# df = pd.read_csv("order_details.csv")

# # Convert to object so None is allowed
# df["ReturnReason"] = df["ReturnReason"].astype(object)

# # Replace <NA> → None
# df["ReturnReason"] = df["ReturnReason"].where(
#     pd.notna(df["ReturnReason"]),
#     None
# )

# # Ensure date is in correct format
# df["ReturnDate"] = pd.to_datetime(df["ReturnDate"]).dt.strftime("%Y-%m-%d")

# # Ensure time is in correct format
# df["ReturnTime"] = pd.to_datetime(df["ReturnTime"], format="%H:%M:%S").dt.strftime("%H:%M:%S")

# data = list(df.itertuples(index=False, name=None))

# cursor.executemany("""
#     INSERT INTO order_details (OrderID, ProductID, Quantity, UnitCost, UnitPrice, DiscountRate, IsReturned, ReturnDate, ReturnTime, ReturnReason)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """, data)
# FILLS TABLES ------------------------------


# Lists the databases and tables within the retail_db database. It also lists the columns in each table with their variable type
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)

# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table)

# cursor.execute("""
#     SELECT table_name
#     FROM information_schema.tables
#     WHERE table_schema = 'retail_db';
# """)

# tables = [row[0] for row in cursor.fetchall()]
# print("Tables:", tables)

# for table in tables:
#     cursor.execute(f"""
#         SELECT column_name, data_type
#         FROM information_schema.columns
#         WHERE table_schema = 'retail_db'
#         AND table_name = '{table}';
#     """)
#     print(f"\nColumns in {table}:")
#     for col in cursor.fetchall():
#         print(col)

# OUTPUT
# Tables: ['categories', 'customers', 'order_details', 'orders', 'products']

# Columns in categories:
# ('CategoryID', 'varchar')
# ('CategoryName', 'varchar')

# Columns in customers:
# ('CustomerID', 'varchar')
# ('Gender', 'varchar')
# ('Age', 'int')
# ('City', 'varchar')
# ('CustomerSegment', 'varchar')
# ('SignUpDate', 'date')
# ('Region', 'varchar')

# Columns in order_details:
# ('OrderID', 'varchar')
# ('ProductID', 'varchar')
# ('Quantity', 'int')
# ('UnitCost', 'decimal')
# ('UnitPrice', 'decimal')
# ('DiscountRate', 'decimal')
# ('isReturned', 'int')
# ('ReturnDate', 'date')
# ('ReturnTime', 'time')
# ('ReturnReason', 'varchar')

# Columns in orders:
# ('OrderID', 'varchar')
# ('CustomerID', 'varchar')
# ('OrderDate', 'date')
# ('OrderTime', 'time')

# Columns in products:
# ('ProductID', 'varchar')
# ('ProductName', 'varchar')
# ('CategoryID', 'varchar')

conn.commit()
cursor.close()
conn.close()