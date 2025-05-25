import csv


def stock_portfolio_tracker():
    # Hardcoded dictionary of stock prices
    stock_prices = {
        'AAPL': 192.25,
        'GOOGL': 173.55,
        'MSFT': 420.72,
        'AMZN': 181.75,
        'TSLA': 248.50
    }

    portfolio = {}
    total_value = 0.0

    # Get user input for stocks and quantities
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter stock name and quantity (type 'done' to finish):")

    while True:
        stock = input("Stock name (or 'done'): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Invalid stock name! Please choose from available stocks.")
            continue
        try:
            quantity = int(input(f"Quantity for {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                continue
            portfolio[stock] = quantity
        except ValueError:
            print("Please enter a valid number for quantity!")

    # Calculate total investment value
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_value += value
        print(f"{stock}: {quantity} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

    # Save results to CSV file
    try:
        with open('portfolio.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Stock', 'Quantity', 'Price', 'Value'])
            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                writer.writerow([stock, quantity, stock_prices[stock], value])
            writer.writerow(['Total', '', '', total_value])
        print("Portfolio saved to portfolio.csv")
    except Exception as e:
        print(f"Error saving to file: {e}")


# Start the program
print("Welcome to Stock Portfolio Tracker!")
stock_portfolio_tracker()