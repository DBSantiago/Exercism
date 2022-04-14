""" This modules has functions for inventory management.
"""


def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    inventory = {}

    for item in items:
        inventory[item] = items.count(item)

    return inventory


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    items_to_add = create_inventory(items)

    for key, value in items_to_add.items():
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    items_to_decrease = create_inventory(items)

    for key, value in items_to_decrease.items():
        if key in inventory:
            if inventory[key] - value < 0:
                inventory[key] = 0
            else:
                inventory[key] -= value

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    for key in inventory:
        if key == item:
            inventory.pop(item)
            break

    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []

    for key in inventory:
        if inventory[key] > 0:
            inventory_list.append(tuple([key, inventory[key]]))

    return inventory_list
