class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LinkedListCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create a cycle: -4 points back to 2
node4.next = node2

# Pass head to the function
result = LinkedListCycle(node1)

if result:
    print("Cycle starts at node:", result.val)
else:
    print("No cycle")