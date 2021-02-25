from car import Car
from street import Street
from typing import List
from scheduler import Scheduler

class UltimateSolver:
    def __init__(self, streets: List[Street], cars: List[Car]):
        self.streets = streets
        self.cars = cars

    def solve(self):
        scheduler = self.create_scheduler()

        print('Scheduler ->', scheduler)
        scheduler.serialize('solution.txt')

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