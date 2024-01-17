def calculate_discount(cart_total, quantities):
    flat_10_discount = 0
    bulk_5_discount = 0
    bulk_10_discount = 0
    tiered_50_discount = 0

    
    if cart_total > 200:
        flat_10_discount = 10

    for quantity in quantities:
        if quantity > 10:
            bulk_5_discount = max(bulk_5_discount, 0.05)

    if sum(quantities) > 20:
        bulk_10_discount = 0.1

    if sum(quantities) > 30 and max(quantities) > 15:
        tiered_50_discount = 0.5

    max_discount = max(flat_10_discount, bulk_5_discount, bulk_10_discount, tiered_50_discount)

    return max_discount


def main():
    products = ["Product A", "Product B", "Product C"]
    prices = {"Product A": 20, "Product B": 40, "Product C": 50}
    quantities = []

    for product in products:
        quantity = int(input(f"Enter quantity of {product}: "))
        quantities.append(quantity)

    gift_wrap_fee = sum(quantities)
    shipping_fee = (sum(quantities) + 9) // 10 * 5

    subtotal = sum(prices[product] * quantity for product, quantity in zip(products, quantities))
    discount_amount = calculate_discount(subtotal, quantities)
    total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

    # Display details
    for product, quantity in zip(products, quantities):
        print(f"{product}: Quantity: {quantity}, Total: ${prices[product] * quantity}")

    print(f"\nSubtotal: ${subtotal}")
    print(f"Discount Applied: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
