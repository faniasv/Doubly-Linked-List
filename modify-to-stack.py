class Node:

   def _init_(self, data):
       self.data = data
       self.next = None
       self.prev = None        
         

class Stack:
 
   def _init_(self):
       self.head = None
         

   def push(self, data):
 
       if self.head is None:
           self.head = Node(data)
       else:
           newNode = Node(data)
           self.head.prev = newNode
           newNode.next = self.head
           newNode.prev = None
           self.head = newNode
             

   def pop(self):
 
       if self.head is None:
           return None
       elif self.head.next is None:
           temp = self.head.data
           self.head = None
           return temp
       else:
           temp = self.head.data
           self.head = self.head.next
           self.head.prev = None
           return temp
 

   def top(self):

       return self.head.data
 

   def size(self):
 
       temp = self.head
       count = 0
       while temp is not None:
           count = count + 1
           temp = temp.next
       return count

   def isEmpty(self):
 
       if self.head is None:
          return True
       else:
          return False
             

   def printStack(self):
         
       print("The elements in the stack are:")
       temp = self.head
       while temp is not None:
           print(temp.data, end ="->")
           temp = temp.next          
         

if _name=='_main_':
 

 stack = Stack()
 

 print("Stack operations using Doubly LinkedList")
 stack.push(10)
 stack.push(5)
 stack.push(7)
 stack.push(3)
 stack.printStack()
 
 print("\nTop element is ", stack.top())
 
 print("Size of the stack is ", stack.size())
 
 stack.pop()
 stack.pop()
   
 stack.printStack()

 print("\nStack is empty:", stack.isEmpty())