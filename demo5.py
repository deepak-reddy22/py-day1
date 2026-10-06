print("Demo of different types of loops in Python")

print("1) Loop through a range:")
for item in range(1, 6):
	print(item)

print("\n2) Loop through a list:")
fruits = ["apple", "banana", "cherry"]
for item in fruits:
	print(item)

print("\n3) Loop through a string:")
word = "Python"
for item in word:
	print(item)

print("\n4) Nested loop:")
for row in range(1, 4):
	for col in range(1, 4):
		print(f"({row}, {col})", end=" ")
	print()
