def reorderList(head):
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        prev=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        first,second=head,prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2