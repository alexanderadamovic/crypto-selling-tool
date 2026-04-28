coin_input = input(f"Which coin do you own? ")
amount_invested = float(input(f"What was the amount of your investment? "))
buy_price = float(input(f"What was the buy price? "))
current_price = float(input(f"What is the current price? "))
sell_target = float(input(f"What is your sell target %? "))
stop_loss = float(input(f"What is your stop loss %? "))

# Price Change Calulation 
price_change = current_price - buy_price
percentage_change = (price_change / buy_price) * 100

if percentage_change>= sell_target:
    print(f"Sell")
elif percentage_change <= -stop_loss:
    print(f"Stop Loss")
else:
    print(f"Hold")

profit = amount_invested * (percentage_change / 100)

print(profit)
print(percentage_change)
