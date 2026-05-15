class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Tính độ dài danh sách
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Đưa k về phạm vi [0, length)
        k %= length
        if k == 0:
            return head

        # Nối tail với head để tạo vòng
        tail.next = head

        # Tìm điểm ngắt: đi (length - k) bước từ head
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head