from item_cl import Item
from sack_cl import Knapsack
from thief_cl import Thief


if __name__ == "__main__":

    # worek = Knapsack(10)

    # A = Item(5, 1, "A")
    # B = Item(2, 2, "B")
    # C = Item(1, 3, "C")

    # worek.put_in(A)
    # worek.put_in(B)
    # worek.put_in(C)

    # print("{}".format(worek.give_total_wgt()))

    zlodziej = Thief(10, "Knapsack/apartment.txt")

    zlodziej.sack_the_place()



