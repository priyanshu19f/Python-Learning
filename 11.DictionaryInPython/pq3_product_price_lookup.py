"""
Q81: Product Price Lookup (HW)
Construct a dictionary containing four product names and their prices. Prompt
the user to enter a product name. Use the in keyword to check if it exists; if
so, display its price. Otherwise, inform the user "Product not found."
"""

product = {
    "laptop": 50000,
    "phone": 20000,
    "tablet": 30000,
    "headphone": 4500,
}

user_prompt = input("Enter product name : ").lower()
if user_prompt in product:
    print(f"{user_prompt} : Rs {product[user_prompt]}")
else:
    print("Product not found.")
