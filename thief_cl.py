from sack_cl import Knapsack
from item_cl import Item
import itertools as it
import sys

class Thief:

    def __init__(self, capacity: int, apartment: str) -> None:
        self.worek = Knapsack(capacity)
        self.mieszkanie = apartment


    def calc_subset_wgt(self, subset: it.combinations) -> int:
        sum = 0
        for i in subset:
            sum += i.give_wgt()
        return sum

    def clac_subset_val(self, subset: it.combinations) -> int:
        sum = 0
        for i in subset:
            sum += i.give_val()
        return sum
    
    def clac_potential_sets(self, item: Item) -> list:
        output_list = []

        for n in list(range(1, self.worek.give_num_of_items()+1)): #all possible combinations of n items

            possible = it.combinations(self.worek.contents, n) # possible is a 'it.combinations' object (a "list") of subsets

            for p in possible:
                subset_val = self.clac_subset_val(p)
                subset_wgt = self.calc_subset_wgt(p)

                if (self.worek.give_total_wgt() + item.give_wgt() - subset_wgt <= self.worek.capacity and
                    self.worek.give_total_val() < self.worek.give_total_val() - subset_val + item.give_val()):

                    output_list.append(p)
        
        return output_list

                #     for i in p:
                #         self.worek.contents.remove(i)

                #     self.worek.contents.append(item) 


    def zajeb(self, item: Item) -> None:
        self.worek.put_in(item)


    def sack_the_place(self) -> None:
        """ for testing, the function will just retrieve one item """
        with open(self.mieszkanie, "r") as sys.stdin:
            id = str(input())
            val = int(input())
            wgt = int(input())

            print("{} {} {}".format(id, val, wgt))

