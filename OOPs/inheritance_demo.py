class user:
  def __init__(self):
    print("inherit this class")

  def login(self):
      print("login")

  def register(self):
      print("register")


class student(user):
    def enroll(self):
      print("enroll")

    def profile(self):
      print("profile")

s1= student()
s1.login()
