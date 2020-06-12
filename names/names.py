import time


# Implementing Binary Search Tree from LEcture/Projects to traverse names
class BSTNode:
     def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None

     # insert value into the tree
     def insert(self, value):
         # if value is < the node value
         if value < self.value:
             # if left = None
             if not self.left:
                 # create new left node
                 self.left = BSTNode(value)
             else:
                 # insert value on left
                 self.left.insert(value)
         else:  # the value is greater than or equal to nodes value
             # if right node is None
             if not self.right:
                 # create the new right node
                 self.right = BSTNode(value)
             else:
                 # insert the value on the right
                 self.right.insert(value)

     # true if tree contains value
     # false if it does not
     def contains(self, target):
         # at start of search self will be the root
         # compare the target against self
         if self.value == target:
             return True
         if target < self.value:
             if not self.left:
                 return False

             return self.left.contains(target)
         else:
             if not self.right:
                 return False

             return self.right.contains(target)

     # return max value found in tree
     def get_max(self):
         # check right side 
         if self.right:
             # if there is a right node, repeat function
             return self.right.get_max()
         else:
             # if right node = none, max value has been found
             return self.value

     def iterative_get_max(self):
         current_max = self.value

         current = self
         # traverse structure
         while current:
             if current.value > current_max:
                 current_max = current.value
             # update our current_max variable if a larger value exists 
             current = current.right
         return current_max

     # Call the function `fn` on the value of each node
     # recursive depth-first traversal
     def for_each(self, fn):
         fn(self.value)
         # if there is a left node
         if self.left:
             # call for_each
             self.left.for_each(fn)
         # if there is a right node
         if self.right:
             # call for_each
             self.right.for_each(fn)

     # iterative depth-first traversal
     def iterative_for_each(self, fn):
         stack = []
         # add the root node
         stack.append(self)
         # loop so long as the stack still has elements
         while len(stack) > 0:
             current = stack.pop()
             if current.right:
                 stack.append(current.right)
             if current.left:
                 stack.append(current.left)
             fn(current.value)







start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# DELETED 

tree = BSTNode(names_1[0])
 # drop first element so it doesn't add another duplicate
names_1_drop_first = [name for name in names_1[1:]]

 # insert values from drop first array to tree
for name in names_1_drop_first:
     tree.insert(name)

 # if the tree contains any duplicates from the names_1 array
 # add it to duplicates array 
for name in names_2:
     if tree.contains(name):
         duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")







# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
