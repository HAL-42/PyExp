# -*- coding: utf-8 -*-
# @Author: Xiaobo Yang
import MyErr

class Animal:

    name = "Animal"
    feed_on = "Air"
    amt = 0
    predator = "Bald Ape"

    def __init__(self, name: str, feed_on: str, amt: int, habitat: str):
        self.name = name
        self.feed_on = feed_on
        self.amt = amt
        self.habitat = habitat

    def howl(self):
        print(self)

    def __add__(self, other):
        if self.name != other.name:
            raise MyErr.CanNotAddErr(self.name + " is not identical to " + other.name)
        return Animal(name=self.name, feed_on=self.feed_on,
                      amt=self.amt + other.amt, habitat=self.habitat)

    def __str__(self):
        return "{amt} of us, called {name} feeding on {feed_on} live in {habitat}".format(
            amt=self.amt, name=self.name, feed_on=self.feed_on, habitat=self.habitat)


ani1 = Animal(name = "Dog", feed_on="Bone", habitat = "Human house", amt = 10)
ani1.howl()

ani2 = Animal(name = "Dog", feed_on="Bone", habitat = "Human house", amt = 10)
ani2.howl()

ani3 = ani1 + ani2
ani3.howl()

ani4 = Animal(name = "Panda", feed_on="Bone", habitat = "Human house", amt = 10)
try:
    ani5 = ani1 + ani4
except MyErr.MyErr as err:
    print(err)
else:
    ani5.howl()

class Dog(Animal):

    def __init__(self, color: str):
        Animal.__init__(self, name = "dog", feed_on="Bone", habitat = "Human house", amt = 1)
        self.color = color

    def howl(self):
        print("Wang Wang Wang")

dog1 = Dog("Yellow")
dog2 = Dog("White")
dog3 = dog1 + dog2
print(dog3.amt)
dog1.howl()








