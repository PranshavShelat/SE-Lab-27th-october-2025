"""Simple inventory system module."""

import json
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Adds a specified quantity of an item."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not item:
        logging.warning(
            "Invalid item name: %s. Must be a non-empty string.", item
        )
        return
    if not isinstance(qty, int):
        logging.warning(
            "Invalid quantity: %s for item %s. Must be an integer.", qty, item
        )
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    log_msg = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_msg)
    logging.info(log_msg)


def remove_item(item, qty):
    """Removes a specified quantity of an item."""
    if not isinstance(item, str) or not item:
        logging.warning(
            "Invalid item name: %s. Must be a non-empty string.", item
        )
        return
    if not isinstance(qty, int):
        logging.warning(
            "Invalid quantity: %s for item %s. Must be an integer.", qty, item
        )
        return

    try:
        if stock_data[item] <= qty:
            logging.info("Removed item %s (all stock taken).", item)
            del stock_data[item]
        else:
            stock_data[item] -= qty
            logging.info("Removed %s of %s. New total: %s", qty, item, stock_data[item])
    except KeyError:
        logging.warning(
            "Attempted to remove non-existent item: %s", item
        )


def get_quantity(item):
    """Gets the current quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("Data file not found: %s. Starting fresh.", file)
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from %s. Starting fresh.", file)
        return {}


def save_data(file="inventory.json"):
    """Saves the current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
            logging.info("Inventory saved to %s", file)
    except IOError as e:
        logging.error("Error saving data to %s: %s", file, e)


def print_data():
    """Prints a report of all items and their quantities."""
    print("\n--- Items Report ---")
    if not stock_data:
        print("Inventory is empty.")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("--------------------\n")


def check_low_items(threshold=5):
    """Finds all items at or below a given threshold."""
    return [
        item for item, quantity in stock_data.items()
        if quantity <= threshold
    ]


def main():
    """Main function to run the inventory system demo."""
    global stock_data
    stock_data = load_data()

    add_item("apple", 10)
    add_item("banana", 15)

    add_item(123, "ten")  # invalid types, no check

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_quantity('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    print_data()

    # eval("print('eval used')")  # dangerous
    logging.info("Main execution finished.")


if __name__ == "__main__":
    main()

