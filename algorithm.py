from car import Car
from street import Street
from input_parser import MetaData
from typing import List
from scheduler import Scheduler
from intersection import Intersection

class UltimateSolver:
    def __init__(self, meta_data: MetaData, streets: List[Street], cars: List[Car]):
        self.meta_data = meta_data
        self.streets = streets
        self.cars = cars

    def solve(self):
        all_intersections = [None] * self.meta_data.intersections_number
        for street in self.streets:
            intersection1 = street.start_intersection
            intersection2 = street.end_intersection
            if all_intersections[intersection1] is None:
                all_intersections[intersection1] = Intersection(intersection1)
            else:
                all_intersections[intersection1].add_outgoing_street(street)
            if all_intersections[intersection2] is None:
                all_intersections[intersection2] = Intersection(intersection2)
            else:
                all_intersections[intersection2].add_ingoing_street(street)

        result = {}
        for intersection in all_intersections:
            result[intersection.id] = intersection.calculate_scheduler()

        return result

    def __str__(self):
        out_str = 'Solver:'
        out_str += '-------------------------------------'
        out_str += 'Streets:'
        for street in self.streets:
            out_str += str(street)
        out_str += '-------------------------------------'
        out_str += 'Cars:'
        for car in self.cars:
            out_str += str(car)

    def create_scheduler(self) -> Scheduler:
        pass