#!/bin/env/python
from typing import List
from street import Street

class Scheduler:
    # this clase is used for every intersection.
    # list of incoming start + time

    def __init__(self, ingoing_streets : List[Street]):
        self.ingoing_streets = ingoing_streets

    def very_stupid_schedule(self):
        return [(street, 10) for street in self.ingoing_streets]

    def calculate_according_to_total_cars(self):
        total_cars_in_scheduler = 0
        average_seconds_for_street = 3
        my_scheduler = []
        for street in self.ingoing_streets:
            total_cars_in_scheduler += street.total_cars_number

        for street in self.ingoing_streets:
            street_green_time = 0
            if total_cars_in_scheduler != 0:
                street_green_time = int((street.total_cars_number / total_cars_in_scheduler) * average_seconds_for_street * len(self.ingoing_streets))
            if street_green_time != 0:
                my_scheduler.append((street.name, street_green_time))
            else:
                if street.total_cars_number != 0:
                    my_scheduler.append((street.name, 1))


        return my_scheduler



