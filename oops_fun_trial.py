class Person:
  def __init__(self,name):
    self.name= name

 class Bestfriend(Person):
   def __init__(self, name):
     super().__init__(name)
     self.memories=[]

  def add_memories(self,memory):
     self.memories.append(memory)

  def show_memories(self,date):
    for memory in self.memories:
      if memory_date= date:
      print(memory_message)

 class Memory:
   def __init__(self,date, message):
     self.date= date
     self.message= message
     
