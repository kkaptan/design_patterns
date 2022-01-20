from abc import ABC
from abc import abstractmethod
from collections import Counter

import numpy as np

class Animal(ABC):
    """Animal abstarct class"""
    @abstractmethod
    def eat(self):
        raise NotImplemented('eat not implemented.')

class Dog(Animal):
    """Dog"""
    def eat(self):
        print('Eats dog food.')

class Cat(Animal):
    """Cat"""
    def eat(self):
        print('Eats mice.')

class Duck(Animal):
    """Duck"""
    def eat(self):
        print('Eats small fish.')


class AnimalFactory(ABC):
    """Animal Factory abstract class"""
    @abstractmethod
    def create_animal(self) -> Animal:
        raise NotImplemented('')

class RandomAnimalFactory(AnimalFactory):
    """Random animal factory 
    returns a random animal class
    """
    def create_animal(self):
        switch = np.random.randint(3)
        if switch == 0:
            return Dog()
        elif switch == 1:
            return Cat()
        elif switch == 2:
            return Duck()

class BalancedAnimalFactory(AnimalFactory):
    """Balanced animal factory
    keeps track of all the object that it creates such that
    no class is allowed to be instantiated by more than one
    of the other classes.
    """

    def __init__(self):
        self._total = 0
        self._animal_dist = Counter({
            'cat':0,
            'dog':0,
            'duck':0
        })
        self._animal_classes = {
            'cat': Cat,
            'dog': Dog,
            'duck': Duck
        }

    def _treshold(self):
        return 1.0 / len(self._animal_dist)

    def create_animal(self):
        arr = []
        total = sum(self._animal_dist.values())

        for k, v in self._animal_dist.items():
            if total == 0:
                arr.append(k)
            elif v/total <= self._treshold():
                arr.append(k)
        
        switch = np.random.choice(arr)
        self._animal_dist[switch] += 1
        animal = self._animal_classes[switch]
        return animal()


if __name__ == '__main__':
    """You can substitute the RandomAnimalFactory with other 
    AnimalFactories to change the behaviour of how the Animal
    objects are instantiated
    """
    animal_factory = RandomAnimalFactory()
    for i in range(99):
        animal = animal_factory.create_animal()
        animal.eat()
