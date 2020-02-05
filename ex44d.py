class Parent(object):
    def introduce(self, name):
        return f"Hello, I'm {name}"

class Child(Parent):
    def introduce(self, name):
        parent_name = "Jane Doe"
        parent_intro = super(Child, self).introduce(parent_name)
        print(parent_intro)
        print(f"Hi, there my name is {name}")

dad = Parent()
son = Child()

print(dad.introduce("John Doe"))

son.introduce("Jane J")
