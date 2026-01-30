contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(f"Alice's number: {contacts['Alice']}")
contacts["Diana"] = "555-4321"
print(f"COntacts after adding Diana: {contacts}")
contacts["Bob"] = "555-0000"
print (f"contacts after updating Bob: {contacts}")
del contacts["Charlie"]
print(f"contacts after deleting Charlie: {contacts}")
print(f"All names {contacts.keys()}")
print(f"all numbers {contacts.values()}")
print(f"total contact: {len(contacts)}")