class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return '"{0}" is made by {1}, in {2}. Painting medium is {3}. \nThis art work is owned by {4} and it is currently located in {5}.'.format(self.title, self.artist, self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new_listing):
    return self.listings.append(new_listing)
  def remove_listing(self, old_listing):
    return self.listings.remove(old_listing)
  def show_listings(self):
    for listing in self.listings:
      print(listing)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = 'Private Collection'
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      veneer.add_listing(Listing(artwork, price, self))
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listingss in veneer.listings:
        if listingss.art == artwork:
          art_listing = listingss
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price 
    self.seller = seller
  def __repr__(self):
    return '{0} : ${1}.'.format(self.art.title, self.price)

Heeone = Client('Heeone Lee', None, False)
Josh = Client('Josh Rees', 'London', True)

Cow = Art('Jungsup Lee', 'Cow', 'oil on paper', 1954, Heeone) 

veneer = Marketplace()

Heeone.sell_artwork(Cow, '650M')
veneer.show_listings()

Josh.buy_artwork(Cow)
print(Cow)
veneer.show_listings()


   