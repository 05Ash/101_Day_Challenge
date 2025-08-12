def maximumProfit(prices) -> int:
    print(prices)
        # code here
    def calculate_current_profit(buy, sell):
        return sell - buy
    total_profit = 0
    buy_price = prices[0]
    sell_price = None
    for price in prices[1:]:
        if price < buy_price:

            if sell_price == None:
                buy_price = price
            else:
                total_profit += calculate_current_profit(buy_price, sell_price)
                buy_price = price
                sell_price = None
        elif price > buy_price:
            if sell_price == None:
                sell_price = price
            elif price <  sell_price:
                total_profit += calculate_current_profit(buy_price, sell_price)
                buy_price = price
                sell_price = None
            else:
                sell_price = price
            print(buy_price, sell_price, total_profit)

    if sell_price != None:
        total_profit += calculate_current_profit(buy_price, sell_price)
    print(total_profit)


    return total_profit

prices = "57 78 91 75 77 90 92 55 51 80 77 70 36 50 36 1 89 62 94 8 10 60 88 88 90 51 85 68 36 76 25 34 24 95 57 7 99 50 98 82 99 46 32 61 10 61 4 16 16 82 59 44 11 99 7 88 87 5 63 41 63 15 15 55 78 92 15 25 13 2 9 73 48 91 39 17 46 67 17 57 90 86 35 54"
prices1 = prices.split(" ")
prices2 = [int(price) for price in prices1]
print(prices2)

maximumProfit(prices2)
