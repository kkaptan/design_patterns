from abc import ABC
from abc import abstractmethod


class Beverage(ABC):
    """Beverage"""

    @abstractmethod
    def description(self) -> str:
        raise NotImplemented('description method not implemented.')
    
    @abstractmethod
    def cost(self) -> float:
        raise NotImplemented('cost method not implemented.')


class Espresso(Beverage):
    """Espresso Beverage"""
    
    def description(self):
        return 'Espresso'
    
    def cost(self):
        return 1.0


class Americano(Beverage):
    """Americano Beverage"""

    def description(self):
        return 'Americano'

    def cost(self):
        return 1.20


class BeverageAddOnDecorator(Beverage):
    """Beverage Add on is a Beverage and 
    has a/uses a Beverage instance"""

    def __init__(self, beverage: Beverage):
        self._beverage = beverage


class CreamAddOnDecorator(BeverageAddOnDecorator):
    """Cream add on decorator"""

    def __init__(self, beverage):
        super().__init__(beverage)

    def description(self):
        return self._beverage.description() + "\n with cream"

    def cost(self):
        return self._beverage.cost() + .50 


class MilkAddOnDecorator(BeverageAddOnDecorator):
    """Milk add on decorator """
    
    def __init__(self, beverage):
        super().__init__(beverage)

    def description(self):
        return self._beverage.description() + "\n with milk"

    def cost(self):
        return self._beverage.cost() + .45 


if __name__ == '__main__':
    esp = Espresso()
    esp_cream = CreamAddOnDecorator(esp)
    esp_cream_milk = MilkAddOnDecorator(esp_cream)
    print(esp_cream_milk.cost(), esp_cream_milk.description())
    
    ame = Americano()
    ame_milk = MilkAddOnDecorator(ame)
    print(ame_milk.cost(), ame_milk.description())
