"""
Billing System (OOP-based)
--------------------------
Classes:
    Product -> name, price, quantity (+ line total)
    Bill    -> holds products, calculates subtotal, tax, grand total
               and prints the final bill in tabular format
"""

from datetime import datetime


class Product:
    """Represents a single product on the bill."""

    def __init__(self, name, price, quantity):
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be >= 0 and quantity must be > 0.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Price of this line item (price x quantity)."""
        return self.price * self.quantity


class Bill:
    """Holds products and does all bill calculations."""

    def __init__(self, customer_name, tax_rate=18.0):
        self.customer_name = customer_name
        self.tax_rate = tax_rate          # in percent (GST)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def subtotal(self):
        return sum(p.total_price() for p in self.products)

    def tax_amount(self):
        return self.subtotal() * self.tax_rate / 100

    def grand_total(self):
        return self.subtotal() + self.tax_amount()

    def display(self):
        """Print the final bill in a tabular format."""
        width = 66
        print("\n" + "=" * width)
        print("INVOICE".center(width))
        print("=" * width)
        print(f"Customer : {self.customer_name}")
        print(f"Date     : {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        print("-" * width)
        print(f"{'S.No':<6}{'Product':<24}{'Price':>10}{'Qty':>8}{'Total':>14}")
        print("-" * width)

        for i, p in enumerate(self.products, start=1):
            print(f"{i:<6}{p.name:<24}{p.price:>10.2f}{p.quantity:>8}{p.total_price():>14.2f}")

        print("-" * width)
        print(f"{'Subtotal':<48}{self.subtotal():>18.2f}")
        print(f"{f'Tax ({self.tax_rate:g}%)':<48}{self.tax_amount():>18.2f}")
        print("=" * width)
        print(f"{'GRAND TOTAL':<48}{self.grand_total():>18.2f}")
        print("=" * width)
        print("Thank you for shopping with us!".center(width))


def read_number(prompt, cast=float):
    """Keep asking until a valid number is entered."""
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("  Invalid input, please enter a valid number.")


def main():
    print("===== BILLING SYSTEM =====")
    customer = input("Enter customer name: ").strip() or "Customer"
    tax = read_number("Enter tax rate in % (e.g. 18): ")
    bill = Bill(customer, tax)

    while True:
        print("\n1. Add product\n2. Generate bill\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("  Product name: ").strip()
            if not name:
                print("  Product name cannot be empty.")
                continue
            price = read_number("  Price: ")
            qty = read_number("  Quantity: ", int)
            try:
                bill.add_product(Product(name, price, qty))
                print(f"  '{name}' added.")
            except ValueError as e:
                print(f"  Error: {e}")

        elif choice == "2":
            if not bill.products:
                print("  No products added yet.")
            else:
                bill.display()
                break

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("  Invalid choice, try again.")


if __name__ == "__main__":
    main()
