# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Generates a linked list        
def generate_linked_list():
    elements = [1,2,3,4,5]
    head = None
    for values in elements:
        head = add_element_at_front(head, values)
    print_linked_list(head)
    return head
    
# Print linked list
def print_linked_list(head):
    curr_node = head
    linked_list_values = []
    
    while curr_node != None:
        linked_list_values.append(curr_node.val)
        curr_node = curr_node.next
    
    print(" linked List -", linked_list_values)

def add_element_at_front(head, val):
    new_node = ListNode(val)
    new_node.next = head
    head = new_node
    return new_node
    
def add_element_at_end(head, val):
    dummy_node = ListNode(-1)
    new_node = ListNode(val)
    
    dummy_node.next = head
    curr_node =  dummy_node
    
    while curr_node.next != None:
        curr_node = curr_node.next
    
    curr_node.next = new_node
    return dummy_node.next
    
def add_element_after_node(head, node_val, val):
    dummy_node = ListNode(-1)
    dummy_node.next = head
    
    new_node = ListNode(val)
    curr_node = dummy_node
    
    while curr_node.val != node_val:
        curr_node = curr_node.next
    
    temp = curr_node.next
    curr_node.next = new_node
    new_node.next = temp
    
    return dummy_node.next

def add_element_before_node(head, node_val, val):
    dummy_node = ListNode(-1)
    dummy_node.next = head
    
    new_node = ListNode(val)
    curr_node = dummy_node
    
    while curr_node.next.val != node_val:
        curr_node = curr_node.next
    
    temp = curr_node.next
    curr_node.next = new_node
    new_node.next = temp
    
    return dummy_node.next

def delete_element_at_front(head):
    if head == None:
        return None
    head = head.next
    return head

def delete_element_at_end(head):
    dummy_node = ListNode(-1)
    dummy_node.next = head
    
    prev_node = dummy_node
    curr_node = dummy_node
    
    while curr_node.next != None:
        prev_node = curr_node
        curr_node = curr_node.next
    
    prev_node.next = None
    return dummy_node.next
    
def delete_element_at_middle(head, node_val):
    dummy_node = ListNode(-1)
    dummy_node.next = head
    curr_node = dummy_node
    prev_node = None
    
    while curr_node.val != node_val:
        prev_node = curr_node
        curr_node = curr_node.next
    
    temp = curr_node.next
    prev_node.next = temp
    
    return dummy_node.next
    
head = generate_linked_list()

print("\n Add element at Front")
head = add_element_at_front(head, 100)
print_linked_list(head)

print("\n Add element at End")
head = add_element_at_end(head, 100)
print_linked_list(head)

print("\n Add element after node")
head = add_element_after_node(head, 2, 20)
print_linked_list(head)

print("\n  Add element before node")
head = add_element_before_node(head, 2, 20)
print_linked_list(head)

print("\n Delete element at front")
head = delete_element_at_front(head)
print_linked_list(head)

print("\n Delete element at end")
head = delete_element_at_end(head)
print_linked_list(head)

print("\n Delete element ")
head = delete_element_at_middle(head, 20)
print_linked_list(head)
