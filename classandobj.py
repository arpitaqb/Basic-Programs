class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def show(self):
        print(f"My name is {self.name} and my age is {self.age}")

obj = person("Arpita", 20)
obj.show()
