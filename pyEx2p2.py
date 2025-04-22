# Online Store Order Calculation
# This program calculates the total cost of an order based on item price, quantity, shipping fees, and discounts.
item_price = float(input("Enter the item price: "))
quantity = int(input("Enter the quantity: "))
total = item_price * quantity

# Step 2: Add shipping fee (free if total > 200)
shipping_fee = 0
if total <= 200:
    shipping_fee = 20   
    print("Shipping fee of $20 applied.")
else:
    print("Free shipping applied.")

# Step 3: Apply discount if total > 500
discount = 0
if total > 500:
    discount = total * 0.10
    print("10% discount applied.")

# Final total
final_total = total - discount + shipping_fee

# Step 4: Print the summary
print("\n--- Order Summary ---")
print(f"Item price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${total:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"Shipping fee: ${shipping_fee:.2f}")
print(f"Total cost: ${final_total:.2f}")