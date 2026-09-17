def maxProfit_bruteforce (prices):
   max_price = 0

   for i, price in enumerate(prices):
       for j in range(i, len(prices)):
           min_price = min(prices[j] - price, min_price)

   return

