# input: Integer (Inventory ID), list containing transaction(dictionaries)
# output: Boolean True or False
# rules:
#   Explicit:
#       - Return True if the sum of the quantity values of the
#         inventory is greater than 0.
#       - To calculate inventory id quantity value based on movement
#         value. 'out' will decrease the quantity, 'in' will increase
#         the quantity.
#       - We should use previous exercise function.
# Examples / Test Cases:
#   transactions = [
    #   {"id": 101, "movement": 'in',  "quantity":  5},
    #   {"id": 105, "movement": 'in',  "quantity": 10},
    #   {"id": 102, "movement": 'out', "quantity": 17},
    #   {"id": 101, "movement": 'in',  "quantity": 12},
    #   {"id": 103, "movement": 'out', "quantity": 20},
    #   {"id": 102, "movement": 'out', "quantity": 15},
    #   {"id": 105, "movement": 'in',  "quantity": 25},
    #   {"id": 101, "movement": 'out', "quantity": 18},
    #   {"id": 102, "movement": 'in',  "quantity": 22},
    #   {"id": 103, "movement": 'out', "quantity": 15},
#   ]

#   print(is_item_available(101, transactions) == False)  # True
#   print(is_item_available(103, transactions) == False)  # True
#   print(is_item_available(105, transactions) == True)   # True
# Data Structure and Algorithm:
#   - Intialize net_quantity = 0
#   - Iterate over each transaction for inventory_id
#       - If movement value is in
#           increase net_quantity by quantity value
#       - Else if movement value is out
#           decrease net_quantity value by quantity value
#   - Return net_quantity greater than 0

def transactions_for(inventory_id, transactions):
    inventory_id_transactions = []
    for transaction in transactions:
        if transaction['id'] == inventory_id:
            inventory_id_transactions.append(transaction)

    return inventory_id_transactions

def is_item_available(inventory_id, transactions):
    net_quantity = 0
    for transaction in transactions_for(inventory_id, transactions):
        if transaction['movement'] == 'in':
            net_quantity += transaction['quantity']
        elif transaction['movement'] == 'out':
            net_quantity -= transaction['quantity']
    
    return net_quantity > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True