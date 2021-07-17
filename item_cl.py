

"""
The main purpose of creating the Item class is that i need to keep track of all the possible "replacements".
If the thief encounters a valuable item, and there are multiple options to replace already stolen
item (or sets of items) with the newfound one, first i need to list all worthwhile sets of replacable items.
"""

class Item:

    def __init__(self, value: int, weight: int, id: str) -> None:
        self.__value = value
        self.__weight = weight
        self.__id = id

    def show_item(self) -> None:
        print("ID:{}, Weight:{}, Value:{}".format(self.__id, self.__weight, self.__value))

    def give_val(self) -> int:
        return self.__value
        
    def give_wgt(self) -> int:
        return self.__weight

    def give_id(self) -> str:
        return self.__id