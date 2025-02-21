class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Insert the item at the front of the stack
        self.stack.insert(0, item)
        print(f"{item} pushed to stack")

    def pop(self):
        # Remove the item from the front of the stack
        if not self.is_empty():
            item = self.stack.pop(0)
            print(f"{item} popped from stack")
        else:
            print("Stack is empty")

    def display(self):
        # Display the stack
        if not self.is_empty():
            print("Stack elements:", self.stack)
        else:
            print("Stack is empty")

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

def main():
    stack = Stack()
    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
