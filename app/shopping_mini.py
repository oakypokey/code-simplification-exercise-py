
from datetime import datetime
import os
import sys

selected_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
] # FYI: for the purposes of this exercise, you won't need to modify this list at all

#RECEIPT FUNCTION
def printReceipt(outputFunction):
    outputFunction("---------" + "\n")
    outputFunction("CHECKOUT AT: " + str(now.strftime("%Y-%M-%d %H:%m:%S")) + "\n")
    outputFunction("---------" + "\n")
    for p in selected_products:
        outputFunction("SELECTED PRODUCT: " + p["name"] + "   " + '${:.0f}'.format(p["price"]) + "\n")
    outputFunction("---------" + "\n")
    outputFunction(f"SUBTOTAL: {subtotal:,.2f}" + "\n")
    outputFunction(f"TAX: {(subtotal * 0.0875):.2f}" + "\n")
    outputFunction(f"TOTAL: {((subtotal * 0.0875) + subtotal):.2f}" + "\n")
    outputFunction("---------" + "\n")
    outputFunction("THANK YOU! PLEASE COME AGAIN SOON!" + "\n")
    outputFunction("---------" + "\n")

now = datetime.now()
subtotal = sum([p["price"] for p in selected_products])

# PRINT RECEIPT
printReceipt(sys.stdout.write)

# WRITE RECEIPT TO FILE
file_name = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{now.strftime('%Y-%M-%d-%H-%m-%S')}.txt")
with open(file_name, 'w') as f:
    printReceipt(f.write)

# TODO: SEND RECEIPT VIA EMAIL
