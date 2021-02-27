#! /usr/bin/env python3
from data import GlobalData
import math

class Intersection:
    def __init__(self, id: str):
        self.id = int(id)

        self.ingoing_streets = {}
        self.outgoing_streets = []

        # save the counts of cars starting in the street
        self.ingoing_streets_preferncy = {}

    def add_weight(self, street: str, weight: int):
        # street name, and weight is the number of cars that will be on this street
        self.ingoing_streets[street] += weight
            

    def add_ingoing_street(self, street: str):
        self.ingoing_streets[street] = 0
        self.ingoing_streets_preferncy[street] = 0

    def add_outgoing_street(self, street: str):
        self.outgoing_streets.append(street)

    def add_start_preferncy(self, street: str, street_index: int):
        # give it kdimut
        # self.ingoing_streets_preferncy[street] += 3 / (street_index + 1) - street_index*5
        if street_index == 0:
            self.ingoing_streets_preferncy[street] += 1

    def __str__(self):
        out_str = 'Intersection class:\n'
        out_str += f'{self.id=}\n'
        out_str += 'Ingoing streets:\n'
        for ingoing in self.ingoing_streets.keys():
            out_str += f'    {ingoing}\n'
        out_str += 'Outgoing streets:\n'
        for outgoing in self.outgoing_streets:
            out_str += f'    {outgoing}\n'
        return out_str


class Scheduler:
    def __init__(self, intersection: Intersection):
        self.intersection = intersection

        self.schdule = {}
        self.calculate_weights()

    def calculate_weights(self):
        self.total_weight = sum(self.intersection.ingoing_streets.values())
        for street, weight in self.intersection.ingoing_streets.items():
            if weight/self.total_weight > 0.80:
                # for really specical cases
                weight = weight*1.7
            # if weight/self.total_weight < 0.01:
                # for really specical cases
                # weight = 0
            self.schdule[street] = math.ceil(weight/self.total_weight*1.5)

    def calculate_according_to_total_cars(self, intersection: Intersection):
        total_cars_in_scheduler = 0
        average_seconds_for_street = 3
        my_scheduler = []
        for street in intersection.ingoing_streets:
            total_cars_in_scheduler += street.total_cars_number

        for street in intersection.ingoing_streets:
            street_green_time = 0
            if total_cars_in_scheduler != 0:
                street_green_time = int((street.total_cars_number / total_cars_in_scheduler) * average_seconds_for_street * len(intersection.ingoing_streets))
            if street_green_time != 0:
                my_scheduler.append((street.name, street_green_time))
            else:
                if street.total_cars_number != 0:
                    my_scheduler.append((street.name, 1))


        return my_scheduler

    def __str__(self):
        out_str = f'{self.intersection.id}\n'

        total_ingoing = len(self.intersection.ingoing_streets)
        solve_str = ''
        for street in sorted(self.intersection.ingoing_streets_preferncy, key=self.intersection.ingoing_streets_preferncy.get, reverse=True):
            street, weight = street, self.schdule[street]
            if weight > GlobalData.meta_data.duration:
                raise Exception("SHIT")
            if weight == 0:
                total_ingoing -= 1
                continue
            solve_str += f'{street} {weight}\n'
        out_str += f'{total_ingoing}\n'
        out_str += solve_str
        return out_str
