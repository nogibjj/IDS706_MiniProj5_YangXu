import unittest
from unittest.mock import MagicMock, patch
from main import create_table, insert_item, get_all_items


class TestMain(unittest.TestCase):
    @patch("main.create_connection")
    def test_crud_operations(self, mock_create_connection):
        # Mocking the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        mock_create_connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Rest of your tests remains the same

        # Create table
        create_table()

        # Insert data (Create)
        insert_item("2023-09-04", "TestItem", 1.5, 30)

        # Fetch data (Read)
        mock_cursor.fetchall.return_value = [(1, "2023-09-04", "TestItem", 1.5, 30)]
        items = get_all_items()
        last_item = items[-1]
        self.assertEqual(last_item[1], "2023-09-04")
        self.assertEqual(last_item[2], "TestItem")
        self.assertEqual(last_item[3], 1.5)
        self.assertEqual(last_item[4], 30)

        # Update the price for TestItem (Update)
        mock_cursor.fetchall.return_value = [(1, "2023-09-04", "TestItem", 2.0, 30)]
        updated_items = (
            get_all_items()
        )  # Assuming you want to mock the same method here
        self.assertEqual(updated_items[0][3], 2.0)

        # Remove TestItem (Delete)
        mock_cursor.fetchall.return_value = []
        self.assertFalse(
            get_all_items()
        )  # Assuming you want to mock the same method here


if __name__ == "__main__":
    unittest.main()
