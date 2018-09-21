# Reference for learning classes and inhertiance
# class Dog:
#     greeting = "Woof!"
#
#     def __init__(self, name):
#         self.name = name
#
#     def bark(self):
#         print(self.greeting)

# my_first_dog = Dog("Annie")
# my_second_dog = Dog("Wyatt")
#
# print(my_first_dog.name)
# print(my_second_dog.name)
#
# my_first_dog.bark()
# my_second_dog.bark()

# This always goes at the bottom
# if __name__ == "__main__":
#     my_dog = Dog()
#     my_dog.bark()
# ==============================================================================
# Inheritance
class Animal:
    def __init__(self, name, sleep_duration): # There is an error with the argument and property not being the same
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours.".format(
            self.name,
            self.sleep_duration))

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()
