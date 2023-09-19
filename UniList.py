my_list = []

while True:
    print("\nChoose an operation:")
    print("1. Insert at Start")
    print("2. Insert at Random")
    print("3. Insert at End")
    print("4. Display")
    print("5. Exit")

    choice = input("\nEnter Your Choice: ")
    
    if choice == "1":
        print("\nInsert at start")
        item = input("Enter the Item: ")
        my_list.insert(0,item)
        print(my_list)
    elif choice == "2":
        print("\nInsert at random")
        item = input("Enter the Item: ")
        position = int(input("Enter the position: "))
        my_list.insert(position -1, item)
        print(f"{item} is Inserted at {position}")
        print(my_list)
    elif choice == "3":
        while True:
            print("\n 1 Insert Single Item")
            print("\n 2 Insert Multiple Items")
            print("\n 3 Exit")
            third = input("Enter Your Choice: ")
            if third == "1":
                print("\n Signle Item")
                item = input("Enter the Item: ")
                my_list.append(item)
                print(my_list)
            elif third == "2":
                print("\n Multiple Items ")
                item = input("Enter the Multiple Items")
                items_list = item.split(",")
                my_list.extend(items_list)
                print(my_list)
            elif third == "3":
                break
    elif choice == "4":
        print("\nDisplaying the list:")
        for item in my_list:
            print(item)
    elif choice == "5":
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please enter a valid option.")
