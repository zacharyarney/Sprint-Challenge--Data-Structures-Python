class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# set up storage as an array
# DFS uses a stack
# append first item of BST
# while storage[0]
# cb(self.value)
# pop self from storage
# if self.left append self.left to storage
# if self.right append self.right to storage
    def depth_first_for_each(self, cb):
        storage = []
        storage.append(self)
        while len(storage):
            cur = storage.pop()
            cb(cur.value)
            if cur.right:
                storage.append(cur.right)
            if cur.left:
                storage.append(cur.left)

    # same as depth first except we pop from the front to make storage a queue
    # instead of a stack
    def breadth_first_for_each(self, cb):
        storage = []
        storage.append(self)
        while len(storage):
            cur = storage.pop(0)  # pop from the front
            cb(cur.value)
            if cur.left:
                storage.append(cur.left)
            if cur.right:
                storage.append(cur.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
