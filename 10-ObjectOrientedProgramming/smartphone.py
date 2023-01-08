from contact import Contact
from contact_list import ContactList

contactList = ContactList()

contactList.add(Contact("John Brown", "brown@onet.pl", "555234000"))
contactList.add(Contact("Ann May", "am@o2.pl", "232000199"))
contactList.add(Contact("George Small", "smallg@google.pl", "222999100"))
contactList.add(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

contactList.display()