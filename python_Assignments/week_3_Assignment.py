def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount (if 20% or higher), otherwise original price
    """
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Main program
def main():
    try:
        # Get user input
        price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Display results
        if discount_percent >= 20:
            print(f"\nDiscount applied: {discount_percent}%")
            print(f"Original price: ${price:.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
            print(f"You saved: ${price - final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Price remains: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()

# Example usage and test cases
print("\n" + "="*50)
print("EXAMPLE TEST CASES:")
print("="*50)

# Test cases
test_cases = [
    (100, 25),    # Should apply 25% discount
    (50, 15),     # Should not apply discount (less than 20%)
    (200, 30),    # Should apply 30% discount
    (75, 20),     # Should apply exactly 20% discount
]

for price, discount in test_cases:
    result = calculate_discount(price, discount)
    if discount >= 20:
        savings = price - result
        print(f"Price: ${price}, Discount: {discount}% → Final: ${result:.2f} (Saved: ${savings:.2f})")
    else:
        print(f"Price: ${price}, Discount: {discount}% → Final: ${result:.2f} (No discount applied)")
