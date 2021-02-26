#! /usr/bin/env python3
from data import GlobalData
from intersection import Scheduler

def silly_algorithm():
    for car in GlobalData.cars:
        for street in car.streets:
            GlobalData.intersections[street.outgoing_intesection].add_weight(street.name)

    print(GlobalData.meta_data)
    for intersection in GlobalData.intersections.values():
        scheduler = str(Scheduler(intersection))
        if scheduler:
            print(scheduler)
