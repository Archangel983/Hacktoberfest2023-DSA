class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Classmate")
e2 = Node("LinkedIn")
e3 = Node("Launchpad")

list.headval.nextval = e2

e2.nextval = e3

list.listprint()
