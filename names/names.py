import time

start_time = time.time()


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BinarySearchTree(value)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = new_node
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = new_node

    def contains(self, target):
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target == self.value:
            return True


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# ORIGINAL ALGORITHM ~ 12s
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# NEW ALGORITHM ~ 0.28s
bst = BinarySearchTree(names_1[0])
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
