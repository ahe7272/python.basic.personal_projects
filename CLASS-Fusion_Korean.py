class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return '{0} menu is available from {1}:00 to {2}:00.'.format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    order = ', '.join(purchased_items)
    for food, price in self.items.items():
      for purchase in purchased_items:
        if food == purchase:
          total += price
          
    return 'Let me check your order again. They are {0}. Total is {1} won.'.format(order, total)


brunch = Menu('Brunch', {'salad and bread': 12000, 'dumplings': 9000, 'burger': 11000, 'home fries': 3400, 'coffee': 2500, 'latte': 3000, 'tea': 2500, 'cereal': 10500, 'orange juice': 2500}, 11, 16)

early_bird = Menu('Early_bird', {'bibimbap': 8000, 'salad and bread': 12000, 'pizza with cheese': 9000, 'soybean soup': 11500, 'mushroom soup': 9500, 'coffee': 2500, 'latte': 3000}, 15,18)

dinner = Menu('Dinner',{'bulgogi': 13000, 'kimchi pancake': 16000, 'pizza with cheese': 9000, 'camp soup': 19500, 'mushroom soup': 9500, 'coffee': 2500, 'latte': 3000}, 17,23)

kids = Menu('Kids', {'chicken nuggets': 6500, 'mushroom soup': 7500, 'apple juice': 3000}, 11, 21)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return 'Hi! this is one of our franchise restaurants located in {0}.'.format(self.address)

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_time <= time and menu.end_time >= time:
        available.append(menu.name)
    return 'Available menus for {0}:00 are {1} menu.'.format(time, ', '.join(available))

Itaewon = Franchise('1133ro, Itaewon, Seoul',[brunch, early_bird, dinner, kids])
Hongdae = Franchise('1133ro, Hongdae, Seoul', [brunch, early_bird, dinner, kids])

Seaside_menu = Menu('Seaside_menu', {'pork soup': 7000, 'seed pancake': 2500, 'Lobster ramyeon': 12000, 'seashell salad': 13000}, 10, 20)
Busan = Franchise("1922ro, Haeundae, Busan",[Seaside_menu])

print('Welcome to our Fusion Korean restaurant Itaewon!')
print('Let me check what menus are available. '+ str(Itaewon.available_menus(17)))
print('Thank you for your order!\nTotal bill is '+str(early_bird.calculate_bill(['bibimbap', 'salad and bread'])))
print('')