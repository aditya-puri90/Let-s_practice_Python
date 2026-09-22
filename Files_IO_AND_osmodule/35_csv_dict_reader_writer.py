'''Q35. CSV DictReader and DictWriter

Read and write CSV files using dictionary mappings for structured header and column management.
'''

import csv

fieldnames = ["id", "product", "price", "stock"]
products = [
    {"id": "101", "product": "Mechanical Keyboard", "price": "2500", "stock": "15"},
    {"id": "102", "product": "Wireless Mouse", "price": "1200", "stock": "30"},
    {"id": "103", "product": "4K Monitor", "price": "22000", "stock": "8"}
]

with open("products.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print("products.csv written using DictWriter.")

print("\nReading products.csv using DictReader:")
with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Product #{row['id']}: {row['product']} - Price: Rs. {row['price']} (Stock: {row['stock']})")
