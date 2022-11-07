# the most basic class

class basic:
    pass

basic=basic()

#use dir() to find out what is available inclass

dir(basic)

# classes in general are good when grouping code and behaviour that can be reused
#That type of grouping is not possible with function for below eg

class Dog:
    is_animal = True

    def bark(self):
        print("woof")

dog=Dog()

#dog class is instantiated and ready to be used, we can now interact with its parts

dog.bark()
dog.is_animal


# can create as many instances of this class as you need

rufus=Dog()
rufus.bark()

#watch out for class attributes that can change "state" from every instance and object

Dog.is_animal=False
print("Is rufus an animal?",rufus.is_animal)
print("is dog an animal?",dog.is_animal)

#that change will effect future objects too

sparky=Dog()
sparky.is_animal
