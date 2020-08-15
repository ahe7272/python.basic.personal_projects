flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'], ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()

class HashMap:
  
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
    
  def hash(self, key):
    return sum(key.encode())
    
  def compress(self, hash_code):
    return hash_code%self.array_size
  
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for array in list_at_array:
      if array[0] == key:
        array[1] = value
        return
    list_at_array.insert(payload)
        
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    for array in list_at_array:
      if array[0] == key:
        return array[1]
    return None
      
blossom = HashMap(len(flower_definitions))
for definition in flower_definitions:
  blossom.assign(definition[0], definition[1])
  
print(blossom.retrieve('daisy'))

