class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def solve(self, A, B):
        head=A
        while(head.next):
            A.val=self.fun(A.val,B)
            head=head.next
    def fun(self,a,b):
        l=[]
        for i in range(a+1):
            if(i%b == 0):
                l.append(i)
            
        return max(l)
    def insert_at_beginning(self,val):
        n=Node(val)
        n.next=self.head
        self.head=n

    def insert_at_end(self,val):
        n=Node(val)
        if self.head is None:
            self.head=n
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=n

    def insert_at_k(self,k,val):
        n=Node(val)
        if k==0:
            self.insert_at_beginning(val)
            return
        count=0
        last=self.head
        while last:
            if(count == k-1):
                n.next=last.next
                last.next=n
                break
            last=last.next
            count+=1
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.val,"->",end=" ")
            printval = printval.next
        print("NULL")
    def length(self):
        count=0
        last=self.head
        while last:
            last=last.next
            count+=1
        return count
    def delete_at_end(self):
        last=self.head
        while last.next.next:
            last=last.next
        last.next=None
    def delete_at_beginning(self):
        self.head=self.head.next

    def delete_at_k(self,k):
        count=0
        itr=self.head
        while itr.next:
            if(count == k-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

linked_list=LinkedList()
linked_list.head=Node(1)
n2=Node(2)
linked_list.head.next=n2
n3=Node(3)
n2.next=n3
linked_list.insert_at_end(4)
linked_list.insert_at_k(0,0)
linked_list.insert_at_k(2,1.5)
linked_list.delete_at_end()
linked_list.delete_at_beginning()
linked_list.delete_at_k(1)
linked_list.listprint()
print(linked_list.length())