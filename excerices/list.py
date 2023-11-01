class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

head = Node(0)

def append(value):
    global head
    to_insert = Node(value)
    if head.next_node == None:
        head = to_insert
    else:
        temp = to_insert
        to_insert.next_node = head
        head = temp

def print_list():
    global head
    current = head
    while current != None:
        print(current.value)
        current = current.next_node


append(5)
append(3)
print(head.next_node)


