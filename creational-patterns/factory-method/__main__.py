from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_product(self):
        pass


class ProductA(Product):
    def get_product(self):
        return "It`s ProductA"


class ProductB(Product):
    def get_product(self):
        return "It`s ProductB"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        product = self.factory_method()
        print(f"Creator: \"{product.get_product()}\"")


class CreatorA(Creator):
    def factory_method(self):
        return ProductA()


class CreatorB(Creator):
    def factory_method(self):
        return ProductB()


def client_creator(creator: Creator):
    creator.some_operation()


if __name__ == "__main__":
    client_creator(CreatorA())
    client_creator(CreatorB())
