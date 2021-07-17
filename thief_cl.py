from sack_cl import Knapsack
import sys

class Thief:

    def __init__(self, capacity: int, apartment: str) -> None:
        self.worek = Knapsack(capacity)
        self.mieszkanie = apartment

    def sack_the_place(self) -> None:
        """ for testing, the function will just retrieve one item """
        with open(self.mieszkanie, "r") as sys.stdin:
            id = str(input())
            val = int(input())
            wgt = int(input())

            print("{} {} {}".format(id, val, wgt))

