from item_cl import Item
from sack_cl import Knapsack
from thief_cl import Thief

""" current version on the program simulates the scenario, where the thief destroys the items that he threw out of his sack"""

if __name__ == "__main__":

    # worek = Knapsack(10)

    A = Item(5, 1, "A")
    B = Item(2, 2, "B")
    C = Item(1, 3, "C")
    D = Item(10, 2, "D")
    E = Item(1, 2, "E")

    F = Item(10, 3, "F")

    # worek.put_in(A)
    # worek.put_in(B)
    # worek.put_in(C)

    # print("{}".format(worek.give_total_wgt()))

    zlodziej = Thief(5, "Knapsack/apartment.txt")
    # zlodziej.zajeb(A)
    zlodziej.zajeb(B)
    zlodziej.zajeb(C)
    # zlodziej.zajeb(D)
    # zlodziej.zajeb(E)

    potential_sets = zlodziej.clac_potential_sets(F)




