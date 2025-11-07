print("welcome to phonebook")
choice=input("enter 1 for new conact\n enter 2 for search contact\n enter 3 for update contact\n enter 4 for delete contact\n enter valid input:")

def create_contact():
    name=input("enter value:")
    email=input("enter email:")
    contact_no=input("enter contact_no:")
    file=open("sample.txt","a")
    file.write(contact_entry)
    file.close()


def search_contact():
    file=open("sample.txt","r")
    master_data=file.read()
    file.close()
    #print(master_data)
    search_term = input("enter search team:")
            

def update_contact():
    pass

def delete_contact():
    pass


if choice== "1":
    create_contact()
elif choice== "2":
    search_contact()
elif choice== "3":
    update_contact()
elif choice== "4":
    delete_contact()
else:
    print("invalid_contact")




