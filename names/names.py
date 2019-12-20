import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# 1.3 sec
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# 1.3sec
# [duplicates.append(x) for x in names_1 if x in names_2]

# 0.005 sec sets are not allowed
# duplicates = set(names_1).intersection(names_2)

# 0.007 sec
# duplicates = set(names_1) & set(names_2)

tree = BinarySearchTree(names_1[0])
for x in range(0, len(names_1)):
    val = tree.insert(names_1[x])
    val2 = tree.insert(names_2[x])
    if val:
        duplicates.append(val)
    if val2:
        duplicates.append(val2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
