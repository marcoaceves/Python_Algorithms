from hashlib import new


class Node():
    def __init__ (self, value):
        self.value = value
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
        list1=[]
        while(runner):
            # print(f'This is your {count} node, it contains value {runner.value}')
            list1.append(runner.value)
            count += 1
            runner = runner.next
        print(list1)

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

    # if contains value delete
    def contains_delete(self, val):

        runner = self.head
        while(runner):
            if runner.next:
                if runner.next.value == val:
                    temp = runner.next
                    runner.next = temp.next
            runner = runner.next
        return self

    # move min to front
    def min_to_front(self):
        runner = self.head
        count=0
        temp = runner.value
        while(runner):
            if runner.next:
                if temp > runner.next.value :
                    count+=1
                    temp=runner.next.value
                    print('temp',temp)
                else:
                    count+=1
            runner = runner.next
        print(temp, 'is your lowest value')
        self.contains_delete(temp)
        self.add_front(temp)

        print('')

    def max_to_back(self):
        runner = self.head
        max1= runner.value
        while(runner):
            if  (max1 < runner.value):
                max1 = runner.value


            runner = runner.next
        self.contains_delete(max1)
        self.push_back(max1)
        print(max1,'is max value')

    def push_back(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode


new_sll = SLL(Node(2))
new_sll.add_front(1).add_front(4).add_front(22).add_front(43).add_front(7)
# new_sll.display()
# new_sll.front_value()
# new_sll.delete_front()
new_sll.display()
# new_sll.contains(7)
# new_sll.number_of_nodes()
new_sll.min_to_front()
new_sll.display()
new_sll.max_to_back()

new_sll.display()


