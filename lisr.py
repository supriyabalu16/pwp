list=[10,9,8,7,6]
print("printing orginal list")
for i in list:
	print(i,end=" ")
list.remove(4)
print("\nprinting the list after removal of first element")
for i in list:
	print(i,end=" ")