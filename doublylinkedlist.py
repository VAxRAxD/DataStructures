class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        
    def size(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
        
    def insert_at_begining(self,data):
        node=Node(data,None,self.head)
        if self.head is not None:
            self.head.prev=node
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,itr,None)
        
    def remove_at(self,index):
        if index<0 and index>self.size():
            return Exception("Invalid")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                itr.next.prev=itr
                break
            itr=itr.next
            count+=1
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        ll=""
        rev=[]
        itr=self.head
        while itr:
            elem=itr
            ll+=str(itr.data)+"-->" if itr.next else str(itr.data)
            itr=itr.next
        itr=elem
        while itr:
            rev.append("<--"+str(itr.data) if itr.prev else str(itr.data))
            itr=itr.prev
        rev.reverse()
        print(ll)
        print(''.join(elem for elem in rev))
        
    def previous(self,data):
        if self.head is None:
             return "Linked List is empty"
        itr=self.head
        while itr.data!=data:
            itr=itr.next
        print(itr.prev.data) if itr.prev is not None else print("Null")