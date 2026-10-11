"""
Q40. Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""

def discount_price(original_price, discount_percent):
    dis_price = (original_price * discount_percent)/100
    final_price = original_price - dis_price
    print(f"You will get a discount of Rs{dis_price}")
    print(f"Final Price : {final_price}")

discount_price(100, 10)
discount_price(555,5)
discount_price(1200,5)