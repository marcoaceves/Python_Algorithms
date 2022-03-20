class Node():
    def __init__ (self, value):
        self. value = value
        self.next = None

class SLL():
    def __init__(self, head):
        self.head = head


    # add to front
    def add_front(self, value):
        temp= self.head
        self.head = Node(value)
        self.head.next = temp
        return self

    # display your list
    def display(self):
        runner = self.head
        count=1
        while(runner):
            print(f'This is your {count} node, it contains value {runner.value}')
            count += 1
            runner = runner.next
        return self

    # retunr value of front
    def front_value(self):

        print(self.head.value)

    # delete front
    def delete_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp=None



new_sll = SLL(Node(1))
new_sll.add_front(2).add_front(4).add_front(22).add_front(43).add_front(7)
new_sll.display()
new_sll.front_value()
new_sll.delete_front()
new_sll.display()

