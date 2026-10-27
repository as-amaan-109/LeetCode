/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution:
        def addTwoNumbers(self, l1, l2):
        # Create a dummy node to simplify logic
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Get values (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Add the values and carry
            total = val1 + val2 + carry
            
            # Get the digit and new carry
            digit = total % 10
            carry = total // 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result (skip dummy node)
        return dummy_head.next