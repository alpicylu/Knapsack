from item_cl import Item 


class Knapsack:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.contents = []
        
    def put_in(self, item: Item) -> None:
        self.contents.append(item)

    def remove(self, id: str) -> None:
        for item in self.contents:
            if item.give_id() == id: self.contents.remove(item)
    
    def give_contents(self) -> None:
        for i in self.contents:
            i.show_item()

    def give_total_val(self) -> int:
        sum = 0
        for i in self.contents:
            sum += i.give_val()
        return sum
    
    def give_total_wgt(self) -> int:
        sum = 0
        for i in self.contents:
            sum += i.give_wgt()
        return sum

    def give_num_of_items(self) -> int:
        sum = 0
        for i in self.contents:
            sum+=1
        return sum