#! /usr/bin/env python3
import argparse
from street import Street
from intersection import Intersection
from car import Car

class MetaData:
    def __init__(self, simulation_duration, intersections_number, streets_number, cars_number, bonus_points):
        self.simulation_duration = simulation_duration
        self.intersections_number = intersections_number
        self.streets_number = streets_number
        self.cars_number = cars_number
        self.bonus_points = bonus_points

    def __str__(self):
        return '''
Meta Data:
Simulation duration: {0}
Number of intersections: {1}
Number of streets: {2}
Number of cars: {3}
Bonus points per car finish: {4}
'''.format(self.simulation_duration, self.intersections_number, self.streets_number, self.cars_number, self.bonus_points)

def get_args():
    args = argparse.ArgumentParser()
    args.add_argument('file_name', help='The name of the input data file')
    return args.parse_args()

def get_street_object_from_name(streets, street_name):
    for street in streets:
        if street.name == street_name:
            return street
def get_street_id_from_name(streets, streets_name):
        index = 0
        for street in streets:
            if street.name == streets_name:
                return index
            index+= 1

def handle_input(data_file):
    with open(data_file) as data:
        data_lines = data.readlines()

    meta_data = data_lines[0].split()
    meta_data = MetaData(int(meta_data[0]), int(meta_data[1]), int(meta_data[2]), int(meta_data[3]), int(meta_data[4]))
    streets = []
    for street in data_lines[1:meta_data.streets_number + 1]:
        split_street = street.split()
        streets.append(Street(int(split_street[0]), int(split_street[1]), split_street[2], int(split_street[3])))

    cars = []
    for car in data_lines[meta_data.streets_number + 1: meta_data.streets_number + meta_data.cars_number + 1]:
        split_car = car.split()
        path = []
        for street in split_car[1:]:
            street_id = get_street_id_from_name(streets, street)
            path.append(get_street_object_from_name(streets, street))
            streets[street_id].total_cars_number += 1 # update a car added to this street

        cars.append(Car(int(split_car[0]), path))

    return meta_data, streets, cars

def main():
    args = get_args()
    meta_data, streets, cars = handle_input(args.file_name)
    print('All information is:')
    print(meta_data)
    for street in streets:
        print(street)
    for car in cars:
        print(car)

if __name__ == '__main__':
    main()