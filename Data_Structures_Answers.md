Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
O(n) as implied by "for each".

2. What is the space complexity of your `depth_first_for_each` function?
 Seems like it would be O(log n) because the storage array fills up with the children of half the children if that makes sense. The array would never contain more than half of the tree.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
O(n^2) because of the nested for loop.

6. What is the space complexity of the provided code in `names.py`?
O(n) because it stores an array of both lists of names

7. What is the runtime complexity of your optimized code in `names.py`?
I think it's going to be O(n log n). O(n) to loop through the arrays multiplied by O(log n) to search the BST.

8. What is the space complexity of your optimized code in `names.py`?
I guess it would still be O(n) but there is also the BST added to storage, so there would be a multiplier to the n potentially.
