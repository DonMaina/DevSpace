# Step 1: Define the function
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise, return original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Helper function to format numbers cleanly
def format_price(value):
    return int(value) if value.is_integer() else round(value, 2)

# Step 2: Loop until the user chooses to quit
while True:
    try:
        price = float(input("Enter the original price of the item (or 0 to quit): "))
        if price == 0:
            print("Exiting discount calculator. Goodbye!")
            break

        discount_percent = float(input("Enter the discount percentage: "))

        # Call the function
        final_price = calculate_discount(price, discount_percent)

        # Display result
        if discount_percent >= 20:
            print(f"✅ Discount applied! Final price: {format_price(final_price)}\n")
        else:
            print(f"ℹ️ No discount applied. Final price: {format_price(final_price)}\n")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.\n")
