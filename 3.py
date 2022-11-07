class Dog:
    allowed_outside = True
    is_good_boy = True
    
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.is_old = False
        self.medication = None

    def age_dog(self):#instance method
        self.age +=1
        return self.age

    @classmethod #class method
    def toggle_allowed(cls):
        cls.allowed_outside = not cls.allowed_outside

class SmallDog(Dog):

    def __init__(self, age, weight, is_yappy):
        super().__init__(age, weight)
        self.is_yappy = is_yappy
        self.check_weight() #run on instantiation
    
    def check_weight(self):
        if self.weight > 10:
            print("This is not a small dog!")

class LargeDog(Dog):

    def __init__(self, age, weight, leash_trained):
        super().__init__(age, weight)
        self.leash_trained = leash_trained
    
    def age_dog(self):
        self.age += 1
        if self.age > 5:
# Lets update 'is_old' to do something
            #self.is_old = True
            self.medication=(Meds(1, 'hip medication'))

# ---- Composition (has-a relationship)
class Meds:

    def __init__(self, number, med_type):
        self.number = number
        self.med_type = med_type

dog_5 = LargeDog(5, 50, True)
print(f"LargeDog is old? {dog_5.is_old} Meds = {dog_5.medication} ")
dog_5.age_dog()
print(f"LargeDog is old? {dog_5.is_old} Meds = {dog_5.medication.number} {dog_5.medication.med_type} ")
