# single_linked_list.py
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of bounds")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_node(self, position):
        if self.head is None:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("Position out of bounds")
                current = current.next
            current.next = current.next.next

    def display_reverse(self):
        def _display_reverse(node):
            if node:
                _display_reverse(node.next)
                print(node.data, end=' ')

        _display_reverse(self.head)
        print()

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

class Menu:
    def get_menu(self, linked_list):
        menu = {
            1: self.add_node,
            2: self.delete_node,
            3: self.display_reverse,
            4: self.display,
            5: self.end_of_program
        }
        self.linked_list = linked_list
        return menu

    def invalid_choice(self):
        print('Invalid choice entered')

    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        linked_list = SinglyLinkedList()
        while True:
            choice = int(input('1: Add node 2: Delete node 3: Display reverse 4: Display list 5: Exit. Your choice: '))
            menu = self.get_menu(linked_list)
            menu.get(choice, self.invalid_choice)()

    def add_node(self):
        data = int(input('Enter data: '))
        position = int(input('Enter position: '))
        try:
            self.linked_list.add_node(data, position)
        except IndexError as e:
            print(e)

    def delete_node(self):
        position = int(input('Enter position to delete: '))
        try:
            self.linked_list.delete_node(position)
        except IndexError as e:
            print(e)

    def display_reverse(self):
        self.linked_list.display_reverse()

    def display(self):
        self.linked_list.display()

if __name__ == "__main__":
    menu = Menu()
    menu.run_menu()
