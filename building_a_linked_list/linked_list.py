from hashlib import new


class Node():
    def __init__ (self, value):
        self. value = value
        self.next = None

class SLL():
    def __init__(self, head):
        self.head = head

    # contains value
    def contains(self, val):
        runner = self.head
        while(runner):
            if runner.value == val:
                print(True)
            else:
                print(False)

            runner = runner.next
        return self

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

    # display number of nodes
    def number_of_nodes(self):
        runner = self.head
        count=0
        while(runner):
            count += 1
            runner = runner.next
        print(f'There are {count} nodes in this list')

    # retunr value of front
    def front_value(self):

        print(self.head.value, 'is heads value')

    # delete front
    def delete_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp=None



    # move min to front
    def min_to_front(self):
        runner = self.head
        temp= runner.value
        node=temp
        runner2 = runner.next
        count=0
        while(runner):
            if runner.value < runner2.value:
                count+=1
                temp=runner.value
                node=runner
                print(temp, 'is your new lowest value', ', node:',count)
            else:

                count+=1
                print(runner2.value, 'is NOT your lowest value', ', node:',count)
            runner = runner.next

        # while(runner):
        #     if runner.next == node:
        #         runner.value== runner.next
        # runner = runner.next
        new_sll.add_front(temp)

        print('')


new_sll = SLL(Node(1))
new_sll.add_front(2).add_front(4).add_front(22).add_front(43).add_front(7)
new_sll.display()
new_sll.front_value()
# new_sll.delete_front()
new_sll.display()
new_sll.contains(7)
new_sll.number_of_nodes()
new_sll.min_to_front()
new_sll.display()


