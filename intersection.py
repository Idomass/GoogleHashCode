#! /usr/bin/env python3
from data import GlobalData

class Intersection:
    def __init__(self, id: str):
        self.id = int(id)

        self.ingoing_streets = {}
        self.outgoing_streets = []

    def add_weight(self, street: str):
        self.ingoing_streets[street] += 1

    def add_ingoing_street(self, street: str):
        self.ingoing_streets[street] = 0

    def add_outgoing_street(self, street: str):
        self.outgoing_streets.append(street)

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
        self.total_weight = sum(self.intersection.ingoing_streets.values())
        self.cycle_time = len(self.intersection.ingoing_streets) * 6
        for street, weight in self.intersection.ingoing_streets.items():
            self.schdule[street] = int((weight/self.total_weight)*self.cycle_time)

    def __str__(self):
        out_str = f'{self.intersection.id}\n'

        total_ingoing = len(self.intersection.ingoing_streets)
        solve_str = ''
        for street, weight in self.schdule.items():
            if weight > GlobalData.meta_data.duration:
                raise Exception("SHIT")
            if weight == 0:
                total_ingoing -= 1
                continue
            solve_str += f'{street} {weight}\n'
        out_str += f'{total_ingoing}\n'
        out_str += solve_str
        return out_str
