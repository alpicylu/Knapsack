from item_cl import Item
from sack_cl import Knapsack
from thief_cl import Thief

""" current version on the program simulates the scenario, where the thief destroys the items that he threw out of his sack"""

if __name__ == "__main__":

    #      val, wgt, id
    A = Item(5, 1, "A")
    B = Item(2, 2, "B")
    C = Item(1, 3, "C")
    D = Item(10, 2, "D")
    E = Item(1, 2, "E")
    F = Item(10, 3, "F")
    G = Item(4, 5, "G")

    H = Item(7, 3, "H")

    zlodziej = Thief(18, "Knapsack/apartment.txt")
    zlodziej.zajeb(A)
    zlodziej.zajeb(B)
    zlodziej.zajeb(C)
    zlodziej.zajeb(D)
    zlodziej.zajeb(E)
    zlodziej.zajeb(F)
    zlodziej.zajeb(G)

    # zlodziej.debug_map_item_tuples(zlodziej.clac_potential_sets(F))    

    # potential_sets = zlodziej.clac_potential_sets(F)

    """outline of the function call sequence:
       1. calc_potential_sets  -- calculates all sets that are technically worth throwing away in exchange for the new item
       2. __map_collective_tuple_descr  -- the worhtwhile sets are converted into tuples (val, wgt, id)
       3. __qsort_collective_tuple_descr  -- the (val, wgt, id) tuples are sorted in an ascending order
       4. __throw_out_the_trash  -- based on the id parameter of the first tuple post-qsort, throw away all the worthless shit

       """


    """ things to look out for:
        1. are potential_sets calculating properly
        2. is the map_collective_tuple_descr mapping tuples properly
        3. is qsort sorting properly
        4. does throw_out_the_trash working well"""
    
    potential_sets = zlodziej.calc_potential_sets(H)


    # zlodziej.debug_map_collective_tuple_descr(potential_sets)

    # zlodziej.debug_qsort_the_trash(zlodziej.map_collective_tuple_descr(potential_sets))


    qsorted = zlodziej.qsort_collective_tuple_descr(zlodziej.map_collective_tuple_descr(potential_sets))

    zlodziej.worek.give_contents()

    print("-----SEPARATOR-----")

    zlodziej.throw_out_the_trash(qsorted, potential_sets)

    

    zlodziej.zajeb(H)


    zlodziej.worek.give_contents()




    

