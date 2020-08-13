hairstyles = ["shortcut", "bobcut", "sandcut", "buildcut", "bonniecut", "suzyhair", "hyaegyocut", "bang"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0
for ti in prices:
  total_price += ti
average_price = total_price/len(prices)
print(average_price)
new_prices = [i-5 for i in prices]
print(new_prices)
total_revenue = 0
for i in range(0,len(hairstyles)):
  total_revenue +=  (prices[i]*last_week[i])
print(total_revenue)
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

cuts_under_30 = [ hairstyles[i] for i in range(0,8) if new_prices[i] < 30]
print(cuts_under_30)