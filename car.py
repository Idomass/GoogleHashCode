from typing import List
from street import Street

class Car():
    def __init__(self, path_len: int, path: List[Street]):
        self.start_street = start_street
        self.current_street = start_street
        self.current_street_index = 0
        self.next_street = path[1]
        self.next_street_index = 1
        self.path_len = path_len
        self.path = path

        self.total_time = 0

        for street in path:
            self.total_time = self.total_time + street.length

        self.remaining_time = self.total_time

    def __str__(self):
        return ("car: with path: {}, now at {}".format(self.path, self.current_street))

    def cross_next_street():
        self.current_street_index = self.current_street_index + 1
        self.current_street = self.next_street

        self.next_street_index = self.next_street_index + 1
        self.next_street = self.path[self.next_street_index]

        self.remaining_time = self.remaining_time - self.current_street.length

        


        


