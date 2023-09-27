# IDS706_MiniProj5_YangXu

This repository is a continuation of the IDS706 course assignments, focusing on Mini Project 5. Building upon the foundational [ids706-python-template](https://github.com/xuy50/ids706-python-template), it introduces database operations and CRUD functionalities.
This script processes data, interfacing with a PostgreSQL database to perform Create, Read, Update, and Delete operations.

## Overview

Utilizing the `psycopg2` library, this project demonstrates essential techniques for database operations in Python, specifically using the PostgreSQL relational database system.

## Key Modifications from Previous Projects

- Added database operation functions such as `create_table()`, `insert_item()`, `update_item()`, and more.
- Modified `test_main.py` to ensure the correct working of new functionalities introduced.
- Integrated `psycopg2-binary 2.9.1` and `python-dotenv 0.19.2` within `requirements.txt` to facilitate database operations and environment variable management.

### Requirements

Ensure the presence of:
- Python (Version 3.6 or newer)
- psycopg2-binary (Version 2.9.1)
- python-dotenv (Version 0.19.2)

## Functionality

- **`create_table()`**: Initializes the `items` table in the database. If the table already exists, it won't be recreated.
- **`insert_item(date, product, price, quantity)`**: Inserts a new item into the `items` table. The arguments represent the date, product name, price, and quantity respectively.
- **`get_all_items()`**: Fetches all items from the `items` table and returns them as a list of tuples.
- **`update_item_price(product, new_price)`**: Finds an item in the `items` table by its product name and updates its price.
- **`delete_item(product)`**: Deletes an item from the `items` table based on the product name.
- **`get_items_by_product(product)`**: Fetches all records of a specific product from the `items` table.

## Sample Output

- **Database Record**:

    ```bash
    (92, datetime.date(2023, 9, 4), 'TestItem', Decimal('1.50'), 30)
    (93, datetime.date(2023, 9, 1), 'Apple', Decimal('1.20'), 50)
    (94, datetime.date(2023, 9, 1), 'Banana', Decimal('0.50'), 40)
    (95, datetime.date(2023, 9, 1), 'Cherry', Decimal('2.50'), 20)
    (96, datetime.date(2023, 9, 2), 'Apple', Decimal('1.30'), 45)
    (97, datetime.date(2023, 9, 2), 'Banana', Decimal('0.60'), 50)
    (98, datetime.date(2023, 9, 2), 'Cherry', Decimal('2.40'), 22)
    (99, datetime.date(2023, 9, 3), 'Apple', Decimal('1.10'), 55)
    (100, datetime.date(2023, 9, 3), 'Banana', Decimal('0.70'), 42)
    (101, datetime.date(2023, 9, 3), 'Cherry', Decimal('2.60'), 19)

    [(92, datetime.date(2023, 9, 4), 'TestItem', Decimal('2.00'), 30)]

    check TestItem deleted:  []

    All items deleted.
    ```

... [Add other outputs, visualizations, or images if necessary]

[![CI/CD workflow](https://github.com/nogibjj/IDS706_MiniProj5_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj5_YangXu/actions/workflows/cicd.yml)
