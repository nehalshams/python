
# class method, instance method, static method

class Example:
    class_variable = "I am a class variable"
    
    def __init__(self, value):
        self.instance_variable = value

    # Instance method: Can access `self`
    def instance_method(self):
        print(f"Instance variable: {self.instance_variable}")
        print(f"Class variable from instance method: {Example.class_variable}")
    
    # Class method: Can access `cls`
    @classmethod
    def class_method(cls):
        print(f"Class variable from class method: {cls.class_variable}")
    
    # Static method: No access to `self` or `cls`
    @staticmethod
    def static_method():
        print("This is a static method")

# Creating an object
obj = Example("I am an instance variable")

# Calling instance method
obj.instance_method()  # Accesses both instance and class data

# Calling class method
Example.class_method()  # Accesses class data only

# Calling static method
Example.static_method()  # Does not access any instance or class data




#----------------------------- 1. Accessing Class Variables in Instance Methods ------------------------------
class Car:
    wheels = 4  # Class variable

    def __init__(self, brand):
        self.brand = brand  # Instance variable

    def instance_method(self):
        # Accessing class variable using the class name
        print(f"Class variable (wheels) via class name: {Car.wheels}")
        
        # Accessing class variable using self (though it's instance-specific, it can still access class-level data)
        print(f"Class variable (wheels) via self: {self.wheels}")
        
        # Accessing instance variable
        print(f"Instance variable (brand): {self.brand}")

# Creating an object
my_car = Car("Toyota")

# Accessing the class variable through an instance method
my_car.instance_method()

#--------------------------- 2. Accessing Class Variables in Static Methods ---------------------------

class Car:
    wheels = 4  # Class variable

    def __init__(self, brand):
        self.brand = brand  # Instance variable

    @staticmethod
    def static_method():
        # Accessing class variable using the class name
        print(f"Class variable (wheels) via class name: {Car.wheels}")

# Calling the static method
Car.static_method()


