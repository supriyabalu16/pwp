numbers={"one","two","three","four","five","six"}
print("\nprint the original set")
print(numbers)
print("\nadding other numbers to the set")
numbers.discard("seven")
print("\nprint the modified set")
print(numbers)
print("looping through the set elements...")
for i in numbers:
	print(i)