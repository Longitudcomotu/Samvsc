import csv

def load_contacts(filename):
    contacts = {}
    with open(filename,"r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            first_name = row[0]
            lastname = row[1]
            phonenumber = row[2]
            email = row[3]
            
            contacts[lastname] = [first_name,phonenumber,email]
    return contacts

def display_contact_info(contact_info):
    if contact_info:
        print("\nContact Information: ")
        print(f"first name: {contact_info[0]}")
        print(f"Phone number: {contact_info[1]}")
        print(f"email: {contact_info[2]}")
    else:
        print("No contact Information found for this last name")
 
def main():
    filename ="csv.csv"

    contacts = load_contacts(filename)
    
    lastname = input("please enter a last name to look up: ").strip()
    contact_info = contacts.get(lastname)
    display_contact_info(contact_info)    
    
main()