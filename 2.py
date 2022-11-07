class Dog:
    allowed_outside = True
    is_good_boy = True
    
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.is_old = False

    def age_dog(self):#instance method
        self.age +=1
        return self.age

    @classmethod #class method
    def toggle_allowed(cls):
        cls.allowed_outside = not cls.allowed_outside

##          DELETE ALL OF THIS VVV 
##
dog_1 = Dog(2, 40)
dog_1.age_dog()
print(f"age = {dog_1.age}, {dog_1.weight}")
Dog.toggle_allowed()
print(dog_1.allowed_outside)
Dog.toggle_allowed()
print(dog_1.allowed_outside)

##
##         ADD EVERYTHING BELOW THIS LINE
##  __________________________________________

# ------ INHERITANCE  (is-a relationship)
class SmallDog(Dog):

    def __init__(self, age, weight, is_yappy):
        super().__init__(age, weight)
        self.is_yappy = is_yappy
        self.check_weight() #run on instantiation - new thing?
    
    def check_weight(self):
        if self.weight > 10:
            print("This is not a small dog!")

dog_2 = SmallDog(5, 22, False)
dog_3 = SmallDog(5, 8, False)

class LargeDog(Dog):

    def __init__(self, age, weight, leash_trained):
        super().__init__(age, weight)
        self.leash_trained = leash_trained
    
    def age_dog(self):
        self.age += 1
        if self.age > 5:
            self.is_old = True
        
dog_4 = LargeDog(5, 50, True)
print(f"LargeDog is {dog_4.age}. Is it old? {dog_4.is_old}")
dog_4.age_dog()
print(f"LargeDog is {dog_4.age}. Is it old? {dog_4.is_old}")
    
