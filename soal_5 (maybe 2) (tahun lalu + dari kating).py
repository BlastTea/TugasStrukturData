class Node:
  def __init__(self, data):
    self.item = data
    self.ref = None

class LinkedList:
  def __init__(self):
    self.start_node = None
  
  def traverse_list(self):
    if self.start_node is None:
      print("List has no element")
      return
    else:
      n = self.start_node
      while n is not None:
          print(n.item , " ")
          n = n.ref

  def insert_at_start(self, data):
    new_node = Node(data)
    new_node.ref = self.start_node 
    self.start_node= new_node
  
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.start_node is None:
        self.start_node = new_node
        return
    n = self.start_node
    while n.ref is not None:
        n= n.ref
    n.ref = new_node

  def insert_after_item(self, x, data):
    n = self.start_node
    print(n.ref)
    while n is not None:
        if n.item == x:
            break
        n = n.ref
    if n is None:
        print("item not in the list")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node
  
  def insert_before_item(self, x, data):
    if self.start_node is None:
      print("List has no element")
      return

    if x == self.start_node.item:
      new_node = Node(data)
      new_node.ref = self.start_node
      self.start_node = new_node
      return

    n = self.start_node
    print(n.ref)
    while n.ref is not None:
      if n.ref.item == x:
          break
      n = n.ref
    if n.ref is None:
      print("item not in the list")
    else:
      new_node = Node(data)
      new_node.ref = n.ref
      n.ref = new_node
  
  def insert_at_index (self, index, data):
    if index == 1:
      new_node = Node(data)
      new_node.ref = self.start_node
      self.start_node = new_node
    i = 1
    n = self.start_node
    while i < index-1 and n is not None:
      n = n.ref
      i = i+1
    if n is None:
        print("Index out of bound")
    else: 
      new_node = Node(data)
      new_node.ref = n.ref
      n.ref = new_node

  def delete_at_start(self):
    if self.start_node is None:
      print("The list has no element to delete")
      return
    self.start_node = self.start_node.ref

  def delete_at_end(self):
    if self.start_node is None:
      print("The list has no element to delete")
      return

    n = self.start_node
    while n.ref.ref is not None:
      n = n.ref
    n.ref = None

  def get_count(self):
    if self.start_node is None:
      return 0
    n = self.start_node
    count = 0
    while n is not None:
      count = count + 1
      n = n.ref
    return count
  
  def get_sum(self):
    if self.start_node is None:
      return 0
    n = self.start_node
    sum_ = 0
    while n is not None:
      sum_ = sum_ + n.item
      n = n.ref
    return sum_

  def search_item(self, x):
    if self.start_node is None:
      print("List has no elements")
      return
    n = self.start_node
    while n is not None:
      if n.item == x:
        print("Item found")
        return True
      n = n.ref
    print("item not found")
    return False

  def delete_element_by_value(self, x):
    if self.start_node is None:
      print("The list has no element to delete")
      return

    # Deleting first node
    if self.start_node.item == x:
      self.start_node = self.start_node.ref
      return

    n = self.start_node
    while n.ref is not None:
        if n.ref.item == x:
            break
        n = n.ref

    if n.ref is None:
        print("item not found in the list")
    else:
        n.ref = n.ref.ref

  def print_list(self):
    list_all = []
    if self.start_node is None:
      print("List has no element")
      return
    else:
      n = self.start_node
    while n is not None:
      list_all.append(n.item)
      n = n.ref
    return print(list_all)

  def merge_linked_list(self, other_linked_list):
    start_node_other = other_linked_list.start_node
    if self.start_node is None:
        self.start_node = start_node_other
        return
    n = self.start_node
    while n.ref is not None:
        n= n.ref
    n.ref = start_node_other
  
  def sort_linked_list(self):
    current = self.start_node  
    index = None  
      
    if(self.start_node == None):  
      return  
    else:  
      while(current != None):  
        index = current.ref  
            
        while(index != None):  
          if(current.item > index.item):  
            temp = current.item  
            current.item = index.item  
            index.item = temp  
          index = index.ref
        current = current.ref 
  
  def reverse(self):
    prev = None
    current = self.start_node
    while current is not None :
      next_ = current.ref
      current.ref = prev
      prev = current
      current = next_
    self.start_node = prev
      
# TUGAS NO 1
linked_list = LinkedList()
linked_list.insert_at_start(9)
print("Isi list setelah memasukkan data 9 di awal :")
linked_list.traverse_list()
linked_list.insert_at_start(2)
print("Isi list setelah memasukkan data 2 di awal :")
linked_list.traverse_list()
linked_list.insert_at_end(6)
print("Isi list setelah memasukkan data 6 di akhir :")
linked_list.traverse_list()
linked_list.insert_at_end(11)
print("Isi list setelah memasukkan data 11 di akhir :")
linked_list.traverse_list()
linked_list.insert_at_index(0,2)
print("Isi list setelah memasukkan data 2 di indeks pertama :")
linked_list.traverse_list()
linked_list.insert_at_index(4,12)
print("Isi list setelah memasukkan data 12 di indeks 4 :")
linked_list.traverse_list()
print("maka isi list secara keseluruhan adalah :")
linked_list.print_list()    

# TUGAS NO 2
linked_list = LinkedList()
linked_list.insert_at_start(3)
linked_list.print_list()
linked_list.insert_at_start(65)
linked_list.print_list()
linked_list.insert_at_start(1)
linked_list.print_list()
linked_list.insert_at_start(3)
linked_list.print_list()
linked_list.insert_at_end(10)
linked_list.print_list()
linked_list.insert_at_end(9)
linked_list.print_list()
linked_list.insert_at_end(12)
linked_list.print_list()
linked_list.insert_at_end(5)
linked_list.print_list()
linked_list.insert_at_index(4,40)
linked_list.print_list()
linked_list.insert_at_index(7,13)
linked_list.print_list()
linked_list.delete_at_start()
linked_list.print_list()
linked_list.delete_at_end()
linked_list.print_list()
linked_list.delete_element_by_value(10)
linked_list.print_list()
linked_list.delete_element_by_value(8)


# TUGAS NO 3
linked_list.reverse()
linked_list.print_list()
linked_list.sort_linked_list()
linked_list.print_list()
print(linked_list.get_count())
print(linked_list.get_sum())


linked_list2 = LinkedList()
linked_list2.insert_at_start(3)
linked_list2.insert_at_start(22)
linked_list2.insert_at_start(3)
linked_list2.insert_at_start(40)
linked_list2.insert_at_end(10)
linked_list2.insert_at_end(33)
linked_list2.insert_at_end(1)
linked_list2.insert_at_end(11)
linked_list2.insert_at_index(4,40)
linked_list2.insert_at_index(7,13)
linked_list2.delete_at_start()
linked_list2.delete_at_end()
linked_list2.traverse_list()
linked_list2.delete_element_by_value(10)
linked_list2.delete_element_by_value(8)
linked_list2.print_list()
linked_list2.reverse()
linked_list2.print_list()
print(linked_list2.get_count())
print(linked_list2.get_sum())


linked_list.merge_linked_list(linked_list2)
linked_list.print_list()