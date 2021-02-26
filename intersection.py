#! /usr/bin/env python3
from data import GlobalData

class Intersection:
    def __init__(self, id: str):
        self.id = int(id)

        self.ingoing_streets = []
        self.outgoing_streets = []

    def add_ingoing_street(self, street: str):
        self.ingoing_streets.append(street)

    def add_outgoing_street(self, street: str):
        self.outgoing_streets.append(street)

    def __str__(self):
        out_str = 'Intersection class:\n'
        out_str += f'{self.id=}\n'
        out_str += 'Ingoing streets:\n'
        for ingoing in self.ingoing_streets:
            out_str += f'    {ingoing}\n'
        out_str += 'Outgoing streets:\n'
        for outgoing in self.outgoing_streets:
            out_str += f'    {outgoing}\n'
        return out_str
