def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
   
  first = 0
  last = len(data)-1
  while first <= last:
    mid = (first+last) //2
    if not data[mid]:
      left = mid - 1
      right = mid + 1
      while True:
        if left < first and right > last:
          print("{0} is not in the dataset".format(search_val))
          return ''
        elif right <= last and data[right]:
          mid = right
          break
        elif left >= first and data[left]:
          mid = left
          break
        right +=1
        left -=1
    if data[mid] == search_val:
      print("{0} found at position {1}".format(search_val, mid))
      return ''
    elif search_val < data[mid]:
      last = mid -1
    elif search_val > data[mid]:
      last = mid +1
  print(str(search_val) +' is not in the dataset.')

unordered1 = ["A", "", "", "", "B", "", "", "", "C", "", "", "D"]
unordered2 = ["A", "B", "", "", "E"]
unordered3 = ["", "X", "", "Y", "Z"]
unordered4 = ["A", "", "", "", "B", "", "", "", "C"]
unordered5 = ["Apple", "", "Banana", "", "", "", "", "Cow"]
unordered6 = ["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"]

print(sparse_search(unordered4, 'B'))