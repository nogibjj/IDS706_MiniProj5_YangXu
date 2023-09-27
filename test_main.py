from main import (
    create_table,
    insert_item,
    get_all_items,
    update_item_price,
    get_items_by_product,
    delete_item,
)


def test_crud_operations():
    # Create table
    create_table()

    # Insert data (Create)
    insert_item("2023-09-04", "TestItem", 1.5, 30)

    # Fetch data (Read)
    items = get_all_items()
    last_item = items[-1]
    assert last_item[1] == "2023-09-04"
    assert last_item[2] == "TestItem"
    assert last_item[3] == 1.5
    assert last_item[4] == 30

    # Update the price for TestItem (Update)
    update_item_price("TestItem", 2.0)
    updated_items = get_items_by_product("TestItem")
    assert updated_items[0][3] == 2.0

    # Remove TestItem (Delete)
    delete_item("TestItem")
    assert not get_items_by_product("TestItem")
