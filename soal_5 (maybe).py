import os
os.system('cls')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method untuk mencari banyaknya anggota linked list
    def count_members(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Method untuk menghitung jumlah (sum) semua bilangan dalam linked list
    def sum_all(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    # Method untuk menyambung dua linked list
    def concatenate(self, other_list, append=True):
        if not other_list.head:
            return

        if append:
            current = self.head
            while current.next:
                current = current.next
            current.next = other_list.head
        else:
            other_list_end = other_list.head
            while other_list_end.next:
                other_list_end = other_list_end.next
            other_list_end.next = self.head
            self.head = other_list.head

    # Method untuk menambahkan data ke linked list dalam kondisi terurut
    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and data > current.next.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Method untuk membalik arah semua pointer di linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Method untuk menampilkan isi linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Contoh penggunaan:
linked_list1 = LinkedList()
linked_list1.insert_sorted(10)
linked_list1.insert_sorted(5)
linked_list1.insert_sorted(8)

linked_list2 = LinkedList()
linked_list2.insert_sorted(3)
linked_list2.insert_sorted(12)
linked_list2.insert_sorted(7)

print("Linked List 1:")
linked_list1.display()
print("Linked List 2:")
linked_list2.display()

linked_list1.concatenate(linked_list2, append=True)
print("Linked List 1 setelah penggabungan (append):")
linked_list1.display()

linked_list1.reverse()
print("Linked List 1 setelah pembalikan:")
linked_list1.display()

print("Jumlah anggota Linked List 1:", linked_list1.count_members())
print("Jumlah seluruh bilangan Linked List 1:", linked_list1.sum_all())
