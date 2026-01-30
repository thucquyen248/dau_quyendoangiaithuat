class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def cong_hai_danh_sach(l1, l2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.value if l1 else 0
        v2 = l2.value if l2 else 0
        total = v1 + v2 + carry

        carry = total // 10
        current.next = Node(total % 10)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next
l1 = Node(2, Node(4, Node(3))) 
l2 = Node(5, Node(6, Node(4))) 

result = cong_hai_danh_sach(l1, l2)
output = []
while result:
    output.append(result.value)
    result = result.next

print(output)  