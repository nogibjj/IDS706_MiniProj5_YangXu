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

- **`create_connection()`**: Establishes a connection with the PostgreSQL database.

- **`create_table()`**: Initializes the database table.

- **`insert_item(date, product, price, quantity)`**: Inserts a new record into the database.

... [Other Functions]

## Sample Output

... [Insert a description or a sample output of your script, if applicable]

- **Database Record**:

    ```bash
    date: YYYY-MM-DD, product: 'Example', price: 100.00, quantity: 5
    ```

... [Add other outputs, visualizations, or images if necessary]

[![CI/CD workflow](https://github.com/nogibjj/IDS706_MiniProj5_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj5_YangXu/actions/workflows/cicd.yml)
