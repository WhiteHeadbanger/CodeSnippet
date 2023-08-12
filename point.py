class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    


class Person:

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def get_name(self):
        return self.name
    
    def get_lastname(self):
        return self.lastname
    
    def get_age(self):
        return self.age