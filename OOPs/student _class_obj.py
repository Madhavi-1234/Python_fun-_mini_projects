class student:

  def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks

  def grade(self):
    if self.marks >= 90:
      return "A"
    elif self.marks >= 80:
      return "B"
    elif self.marks >= 70:
      return "C"
    elif self.marks >= 60:
      return "D"
    else:
      return "F"

student1= student("Alice", 101, 85)
student2= student("Bob", 102, 92)

print(f"{student1.name} got {student1.grade()} grade")
print(f"{student2.name} got {student2.grade()} grade")
