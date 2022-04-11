class Calculator:
    def __init__(self):
        self.miles = 0
        self.km = 1.6

    def conversion_calculator(self, *args):
        for n in args:
            self.miles *= self.km
        return self.miles


# 1 * 1.609344
