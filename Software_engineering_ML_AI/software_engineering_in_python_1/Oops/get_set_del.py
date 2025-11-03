'''
class Animal:
  def __init__(self, name):
    self._name = name
    self._age = None

  def get_age(self):
    return self._age

  def set_age(self, new_age):
    if isinstance(new_age, int):
      self._age = new_age
    else:
      raise TypeError

  def delete_age(self):
    del self._age
    print("_age Deleted")

a = Animal("Rufus")
print(a.get_age()) # None

a.set_age(10)
print(a.get_age()) # 10

a.set_age("Ten") # Raises a TypeError

a.delete_age() # "_age Deleted"
print(a.get_age()) # Raises a AttributeError

'''

class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  def get_name(self):
    return self._name

  def set_name(self, new_name):
    self._name = new_name

  def del_name(self):
    del self._name

e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())

