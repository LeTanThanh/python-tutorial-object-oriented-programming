class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

if __name__ == "__main__":
  # Define a class

  # person = Person()
  # print(type(person))

  # Define instance attributes

  # person.name = "John"
  # print(person.name)

  person = Person("John", 25)
  print(person.name)
  print(person.age)
