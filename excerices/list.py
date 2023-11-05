class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        print("[" , end="", sep="")
        print(current_node.value, ", ", end="", sep="")

        while current_node.next_node != None:
            current_node = current_node.next_node
            if current_node.next_node != None:
                print(current_node.value, ", ", end="", sep="")
            else:
                print(current_node.value, end="", sep="")

        print("]" , end="", sep="")

    def append(self, value):
        new_node = Node(value)
        current_node = self.head
    
        if self.head == None:
            self.head = new_node
            return

        while current_node.next_node != None:
            current_node = current_node.next_node
        
        current_node.next_node = new_node
    
    def append_at(self, value, index):
        new_node = Node(value)
        current_node = self.head

        if index == 0:
            whole_list = self.head
            self.head = new_node
            new_node.next_node = whole_list

        for _ in range(index - 1):
            current_node = current_node.next_node

        #print("index_to_replace: ", current_node.value)
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete(self, value):
        current_node = self.head

        while current_node.next_node != None:
            if current_node.next_node.value == value:
                break
            current_node = current_node.next_node

        current_node.next_node = current_node.next_node.next_node



list = LinkedList()
list.append(5)
list.append(10)
list.append(15)
list.append(20)
list.append(25)

list.append_at(4, 3)

list.delete(15)

list.print_list()