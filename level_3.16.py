# Create a shopping bill that accepts the price and quantity of three products and displays the total bill.

product_1 = input("\nEnter 1st product name: ")
price_1 = int(input(f"Enter {product_1} price: "))
qty_1 = int(input(f"Enter quantity of {product_1}: "))

product_2 = input("\nEnter 2nd product name: ")
price_2 = int(input(f"Enter price of {product_2} : "))
qty_2 = int(input(f"Enter quantity of {product_2}: "))

product_3 = input("\nEnter 3rd product name: ")
price_3 = int(input(f"Enter price of {product_3}: "))
qty_3 = int(input(f"Enter quantity of {product_3}: "))

total = price_1 * qty_1 + price_2 * qty_2 + price_3 * qty_3

print(f"""
{'=' * 36}
{'SHOPPING BILL':^36}
{'=' * 36}
{'Product Name':<18} {'Qty':>6} {'Price':>10}
{'-' * 36}
{product_1:<18} {qty_1:>5} {price_1:>10.2f}
{'-' * 36}
{product_2:<18} {qty_2:>5} {price_2:>10.2f}
{'-' * 36}
{product_3:<18} {qty_3:>5} {price_3:>10.2f}
{'-' * 36}
Total Bill  :  Rs.{total}
{'-' * 36}
{'THANK YOU, DO VISIT AGAIN !!':^36}
""")


