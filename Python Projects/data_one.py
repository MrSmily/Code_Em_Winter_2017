#Data1
contact = ('first_name', 'last_name', 'mobile_phone', 'home_phone', 'zip_code')

def create_contact(first_name, last_name, mobile_phone, home_phone=None, zip_code=None):
    return(first_name, last_name, mobile_phone, home_phone, zip_code)

contacts = []
contacts.append(create_contact("Mom", "Chalfant1", "804-530-2770"))
contacts.append(create_contact("Dad", "Chalfant2", "804-540-2770", "804-550-2770"))
contacts.append(create_contact("sister", "Chalfant3", "804-540-2770", "804-550-2770", "64738"))

print
print ("Contacts in the list")
print (contacts)
print ("\n\n\n")

#def find_contact_by_first_name(first_name):
 #   for contacts in contacts:
  #      if contact[0] == first_name:
   #         return contact

#contact = find_contact_by_first_name("Mom")

#print
#print ("Contact lookup of Mom using our custom finder")
#print (contact)

FIRST_NAME = 0
LAST_NAME = 1
MOBILE_PHONE = 2
HOME_PHONE = 3
ZIP_CODE = 4

def find_contact_by_first_name(first_name):
    for contact in contacts:
        if contact[FIRST_NAME] == first_name:
            return contact

contact = find_contact_by_first_name("Mom")

print
print ("Contact lookup of Mom using our improved custom finder.\n")
print (contact)
print ("\n\n\n")

def find_contact_by_last_name(last_name):
    for contact in contacts:
        if contact[LAST_NAME] == last_name:
            return contact

contact = find_contact_by_last_name("Chalfant2")

contacts_by_first_name = {}

for contact in contacts:
    contacts_by_first_name[contact[FIRST_NAME]] = contact

contact = contacts_by_first_name["Dad"]

print
print ("First Name lookup of 'Dad' using Python's dictionary key index syntax")
print (contact)

print
print ("Contact lookup of 'Chalfant2' using our find by last name.\n")
print (contact)
print ("\n") 

print("Give first name:")
first_name1 = input()

print("Give last name:")
last_name1 = input()

print("Give home phone number:")
home_phone1 = input()

print("Give mobile phone number:")
mobile_phone1 = input()

print("Give zip code:")
zip_code1 = input()

person1 = (first_name1, last_name1, home_phone1, mobile_phone1, zip_code1)

contacts.append(person1)

print(contacts)



































