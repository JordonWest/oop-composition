class Dog:
    #what do all dogs have
    allowed_outside = True
    is_good_boy = True

    #what do all dogs have (variable to the dog)
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.is_old = False
        self.medication = []

    # instance method
    def age_dog(self):
        self.age +=1
        return self.age
    # Methods that are only invoked on the class - not instances
    @classmethod
    def toggle_allowed(cls):
        cls.allowed_outside = not cls.allowed_outside
# ------ INHERITANCE  (is-a relationship)
class SmallDog(Dog):

    def __init__(self, age, weight, is_yappy):
        super().__init__(age, weight)
        self.is_yappy = is_yappy
        self.check_weight() #run on instantiation - new thing?

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
            self.is_old = True
            self.medication=Medication(1, 'hip medication')

# ---- Composition (has-a relationship)
class Medication:

    def __init__(self, number, med_type):
        self.number = number
        self.med_type = med_type

    def __str__(self):
        return f"""
            Number of meds: {self.number}
            Type of meds: {self.med_type}
            """
dog_5 = LargeDog(5, 50, True)
dog_5.age_dog()
print(dog_5.medication)
