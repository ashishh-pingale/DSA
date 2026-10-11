class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


head = [1, 2, 3, 4, 5]


dummy = ListNode()
curr = dummy

for val in head:
    curr.next = ListNode(val)
    curr = curr.next

head = dummy.next


s1 = Solution()
result = s1.reverseList(head)


output = []
while result:
    output.append(result.val)
    result = result.next

print(output)