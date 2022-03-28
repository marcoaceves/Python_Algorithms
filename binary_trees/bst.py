class Node:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

#   add Node
    def add_node(self, data):
        monkey = self.root
        new_node= Node(data)
        while(monkey):
            if(data > monkey.data):
                if(monkey.right):
                    monkey=monkey.right
                else:
                    monkey.right = new_node
                    return self
            else:
                if(monkey.left):
                    monkey=monkey.left
                else:
                    monkey.left=new_node
                    return self

        return self

    # search node
    def search_for_node(self,data):
        monkey = self.root
        while(monkey):
            if data > monkey.data:
                monkey = monkey.right
            elif data < monkey.data:
                monkey = monkey.left
            else:
                return monkey.data, "i found the node"
        return "Node Not Found"
    # max
    def max_node(self):

        runner=self.root
        maxi=self.root.data

        if(self.root == None):
            print("List is empty");
        else:
            while(runner):
                if maxi < runner.data :
                    maxi = runner.data
                runner= runner.right
                if(runner == self.root):
                    break
        return("Maximum value node in the list:", maxi )
    # max
    def min_node(self):

        runner=self.root
        mini=self.root.data

        if(self.root == None):
            print("List is empty");
        else:
            while(runner):
                if mini > runner.data :
                    mini = runner.data
                runner= runner.left
                if(runner == self.root):
                    break
        return("Minimum value node in the list:", mini )


new_bst = BST(Node(10))
print(new_bst, 'This is the BST object')
print(new_bst.root, 'This is the root node object')
print(new_bst.root.data, 'This is the value my root node contains')
new_bst.add_node(11).add_node(22).add_node(2).add_node(7).add_node(4)
print(new_bst.root.right.data, 'this is the value we just added')
print(new_bst.root.left.data)
print(new_bst.search_for_node(22))
print(new_bst.max_node())
print(new_bst.min_node())