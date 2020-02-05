class Parent(object):
    def altered(self):
        print("PARENT override()")

class Child(Parent):
    def altered(self):
        print("CHILD, Befor PARENT altered()")
        super(Child, self).altered()
        print("CHILD, After PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
