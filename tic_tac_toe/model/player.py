class Player:
    def __init__(self, name, symbol, is_human):
        self.name = name
        self.symbol = symbol
        self.is_human = is_human

    def __str__(self):
        return f'Name: {self.name}, Symbol: {self.symbol}, Is_human: {self.is_human}'
