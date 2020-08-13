toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2000,6000,1000,3000,2000,7000,2000]
num_pizzas = len(toppings)

print("We have "+str(num_pizzas)+" different kinds of pizza!")
print('Have a look on the menu below!')
pizzas = list(zip(prices, toppings))
pizzas.sort()
print(pizzas)
print(" ")
cheapest_pizza = pizzas[1]
print('Cheapeast one is '+str(cheapest_pizza))
priciest_pizza = pizzas[-1]
print('The most expensive one is '+str(priciest_pizza))
three_cheapest = pizzas[:3]
print('Top 3 cheapest pizzas are ' +str(three_cheapest))

num_2000_pizza=prices.count(2000)
print('We have '+ str(num_2000_pizza)+' pizzas that are only 2000won!') 