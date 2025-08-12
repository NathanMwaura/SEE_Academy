# 1. Create an empty list called my_list
my_list = []
print(f"1. Created empty list: {my_list}")

# 2. Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"2. After appending 10, 20, 30, 40: {my_list}")

# 3. Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position
print(f"3. After inserting 15 at second position: {my_list}")

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"4. After extending with [50, 60, 70]: {my_list}")

# 5. Remove the last element from my_list
my_list.pop()  # or my_list.pop(-1)
print(f"5. After removing last element: {my_list}")

# 6. Sort my_list in ascending order
my_list.sort()
print(f"6. After sorting in ascending order: {my_list}")

# 7. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"7. Index of value 30: {index_of_30}")

print(f"\nFinal list: {my_list}")