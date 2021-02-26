#! /usr/bin/env python3
from data import GlobalData
from intersection import Scheduler


def silly_algorithm():
    for car in GlobalData.cars:
        for street in car.streets:
            GlobalData.intersections[street.outgoing_intesection].add_weight(
                street.name, 1)
    solve()

def smarter_algorithm():
    for car in GlobalData.cars:
        journey_to_street = 0
        for street in car.streets:
            journey_to_street += street.length
            weight = GlobalData.meta_data.duration / journey_to_street
            GlobalData.intersections[street.outgoing_intesection].add_weight(street.name, weight)
    solve()

def solve():
    solve = ''
    for intersection in GlobalData.intersections.values():
        if len(intersection.ingoing_streets) and sum(intersection.ingoing_streets.values()):
            solve += str(Scheduler(intersection))
        else:
            GlobalData.meta_data.intersections -= 1
    print(GlobalData.meta_data.intersections)
    print(solve)
