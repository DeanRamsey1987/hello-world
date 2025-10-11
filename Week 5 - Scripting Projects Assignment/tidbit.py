def main():
    # Purchase Price
    price = float(input("Enter the purchase price: "))

    # Terms
    down_payment = 0.10 * price
    annual_rate = 0.12
    monthly_payment = 0.05 * price

    # Initial balance sans down
    balance = price - down_payment

    # Print headers
    print("\nTidBit Computer Store Payment Schedule")
    print(f"Purchase price: ${price:,.2f}")
    print(f"Down payment:   ${down_payment:,.2f}")
    print(f"Monthly payment (fixed): ${monthly_payment:,.2f}\n")

    print("{:<8}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        "Month", "Balance Owed", "Interest", "Principal", "Payment", "New Balance"))
    print("-" * 83)

    month = 0
    # Loop till paid
    while balance > 0:
        month += 1
        interest = balance * (annual_rate / 12)
        principal = monthly_payment - interest

        # Adjust final payment
        if principal > balance:
            principal = balance
            monthly_payment = principal + interest

        new_balance = balance - principal

        print("{:<8}{:<15,.2f}{:<15,.2f}{:<15,.2f}{:<15,.2f}{:<15,.2f}".format(
            month, balance, interest, principal, monthly_payment, new_balance))

        balance = new_balance


if __name__ == "__main__":
    main()
