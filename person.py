class Person:
  counter = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.counter += 1

  def greet(self):
    return f"Hi, It's {self.name}."

  @classmethod
  def create_anonymous(cls):
    return Person("Anonymous", 22)