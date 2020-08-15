hairstyles = ["shortcut", "bobcut", "sandcut", "buildcut", "bonniecut", "suzyhair", "hyaegyocut", "bang"]
prices = [12000, 18000, 22000, 28000, 17000, 29000, 35000, 29000]
stylebook = list(zip(hairstyles, prices))
print("Welcome to Heeone's hairsalon. We do fabulous hairstyles. Check our stylebook!")
print(stylebook)
print('')
total_price = 0
for ti in prices:
  total_price += ti
average_price = total_price/len(prices)
print('Average price for our hairstyles is '+str(average_price)+'won.')
print('')
print('You are lucky! we do offer for this weekend, which is 5000won off for each styles.')
new_prices = [i-5000 for i in prices]
print('Have a look on our new style book with new prices.')
new_stylebook = list(zip(new_prices, hairstyles))
print(new_stylebook)
print('')
print('Looking for cheap but stylish hairstyle? How about these hairs?')
cuts_under_15000 = [ hairstyles[i] for i in range(0,8) if new_prices[i] < 15000]
print(cuts_under_15000)

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_revenue = 0
for i in range(0,len(hairstyles)):
  total_revenue +=  (prices[i]*last_week[i])

print('')

#수익 계산하기 
print('We had done'+str(last_week)+ ' times of each hairstyle for the last week.')
print('The total revenue from last week is '+str(total_revenue))
average_daily_revenue = round(total_revenue/7)
print('')
print('Then we can come to conclusion that we make '+str(average_daily_revenue)+ 'won per day.')

