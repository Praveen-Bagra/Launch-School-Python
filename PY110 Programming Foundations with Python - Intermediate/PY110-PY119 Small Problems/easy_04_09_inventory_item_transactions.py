# input: Integer (Inventory ID), List containing dictionaries (ransactions)
# output: new list
# rules:
#   Explicit:
#       - Returns a list containing only the transactions for the 
#         specified inventory item.
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

#   print(transactions_for(101, transactions) ==
      # [
          # {"id": 101, "movement": "in",  "quantity":  5},
          # {"id": 101, "movement": "in",  "quantity": 12},
          # {"id": 101, "movement": "out", "quantity": 18},
      # ]) # True
# Data Structure and Algorithm:
#   - inventory_id_tranasctions = []
#   - Iterate over each transaction (dictionary)
#       - Check dictionary id, if it is equal to inventory_id
#           - add transaction to inventory_id_transactions
#   - Return inventory_id_transactions list.

def transactions_for(inventory_id, transactions):
#       inventory_id_transactions = []
    #   for transaction in transactions:
        #   if transaction['id'] == inventory_id:
            #   inventory_id_transactions.append(transaction)

    #   return inventory_id_transactions
    return [transaction for transaction in transactions
                        if transaction['id'] == inventory_id]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True