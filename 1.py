class Dog:
    #what do all dogs have
    allowed_outside = True
    is_good_boy = True
    
    #what do all dogs have (variable to the dog)
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.is_old = False

    # instance method
    def age_dog(self):
        self.age +=1
        return self.age
    # Methods that are only invoked on the class - not instances
    @classmethod
    def toggle_allowed(cls):
        cls.allowed_outside = not cls.allowed_outside

dog_1 = Dog(2, 40)
dog_1.age_dog()
print(f"age = {dog_1.age}, {dog_1.weight}")
Dog.toggle_allowed()
print(dog_1.allowed_outside)
Dog.toggle_allowed()
print(dog_1.allowed_outside)
