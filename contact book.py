contact={}
def display_contact():
    print("Name \t\t contact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True :
    choice=int(input("Enter your choice "))
    if choice==1:
         name= input("Enter the name")
         phone=input("Enter the phone number")
         contact[name]=phone
    elif choice==2:
        search_name= input("Enter search name")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print(search_name," is not founded")
    elif choice==3:
        if not contact:
            print("Empty contact name")
        else:
            display_contact()

    elif choice==4:
        edit_contact=input("Enter the contact to be edited")
        if edit_contact in contact:
            phone= input("Enter phone number")
            contact[edit_contact]=phone
            print("contact upload")
            display_contact()
        else:
            print("Name is not found in contact book")

    elif choice==5:
        del_contact= input("Enter delete contact number")
        if del_contact in contact:
            confirm= input("Do you want to delete this contact yes/no")
            if confirm=='Y' or confirm=='y':
                contact.pop(del_contact)
            display_contact()

        else:
            print("Name is not found in contact book")

    else:
        break
