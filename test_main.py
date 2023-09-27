import unittest
from unittest.mock import MagicMock, patch
from main import (
    create_table,
    insert_item,
    get_all_items,
    update_item_price,
    delete_item,
    delete_all_items,
    get_items_by_product,
    insert_data_from_csv,
)


class TestMain(unittest.TestCase):
    @patch("main.create_connection")
    def test_crud_operations(self, mock_create_connection):
        # Mocking the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        mock_create_connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Create table
        create_table()

        # Insert data (Create)
        insert_item("2023-09-04", "TestItem", 1.5, 30)
        mock_cursor.fetchall.return_value = [(1, "2023-09-04", "TestItem", 1.5, 30)]
        items = get_all_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], "2023-09-04")
        self.assertEqual(items[0][2], "TestItem")
        self.assertEqual(items[0][3], 1.5)
        self.assertEqual(items[0][4], 30)

        # Insert data from CSV
        insert_data_from_csv()
        # Mock a return value which includes TestItem + 3 rows from CSV
        mock_cursor.fetchall.return_value.extend(
            [
                (2, "2023-09-01", "Apple", 1.2, 50),
                (3, "2023-09-01", "Banana", 0.5, 40),
                (4, "2023-09-01", "Cherry", 2.5, 20),
            ]
        )
        items = get_all_items()
        self.assertEqual(len(items), 4)

        # Update the price for TestItem (Update)
        update_item_price("TestItem", 2.0)
        mock_cursor.fetchall.return_value[0] = (1, "2023-09-04", "TestItem", 2.0, 30)
        updated_items = get_all_items()
        self.assertEqual(updated_items[0][3], 2.0)

        # Check specific product
        mock_cursor.fetchall.return_value = [(1, "2023-09-04", "TestItem", 2.0, 30)]
        test_items = get_items_by_product("TestItem")
        self.assertEqual(len(test_items), 1)
        self.assertEqual(test_items[0][3], 2.0)

        # Remove TestItem (Delete)
        delete_item("TestItem")
        mock_cursor.fetchall.return_value.pop(0)
        items_after_deletion = get_all_items()
        self.assertEqual(len(items_after_deletion), 3)

        # Delete all items
        delete_all_items()
        mock_cursor.fetchall.return_value = []
        self.assertFalse(get_all_items())


if __name__ == "__main__":
    unittest.main()
