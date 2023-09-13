List = []

while True:
    print("\nChoose an operation:")
    print("1. Insert")
    print("2. Delete")
    print("3. Find / Indexing")
    print("4. Count")
    print("5. Update")
    print("6. Display")
    print("7. Exit")

    choice = input("\n Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to insert: ")
        position = int(input("Enter the position to insert: "))
        List.insert(position, item)
        print(f"{item} is insterted at index {position}")

    elif choice == "2":
        item = input("Enter the item to delete: ")
        if item in List:
            List.remove(item)
            print(f"{item} is Deleted")
        else:
            print(f"{item} is not found in the list")
        
    elif choice == "3":
        search_item = input("Enter the item to find: ")
        find_index = [i for i, item in enumerate(List) if item == search_item]
        if find_index:
            print(f"Item '{search_item}' found at index: {find_index}")
        else:
            print(f"{search_item} not found in the list")

    elif choice == "4":
        count = len(List)
        print(f"Number of items in the list: {count}")

    elif choice == "5":
        position = int(input("Enter the index to update: "))
        if 0 <= position < len(List):
            new_item = input("Enter the new item: ")
            List[position] = new_item
        else:
            print("Invalid index")

    elif choice == "6":
        print(List)

    elif choice == "7":
        break
    
    else:
        print("Invalid choice. Please choose a valid operation.")
