from typing import List
from street import Street

class Car():
    def __init__(self, path_len: int, path: List[Street]):
        self.path_len = path_len
        self.path = path

        self.current_index = 0
        self.distance_left = self.path[self.current_index].length
        self.queued = True
        self.driving = False

    def cross_street(self):
        self.current_index += 1
        if self.current_index == self.path_len:
            self.distance_left = self.path[self.current_index].length

    def tick(self):
        if self.queued:
            return
        if self.driving:
            self.distance_left -= 1
            if self.distance_left == 0:
                self.driving = False
                self.queued = True


