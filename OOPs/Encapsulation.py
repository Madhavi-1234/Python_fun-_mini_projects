class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def update_marks(self):
        new_marks = int(input("Enter your new marks: "))

        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")
