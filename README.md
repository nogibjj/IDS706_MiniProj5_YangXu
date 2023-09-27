# IDS706_MiniProj5_YangXu

This repository is a continuation of the IDS706 course assignments, focusing on Mini Project 5. Building upon the foundational [ids706-python-template](https://github.com/xuy50/ids706-python-template), it introduces database operations and CRUD functionalities.
This script processes data, interfacing with a PostgreSQL database to perform Create, Read, Update, and Delete operations.

## Overview

Utilizing the `psycopg2` library, this project demonstrates essential techniques for database operations in Python, specifically using the PostgreSQL relational database system.

## Key Modifications from Previous Projects

- Introduced database operation functions like `create_table()`, `insert_item()`, `update_item_price()`, `delete_item()`, `delete_all_items()`, `get_items_by_product()`, and `insert_data_from_csv()`.
- Extended `test_main.py` to verify the correct working of the newly added functionalities.
- Added `psycopg2-binary 2.9.1` and `python-dotenv 0.19.2` to `requirements.txt` to enhance database operations and environment variable management.


### Requirements

Ensure the presence of:
- Python (Version 3.6 or newer)
- psycopg2-binary (Version 2.9.1)
- python-dotenv (Version 0.19.2)
- pandas

## Functionality

- **`create_table()`**: Sets up the `items` table in the database. If already present, the table isn't recreated.
- **`insert_item(date, product, price, quantity)`**: Adds a new item to the `items` table.
- **`insert_data_from_csv()`**: Inputs multiple items into the `items` table from a CSV file named `dataset_sample.csv`.
- **`get_all_items()`**: Retrieves all items from the `items` table.
- **`update_item_price(product, new_price)`**: Updates the price of an item based on the product name.
- **`delete_item(product)`**: Removes an item using the product name.
- **`delete_all_items()`**: Deletes all entries from the `items` table.
- **`get_items_by_product(product)`**: Acquires all records of a specific product.

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

[![CI/CD workflow](https://github.com/nogibjj/IDS706_MiniProj5_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj5_YangXu/actions/workflows/cicd.yml)
