import decimal
from math import factorial as fac


class Game:

    def __init__(self, file_path="e.txt", digits=100):
        # to load arguments
        self.file_path = file_path
        self.digits = digits

        # boolean states of the game
        self.states = {
            "running": True
        }

        # to initialize the precision
        self.dec = decimal.Decimal
        try:
            decimal.getcontext().prec = len(open(self.file_path, "r").read())-1 + self.digits
        except FileNotFoundError:
            decimal.getcontext().prec = self.digits

        # to load n and e
        try:
            self.n = int(open("n.txt", "r").read())
            self.e = [self.dec(open(self.file_path, "r").read())+self.dec(1/fac(self.n)),
                      self.dec(open(self.file_path, "r").read())]
        except FileNotFoundError:
            self.n = 0
            self.e = [self.dec(1/fac(self.n)), self.dec(0)]

        # to initialize i (index of calculation)
        self.i = self.n + 1

    def handling_events(self):
        pass

    def update(self):
        if self.e[0] != self.e[1]:
            self.e[0] += self.dec(1/fac(self.i))
            self.e[1] = self.e[0] + self.dec(1/fac(self.i))
            self.i += 1

            open("n.txt", "w").write(str(self.n + self.i))
            open(self.file_path, "w").write(str(self.e[0]))
        else:
            self.states["running"] = False

    def display(self):
        pass

    def run(self):
        # game LOOP
        while self.states["running"]:
            # check events
            self.handling_events()
            # the logic of the game
            self.update()
            # display
            self.display()
