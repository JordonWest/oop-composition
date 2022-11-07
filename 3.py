class Dog:
    allowed_outside = True
    is_good_boy = True
    
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.is_old = False
### add this after bottom VVVV
        self.medication = None

    def age_dog(self):#instance method
        self.age +=1
        return self.age

    @classmethod #class method
    def toggle_allowed(cls):
        cls.allowed_outside = not cls.allowed_outside

# ------ INHERITANCE  (is-a relationship)
class SmallDog(Dog):

    def __init__(self, age, weight, is_yappy):
        super().__init__(age, weight)
        self.is_yappy = is_yappy
        self.check_weight() #run on instantiation
    
    def check_weight(self):
        if self.weight > 10:
            print("This is not a small dog!")
##          DELETE ALL THIS VVV
#dog_2 = SmallDog(5, 22, False)
#dog_3 = SmallDog(5, 8, False)
##          DELETE ALL THIS ^^^

class LargeDog(Dog):

    def __init__(self, age, weight, leash_trained):
        super().__init__(age, weight)
        self.leash_trained = leash_trained
    
    def age_dog(self):
        self.age += 1
        if self.age > 5:
# Lets update 'is_old' to do something
            self.medication=(Medication(1, 'hip medication'))

##          DELETE ALL THIS VVV
#dog_4 = LargeDog(5, 50, True)
#print(f"LargeDog is {dog_4.age}. Is it old? {dog_4.is_old}")
#dog_4.age_dog()
#print(f"LargeDog is {dog_4.age}. Is it old? {dog_4.is_old}")
##          DELETE ALL THIS ^^^

####        ----- ADD ALL THIS VVVVVVV ------

# ---- Composition (has-a relationship)
class Medication:

    def __init__(self, number, med_type):
        self.number = number
        self.med_type = med_type

dog_5 = LargeDog(5, 50, True)
print(f"LargeDog is old? {dog_5.is_old} Meds = {dog_5.medication} ")
dog_5.age_dog()
print(f"LargeDog is old? {dog_5.is_old} Meds = {dog_5.medication.number} {dog_5.medication.med_type} ")
