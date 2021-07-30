from math import factorial
import decimal
from datetime import datetime
from time import time


def calc_e():

    def e_(precision=100):
        dec = decimal.Decimal
        decimal.getcontext().prec = precision
        try:
            n = int(open("n.txt", "r").read())
            e = [dec(open("e.txt", "r").read())+dec(1/factorial(n)), dec(open("e.txt", "r").read())]
            open("log.txt", "a").write("n.txt e.txt loaded\n")
        except FileNotFoundError:
            n = 0
            e = [dec(1 / factorial(n)), dec(0)]
            open("log.txt", "a").write("n.txt e.txt FileNotFoundError\n")
        i = n + 1

        calculation_time = time()
        while e[0] != e[1]:
            e[0] += dec(1/factorial(i))
            e[1] = e[0] + dec(1/factorial(i))
            i += 1
        open("log.txt", "a").write(f"calculation completed : {time()-calculation_time}sec\n")
        open("log.txt", "a").write(f"precision = {precision}\n")

        open("n.txt", "w").write(str(n+i))
        open("log.txt", "a").write("n saved in n.txt\n")

        open("e.txt", "w").write(str(e[0]))
        open("log.txt", "a").write("e saved in e.txt\n")

        open("precision.txt", "w").write(str(precision))
        open("log.txt", "a").write("precision saved in precision.txt\n")

    open("log.txt", "a").write(f"{datetime.now()}\n")

    try:
        open("log.txt", "a").write("precision.txt loaded\n")
        e_(precision=int(open("precision.txt", "r").read())+100)
    except FileNotFoundError:
        open("log.txt", "a").write("precision.txt FileNotFoundError\n")
        e_()

    open("log.txt", "a").write("\n")


if __name__ == "__main__":
    calc_e()
