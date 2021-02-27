#! /usr/bin/env python3
from data import GlobalData
from intersection import Intersection

class Street:
    def __init__(self, ingoing_intersection: str, outgoing_intersection: str, name: str, length: str):
        self.ingoing_intersection = int(ingoing_intersection)
        self.outgoing_intersection = int(outgoing_intersection)
        self.name = name
        self.length = int(length)

        self._add_intersections()

    def _add_intersections(self):
        if not GlobalData.intersections.get(self.outgoing_intersection):
            GlobalData.intersections[self.outgoing_intersection] = Intersection(self.outgoing_intersection)

        GlobalData.intersections[self.outgoing_intersection].add_ingoing_street(self.name)

        if not GlobalData.intersections.get(self.ingoing_intersection):
            GlobalData.intersections[self.ingoing_intersection] = Intersection(self.ingoing_intersection)

        GlobalData.intersections[self.ingoing_intersection].add_outgoing_street(self.name)

    def __str__(self):
        out_str = f'{self.name} Street:\n'
        out_str += f'   {self.ingoing_intersection=}\n'
        out_str += f'   {self.outgoing_intersection=}\n'
        out_str += f'   {self.length=}'
        return out_str


if __name__ == '__main__':
    print(Street('1', '17', 'Eli Eildis blvd.', 18))
