import random
# Reference Code: https://www.youtube.com/watch?v=Cn7AkDb4pIU
# Parent Class
# Super Class
# Should be logical name (for simplicity using class A)
class A:
    """
    This class has 2 features
    """
    def feature_1(self):
        print("Feature 1 working")

    def feature_2(self):
        print("Feature 2 working")
# Class B is a child class of Class A
# Sub Class
class B:
    """
    This class has 2 features
    """
    def feature_3(self):
        print("Feature 3 operational")

    def feature_4(self):
        print("Feature 4 working")

class C(A,B):
    def feature_5(self):
        print("Feature 5 working")

heroes = [
    "Athena",
    "Jodie Foster",
    "Wonder Woman"]

# A way you can access the class is with the help of object
a1 = A()
b1 = B()
c1 = C()

a1.feature_1()
a1.feature_2()

c1.feature_3()

name_of_hero = random.randint(0, 4)
# print(heroes[name_of_hero])
print(heroes[name_of_hero])
