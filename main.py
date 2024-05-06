class Person:
  counter = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.counter += 1

  def greet(self):
    return f"Hi, It's {self.name}"

  @classmethod
  def create_anonymous(cls):
    return Person("Anonymous", 22)

class Empolyee(Person):
  def __init__(self, name, age, job_title):
    super().__init__(name, age)
    self.job_title = job_title

  def greet(self):
    return super().greet() + f"I'm a {self.job_title}"

if __name__ == "__main__":
  # Define a class

  # person = Person()
  # print(type(person))

  # Define instance attributes

  # person.name = "John"
  # print(person.name)

  # person = Person("John", 25)
  # print(person.name)
  # print(person.age)

  # Define instance methods

  # person = Person("John", 25)
  # print(person.greet())

  # Define class attributes

  # print(Person.counter)

  # person = Person("John", 25)
  # print(Person.counter)
  # print(person.counter)

  # Define class method

  # anonymous = Person.create_anonymous()
  # print(anonymous.name)

  # Define static method

  # class TemperatureConverter:
  #   @staticmethod
  #   def celsius_to_fahrenheit(celsius):
  #     return 32 + celsius * 1.8

  #   @staticmethod
  #   def fahrenheit_to_celsius(fahrenheit):
  #     return (fahrenheit - 32) / 1.8

  # print(TemperatureConverter.celsius_to_fahrenheit(30))

  # Single inheritance

  empolyee = Empolyee("John", 25, "Python Developer")
  print(empolyee.greet())
