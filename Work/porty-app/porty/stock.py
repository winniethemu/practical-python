from .typedproperty import String, Integer, Float


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'

    '''
    Decorator syntax, equivalent to:

    def property(func):
        def wrapper(*args, **kwargs):
            ...
            return func(*args, **kwargs)
        return wrapper

    cost = property(cost)
    '''
    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, num: int) -> None:
        if num <= self.shares:
            self.shares -= num
