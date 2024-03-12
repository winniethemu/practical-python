class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, num: int) -> None:
        if num <= self.shares:
            self.shares -= num
