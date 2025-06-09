from linked_list.linked_list import LinkedList

def run():
    ll = LinkedList()
    print("\nWelcome to LinkedList CLI System\n")

    while True:
        print("\nOptions:\n1. Add Node\n2. Delete Node at Position\n3. Print List\n4. Exit")
        choice = input("Select option (1-4): ").strip()

        if choice == '1':
            value = input("Enter value to append: ").strip()
            print(ll.append(value))
        elif choice == '2':
            try:
                index = int(input("Enter position to delete (1-based): "))
                print(ll.delete_nth_node(index))
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '3':
            print("List:", ll.display())
        elif choice == '4':
            print("B'bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()
