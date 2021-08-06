from sack_cl import Knapsack
from item_cl import Item
import itertools as it
import sys

class Thief:

    def __init__(self, capacity: int, apartment: str) -> None:
        self.worek = Knapsack(capacity)
        self.mieszkanie = apartment

    """its purpose is to map a list of tuples of items (the potential-throwaway sets) into a
       list of tuples of 3 values: collective value, collective weight, and original index of the set (val, wgt, id).
       Example: [(A, G, D), (D, B), (A, G)] will map into [(val0, wgt0, 0), (val1, wgt1, 1), (val2, wgt2, 2)] where the
       uppercase letters are item objects. This is done so that a modified quicksort does not have to perform too many distinctive actions.
       Despite its function (mapping) it wont be utilised by a map() function - that is because map() takes in as an argument
       an iterable of objects and runs those objects one by one through the given function. Since it runs the mapping function multiple times
       it cannot increment the set_id variable. A way to circumvent this would be to define a generator outside this function that would yield
       an incremented integer each time its called, but that a little to over-ingineered, so ill stick with just a simple function call (no map())"""
    def map_collective_tuple_descr(self, list_of_possible: list) -> tuple:

        mapped_list = []
        set_id = 0

        for set in list_of_possible:
            set_val = 0
            set_wgt = 0

            for item in set:
                set_val += item.give_val()
                set_wgt += item.give_wgt()
        
            mapped_list.append((set_val, set_wgt, set_id))

            set_id+=1

        return(mapped_list)
    

    """this function performs a quick sort on the list of tuples of attributes (see map_collective_tuple_descr()) and then returns
       an index attribute of the first (0-th) set. Sorts in ascending order by value and then in descending by mass(TODO), so that if multiple
       sets have the same value but different masses, it will choose the set with the highest mass from the sets of the lowest value"""
    def qsort_collective_tuple_descr(self, mapped_tuple_list) -> list:

        if len(mapped_tuple_list) <= 1:
            return(mapped_tuple_list)

        else:
            left_tuple_list = []
            right_tuple_list = []
            pivot = [mapped_tuple_list[0]]

            for tupl in mapped_tuple_list[1:]:
                if tupl[0] <= pivot[0][0]: left_tuple_list.append(tupl)   
                else:                      right_tuple_list.append(tupl)
            
            left_tuple_list = self.qsort_collective_tuple_descr(left_tuple_list)
            right_tuple_list = self.qsort_collective_tuple_descr(right_tuple_list)

            pivot.extend(right_tuple_list)
            left_tuple_list.extend(pivot)

        return left_tuple_list


    """this function removes the most worthless items from the knapsack.
    
       qsorted_descr_tuples is the list of descriptor tuples (see map_collective_tuple_descr) that have been sorted by the qsort method.
       
       potential_sets is the list of sets of items that have been produced by calc_potential_sets()"""
    def throw_out_the_trash(self, qsorted_descr_tuples, potential_sets) -> None:
        
                                             #qsorted_descr_tuples[0][2] basically retrieves the index of the worst tuple
        tuple_of_worst_items = potential_sets[qsorted_descr_tuples[0][2]]

        for item in tuple_of_worst_items:
            self.worek.remove(item.give_id())

    #DEBUG START-------------------------

    #prints out the returned value of map_collective_tuple_descr
    def debug_map_collective_tuple_descr(self, list_of_possible: list) -> None:
        descriptors = ["worth", "weight", "index"]

        list_collective_tuple_descr = self.map_collective_tuple_descr(list_of_possible)

        for i in list(range(len(list_of_possible))):
            for item in list_of_possible[i]:
                print(item.give_id(), end=" ")
            
            print("\n")
            
            for k in list(range(3)):
                print("{}: {}".format(descriptors[k], list_collective_tuple_descr[i][k]))
        
            print("-----------------")
            
    def debug_calc_potential_sets(self, item: Item) -> None:
        
        for tup in self.calc_potential_sets(item):
            for item in tup:
                print(item.give_id())
            print("------------")

    def debug_qsort_the_trash(self, mapped_tupule_list) -> None:

        #here, tupl is a tuple of the 3 values: (val, wgt, id)
        for tupl in self.qsort_collective_tuple_descr(mapped_tupule_list):
            print("val: {}, wgt: {}, id: {}".format(tupl[0], tupl[1], tupl[2]))
        


    #DEBUG END----------------------------

    def calc_subset_wgt(self, subset: tuple) -> int:
        sum = 0
        for i in subset:
            sum += i.give_wgt()
        return sum

    def clac_subset_val(self, subset: tuple) -> int:
        sum = 0
        for i in subset:
            sum += i.give_val()
        return sum
    
    """This function is responsible for creating a list of tuples of items that meet the following criteria:
       1. the weight of the sack after removing a set of items and adding the new item stays within the weight limit.
       2. the value of the sack after removing a set of items and adding the new item has increased
       
       After the qsort sorts the """
    def calc_potential_sets(self, item: Item) -> list:
        output_list = []

        for n in list(range(1, self.worek.give_num_of_items()+1)): #all possible combinations of n items

            """check if it is possible to calculate only the items that meet the criteria insted of calculating all objects
                and then filtering them"""

            possible = it.combinations(self.worek.contents, n) # possible is a 'it.combinations' object (a "list") of subsets

            for p in possible: # every 'p' is a TUPLE of <item_cl.Item> objects
                subset_val = self.clac_subset_val(p)
                subset_wgt = self.calc_subset_wgt(p)

                if (self.worek.give_total_wgt() + item.give_wgt() - subset_wgt <= self.worek.capacity and
                    self.worek.give_total_val() < self.worek.give_total_val() - subset_val + item.give_val()):

                    output_list.append(p)
        
        return output_list

    def zajeb(self, item: Item) -> None: self.worek.put_in(item)

    def sack_the_place(self) -> None:

        pass

