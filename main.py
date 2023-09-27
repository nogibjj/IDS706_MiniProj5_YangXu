import psycopg2
import os
from config import get_db_config
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    config = get_db_config()
    connection = psycopg2.connect(**config)
    return connection

def create_table():
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS items(
                id SERIAL PRIMARY KEY,
                date DATE,
                product VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2),
                quantity INTEGER
            );
            """)

def update_item_price(product, new_price):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE items SET price = %s WHERE product = %s",
                           (new_price, product))
            conn.commit()

def delete_item(product):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM items WHERE product = %s", (product,))
            conn.commit()

def get_items_by_product(product):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items WHERE product = %s", (product,))
            return cursor.fetchall()

def insert_item(date, product, price, quantity):
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO items (date, product, price, quantity) VALUES (%s, %s, %s, %s)",
                           (date, product, price, quantity))
            conn.commit()

def get_all_items():
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items;")
            return cursor.fetchall()

if __name__ == "__main__":
    create_table()
    # Create - Insert data
    insert_item('2023-09-04', 'TestItem', 1.5, 30)
    # Read - Fetch data
    items = get_all_items()
    print(items)
    # Update - Change the price of TestItem to 2.0
    update_item_price('TestItem', 2.0)
    # Check the item after the update
    test_items = get_items_by_product('TestItem')
    print(test_items)
    # Delete - Remove TestItem
    delete_item('TestItem')
