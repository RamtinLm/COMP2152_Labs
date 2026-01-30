cart = ["apple", "Banana", "Milk", "Bread", "apple", "Eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
milk_position = cart.index("milk")
print(f"Position Of Milk: {milk_position}")
cart.remove("apple") #using remove
removed_item = cart.pop()
print (f"Removed Item Using Pop: {removed_item}")
print(f"Is Banana In Cart?", "Banana" in cart)