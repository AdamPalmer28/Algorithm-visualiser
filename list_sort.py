"Handles the list sorting of the for visualisation"

import numpy as np
import random 
class list_sorter:

    def __init__(self, n, method):
        self.size = n
        self.values = random.sample(range(n), n) # creates random list
        self.method = method # 0 = bubble sort

    def sort_iteration(self, ind) -> bool:
        "1 iteration of sorting algorithm (depending on method)"
        if self.method == 0:
            # bubble sort
            swap = self.bubble_sort(ind)
        
        return swap


    def bubble_sort(self, ind) -> bool:
        "1 iteration of bubble_sort"
        if self.values[ind] > self.values[ind + 1]:
            # swap elements
            self.values[ind], self.values[ind + 1] = self.values[ind + 1], self.values[ind]
            return True


if __name__ == '__main__':
    num = values_sorter(5, 0)
    print(num.values)
    for i in range(4):
        num.sort_iteration(i)
        print(num.values)