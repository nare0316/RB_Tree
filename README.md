🔴 ⚫️ Red-Black Tree (RB-Tree) Implementation in Python

📎 Key Features:
- Insert: Adds a new node to the tree while ensuring it remains balanced.

- Delete: Removes a node from the tree while maintaining balance.

- Traversal: Displays the current structure of the tree with the node's value and color.
- Self-balancing: Automatically balances the tree through rotations and color changes during insertion and deletion.

📎 How it Works
The **Red-Black Tree** guarantees that the tree is balanced by enforcing the following properties:
1. Each node is either RED or BLACK.
2. The root is always BLACK.
3. All leaves (NIL nodes) are BLACK.
4. A red node cannot have a red child (i.e., no two red nodes can be adjacent).
5. Every path from a node to its descendant NIL nodes must have the same number of black nodes.

📎 The tree ensures efficient search, insert, and delete operations, each with an average and worst-case time complexity of O(log n).

📎 Classes
    `TreeNode`
Represents a node in the tree. Each node contains:
- `val`: The value of the node.
- `color`: The color of the node, either "RED" or "BLACK".
- `left`: Reference to the left child.
- `right`: Reference to the right child.
- `parent`: Reference to the parent node.


📎 Methods:
1. insert(val): Inserts a new value into the tree and fixes any violations of Red-Black Tree properties.

2. delete(val): Deletes a node with the specified value from the tree, balancing the tree afterward.

3. print(): Prints the tree structure in a level-order format (using a queue), showing the value and color of each node.

4. __leftRotate(x), __rightRotate(x): Private methods that perform left and right rotations, respectively, to maintain the tree's balance.

5. __insertFixup(z): Private method that fixes any violations after inserting a node.

6. __deleteFixup(x): Private method that fixes any violations after deleting a node.

7. __getMinimum(node): Private method that returns the minimum node in a subtree.
