contacts={} # contact module
def display_contacts():
    print("Here is your contacts:")
    for (name,mbl) in contacts.items():
          print(name,mbl,sep=":")
#print(contacts)
def add_contact(name,mbl):
    if name not in contacts:
        contacts[name]=mbl
        print("contact added..!")
    else:
        print(name,"already exist")
#add_contact(input("Name:"),int(input("Mobile Num:")))
def edit_contact(name): # new mbl
    if name in contacts:
        new=int(input("New mbl number:"))
        contacts[name]=new
        print("contact updated..!")
    else:
        print(name,"doesn't exist")
#edit_contact        
def search_contact(name):
    if name in contacts:
        print("Your contact\n")
        print(name,contacts[name],sep=":")
    else:
        print(name,"doesn't exist")
        
# search_contact()
def delete_contact(name):
    if name not in contacts:
        print(name,"doesn't exist")
    else:
        print(contacts.pop(name))