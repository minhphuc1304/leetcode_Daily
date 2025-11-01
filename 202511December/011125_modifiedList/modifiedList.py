class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_remove = set(nums)
        vals = []
        curr = head
        while curr:
            if curr.val not in to_remove:
                vals.append(curr.val)
            curr = curr.next

        if not vals:
            return None

        curr = head
        prev = None
        for v in vals:
            curr.val = v
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
        return head
