# merge_menu.py
# merge_menu.py
from single_linked_list import Node, SinglyLinkedList
import sys

class ExtendedSinglyLinkedList(SinglyLinkedList):
    def merge_list(self, other_list, position):
        if position == 0:
            # Find the tail of other_list
            other_tail = other_list.head
            while other_tail and other_tail.next:
                other_tail = other_tail.next
            # Attach the current list to the tail of other_list
            other_tail.next = self.head
            self.head = other_list.head
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of bounds")
                current = current.next
            # Insert other_list at the specific position
            other_tail = other_list.head
            while other_tail and other_tail.next:
                other_tail = other_tail.next
            other_tail.next = current.next
            current.next = other_list.head

class MergeMenu:
    def get_menu(self, list1, list2):
        menu = {
            1: self.add_node_list1,
            2: self.add_node_list2,
            3: self.delete_node_list1,
            4: self.delete_node_list2,
            5: self.display_list1,
            6: self.display_list2,
            7: self.merge_lists,
            8: self.end_of_program
        }
        self.list1 = list1
        self.list2 = list2
        return menu

    def invalid_choice(self):
        print('Invalid choice entered')

    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        list1 = ExtendedSinglyLinkedList()
        list2 = ExtendedSinglyLinkedList()
        while True:
            choice = int(input('1: Add node to List1 2: Add node to List2 3: Delete node from List1 4: Delete node from List2 5: Display List1 6: Display List2 7: Merge List2 into List1 8: Exit. Your choice: '))
            menu = self.get_menu(list1, list2)
            menu.get(choice, self.invalid_choice)()

    def add_node_list1(self):
        data = int(input('Enter data for List1: '))
        position = int(input('Enter position for List1: '))
        try:
            self.list1.add_node(data, position)
        except IndexError as e:
            print(e)

    def add_node_list2(self):
        data = int(input('Enter data for List2: '))
        position = int(input('Enter position for List2: '))
        try:
            self.list2.add_node(data, position)
        except IndexError as e:
            print(e)

    def delete_node_list1(self):
        position = int(input('Enter position to delete from List1: '))
        try:
            self.list1.delete_node(position)
        except IndexError as e:
            print(e)

    def delete_node_list2(self):
        position = int(input('Enter position to delete from List2: '))
        try:
            self.list2.delete_node(position)
        except IndexError as e:
            print(e)

    def display_list1(self):
        print("List1: ", end='')
        self.list1.display()

    def display_list2(self):
        print("List2: ", end='')
        self.list2.display()

    def merge_lists(self):
        position = int(input('Enter position to merge List2 into List1: '))
        try:
            self.list1.merge_list(self.list2, position)
        except IndexError as e:
            print(e)

# Run the menu
merge_menu = MergeMenu()
merge_menu.run_menu()
