monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday Classs: {wednesday_class}")
print(f"Attended both classes: {monday_class & wednesday_class}")
print(f"Attended either class: {monday_class | wednesday_class}")
print(f"Only monday: {monday_class - wednesday_class}")
print(f"Only one class: {monday_class ^ wednesday_class}")
allStudents = monday_class | wednesday_class
print("Is Monday subset of all student? ", monday_class <= allStudents)