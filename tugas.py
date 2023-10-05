import os
os.system('cls')

# soal 1
def fibonacci(num):
    if (num <= 1):
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

print(f'5 : {fibonacci(5)}')
print(f'7 : {fibonacci(7)}')
print(f'10 : {fibonacci(10)}')

print(f'4 : {fibonacci(4)}')

# soal 2
print("\n")
def is_palindrome_list(nums):
    if len(nums) <= 1:
        return True
    if nums[0] != nums[-1]:
        return False
    return is_palindrome_list(nums[1:-1])

print(is_palindrome_list([1,2,3,4,4,3,2,1]))

# soal 3
print("\n")
class DuaDimensi:
  x = 0
  y = 0

  def __init__(self,x,y):
    self.x = x
    self.y = y
  def geserHorizontal(self,dx):
    self.x += dx
  def geserVertikal(self,dy):
    self.y += dy
  def hitungJarak(self, titikLain):
    jarak_x = titikLain.getX() - self.getX()
    jarak_y = titikLain.getY() - self.getY()
    jarak = (jarak_x**2 + jarak_y**2)**0.5
    return jarak 
  def getX(self):
    return self.x
  def getY(self):
    return self.y

# soal 4  
print("\n")
t1 = DuaDimensi(2,3)  
t2 = DuaDimensi(4,5) 

t1.geserHorizontal(-3)
t1.geserVertikal(-7)
print("Koordinat titik t1 = ", (t1.getX(), t1.getY()))

t2.geserHorizontal(15)
t2.geserVertikal(9)
print("Koordinat titik t2 = ", (t2.getX(), t2.getY()))

print(t1.hitungJarak(t2))

# soal 5
print("\n")
class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

class LinkedListInteger():
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, value):
        'Menambahkan node baru di awal linked list'
        new_node = Node(value)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, value):
        'Menambahkan node baru di akhir linked list'
        new_node = Node(value)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_before_item(self, oldValue, newValue):
        'Menambahkan data sebelum node tertentu'
        if self.start_node is None:
            return print('List has no element')

        if oldValue == self.start_node:
            new_node = Node(newValue)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node

        while n.ref is not None:
            if n.ref.value == oldValue:
                break
            n = n.ref

        if n.ref is None:
            return print('Item not in the list')

        new_node = Node(newValue)
        new_node.ref = n.ref
        n.ref = new_node

    def insert_after_item(self, oldValue, newValue):
        'Menyisipkan data setelah node tertentu'
        n = self.start_node

        while n is not None:
            if n.value == oldValue:
                break
            n = n.ref

        if n is None:
            return print('Item not in the list')

        new_node = Node(newValue)
        new_node.ref = n.ref
        n.ref = new_node

    def delete_at_start(self):
        'Penghapusan node di awal node'
        if self.start_node is None:
            return print('The list has no element to delete')

        self.start_node = self.start_node.ref

    def delete_at_end(self):
        'Penghapusan node di akhir node'
        if self.start_node is None:
            return print('The list has no element to delete')

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def length(self):
        'Menghitung banyaknya anggota'
        if self.start_node is None:
            return 0

        n = self.start_node
        length = 0

        while n is not None:
            length += 1
            n = n.ref

        return print(length)

    def contains(self, value):
        'Mengecek apakah list berisi value'

        n = self.start_node
        while n is not None:
            if n.value == value:
                return True
            n = n.ref
        return False

    def delete_element_by_value(self, value):
        'Menghapus node yang memiliki nilai tertentu'
        if self.start_node is None:
            return print('The list has no element to delete')

        n = self.start_node
        while n is not None:
            if n.value == value:
                pass
        # TODO: Implement this method :)

    def sum(self):
        'Menghitung jumlah semua bilangan di dalam list'
        sum = 0

        currentNode = self.start_node
        while currentNode is not None:
            sum += currentNode.value
            currentNode = currentNode.ref

        return sum

    def insert_all(self, otherList, append=True):
        'Method untuk menyambung dua linked list'
        if not otherList.start_node:
            return

        if append:
            current = self.start_node
            while current.ref:
                current = current.ref
            current.ref = otherList.start_node
        else:
            other_list_end = otherList.start_node
            while other_list_end.ref:
                other_list_end = other_list_end.ref
            other_list_end.ref = self.start_node
            self.start_node = otherList.start_node

    def insert_sorted(self, value):
        'Method untuk mengurutkan linked list'
        current = self.start_node  
        index = None  
        
        if(self.start_node == None):  
            return  
        else:  
            while(current != None):  
                index = current.ref  
                    
                while(index != None):  
                    if(current.value > index.value):  
                        temp = current.value  
                        current.value = index.value  
                        index.value = temp  
                    index = index.ref
                current = current.ref
        'Method untuk menambahkan data ke linked list dalam kondisi terurut'
        new_node = Node(value)
        if not self.start_node or value < self.start_node.value:
            new_node.ref = self.start_node
            self.start_node = new_node
        else:
            current = self.start_node
            while current.ref and value > current.ref.value:
                current = current.ref
            new_node.ref = current.ref
            current.ref = new_node

    def reverse(self):
        'Method untuk membalik arah semua pointer di linked list'
        prev = None
        current = self.start_node
        while current:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.start_node = prev

    def traverse_list(self):
        'Mencetak seluruh isi list'
        data = '['

        currentNode = self.start_node

        if (currentNode is None):
            data += ']'
            return print(data)

        while currentNode is not None:
            if currentNode.ref is not None:
                data += f'{currentNode.value}, '
            else:
                data += f'{currentNode.value}'

            currentNode = currentNode.ref

        data += ']'

        print(data)

linkedListInteger = LinkedListInteger()
linkedListInteger.traverse_list()

linkedListInteger.insert_at_start(3)
linkedListInteger.insert_at_end(5)
linkedListInteger.insert_at_end(10)
linkedListInteger.traverse_list()

#2
print(linkedListInteger.sum())

linkedListInteger2 = LinkedListInteger()
linkedListInteger2.insert_at_end(7)
linkedListInteger2.insert_at_end(6)

#3
linkedListInteger.insert_all(linkedListInteger2)
linkedListInteger.traverse_list()

#4
linkedListInteger.insert_sorted(11)
linkedListInteger.traverse_list()

# 1
linkedListInteger.length()

#5
linkedListInteger.reverse()
linkedListInteger.traverse_list()