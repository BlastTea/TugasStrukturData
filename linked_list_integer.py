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
        'Menhitung banyaknya anggota'
        if self.start_node is None:
            return 0
        
        n = self.start_node
        length = 0
        
        while n is not None:
            length += 1
            n = n.ref

        return length

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

    def insert_all(self, otherList):
        pass

    def sort(self):
        pass

    def reverse(self):
        pass

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

print(linkedListInteger.sum())